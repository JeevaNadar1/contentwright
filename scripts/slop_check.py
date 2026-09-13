#!/usr/bin/env python3
"""slop_check.py - mechanical AI-slop detector for contentwright output.

Usage:
    python slop_check.py draft.md
    python slop_check.py draft.md --extra-banned my_words.txt
    python slop_check.py draft.md --json

Exit codes:
    0  clean
    1  hard failures present
    2  bad usage / file not found

Hard failures: banned punctuation, banned vocabulary, banned sentence shapes.
Warnings: rhythm, length, contraction rate, second-person density, uniform paragraphs.
Stdlib only. No network.
"""

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

BANNED_PUNCT = {
    "\u2014": "em dash",
    "\u2015": "horizontal bar",
    "\u2e3a": "two-em dash",
    "\u2e3b": "three-em dash",
}

# en dash only counts when used as punctuation between spaces, not in ranges
EN_DASH_PUNCT = re.compile(r"(?<=\s)\u2013(?=\s)|(?<=\w)\u2013(?=\s)|(?<=\s)\u2013(?=\w)")

BANNED_WORDS = [
    "delve", "delving", "unlock", "unlocking", "elevate", "elevating", "harness",
    "robust", "seamless", "seamlessly", "streamline", "streamlining", "empower",
    "empowering", "foster", "fostering", "game-changer", "game changer",
    "gamechanger", "revolutionary", "cutting-edge", "cutting edge",
    "state of the art", "state-of-the-art", "transformative", "testament to",
    "tapestry", "beacon", "synergy", "holistic", "curated", "best-in-class",
    "world-class", "next-level", "paradigm shift", "deep dive", "let's dive in",
    "lets dive in", "buckle up", "spoiler alert", "plot twist",
    "at the end of the day", "needless to say", "it goes without saying",
    "furthermore", "moreover", "in conclusion", "to summarise", "to summarize",
    "pivotal", "myriad", "plethora", "boasts", "resonate", "resonates",
    "unpack", "lean into", "supercharge", "turbocharge", "simply put",
    "essentially", "fundamentally", "arguably", "in today's fast-paced world",
    "in today's fast paced world", "ever-evolving", "ever evolving",
    "navigate the landscape", "in the realm of", "when it comes to",
]

# context-sensitive: flagged, but often legitimate. reported separately.
SOFT_WORDS = ["leverage", "ecosystem", "landscape", "journey", "align", "crucial", "vital", "bespoke"]

BANNED_SHAPES = [
    (re.compile(r"\bit'?s not (just )?(about )?[^.!?\n]{1,40}?,\s*it'?s\b", re.I),
     "not-X-it's-Y construction"),
    (re.compile(r"\bthis is'?n?t (just )?[^.!?\n]{1,40}?\.\s*(it'?s|this is)\b", re.I),
     "not-X-it's-Y construction"),
    (re.compile(r"^[\s>#*\-\d.)]*(?:\*\*[^*\n]{1,30}:?\*\*\s*)?"
                r"(ever wonder(ed)?|what if i told you|have you ever|did you know)\b", re.I | re.M),
     "rhetorical question opener"),
    (re.compile(r"\bhere'?s the (thing|kicker|secret|truth)\b", re.I),
     "setup-colon-reveal cliche"),
    (re.compile(r"\b(the (harsh |hard )?(truth|reality) is|the fact of the matter is)\b", re.I),
     "empty emphasis phrase"),
    (re.compile(r"\b(studies show|research shows|experts agree|a recent study (found|showed))\b", re.I),
     "unsourced authority claim"),
    (re.compile(r"\bit('s| is) worth noting that\b", re.I), "hedge stack"),
    (re.compile(r"\bas (someone|a professional) who has spent\b", re.I), "credentials-first opener"),
    (re.compile(r"^[\s>#*\-\d.)]*(?:\*\*[^*\n]{1,30}:?\*\*\s*)?"
                r"(hey guys|hi everyone|hello everyone|welcome back|what's up guys)\b", re.I | re.M),
     "greeting opener"),
    (re.compile(r"\ba thread\s*[:\U0001F9F5]", re.I), "thread label"),
]

CONTRACTIONS = re.compile(
    r"\b\w+'(s|t|re|ve|ll|d|m)\b", re.I)
SECOND_PERSON = re.compile(r"\b(you|your|you're|youre|yours)\b", re.I)
SENT_SPLIT = re.compile(r"(?<=[.!?])[\s\n]+")
CODE_FENCE = re.compile(r"```.*?```", re.S)
MD_META = re.compile(r"^\s*(#{1,6}\s|\||\*\*(Hook options|Notes|Post / Script|Voice profile))", re.M)


def prose_only(text: str) -> str:
    """Strip code fences, tables, and headings so metrics measure the writing."""
    text = CODE_FENCE.sub(" ", text)
    kept = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or stripped.startswith("|") or stripped.startswith(">"):
            continue
        if re.match(r"^\*\*[^*]+:?\*\*\s*$", stripped):
            continue
        kept.append(stripped)
    return "\n".join(kept)


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def find_punct(text: str):
    hits = []
    for ch, name in BANNED_PUNCT.items():
        for m in re.finditer(re.escape(ch), text):
            hits.append({"type": "punctuation", "detail": name, "line": line_of(text, m.start()),
                         "context": snippet(text, m.start())})
    for m in EN_DASH_PUNCT.finditer(text):
        hits.append({"type": "punctuation", "detail": "en dash used as punctuation",
                     "line": line_of(text, m.start()), "context": snippet(text, m.start())})
    for m in re.finditer(r"(?<=\w);", text):
        hits.append({"type": "punctuation", "detail": "semicolon", "line": line_of(text, m.start()),
                     "context": snippet(text, m.start())})
    return hits


def snippet(text: str, pos: int, width: int = 38) -> str:
    start = max(0, pos - width)
    end = min(len(text), pos + width)
    return text[start:end].replace("\n", " ").strip()


def find_words(text: str, words, kind):
    hits = []
    for word in words:
        pattern = re.compile(r"(?<!\w)" + re.escape(word).replace(r"\ ", r"\s+") + r"(?!\w)", re.I)
        for m in pattern.finditer(text):
            hits.append({"type": kind, "detail": word, "line": line_of(text, m.start()),
                         "context": snippet(text, m.start())})
    return hits


def find_shapes(text: str):
    hits = []
    for pattern, name in BANNED_SHAPES:
        for m in pattern.finditer(text):
            hits.append({"type": "shape", "detail": name, "line": line_of(text, m.start()),
                         "context": snippet(text, m.start())})
    return hits


def metrics(prose: str):
    sentences = [s.strip() for s in SENT_SPLIT.split(prose) if len(s.strip()) > 1]
    lengths = [len(re.findall(r"\b[\w'-]+\b", s)) for s in sentences]
    lengths = [n for n in lengths if n > 0]
    words = re.findall(r"\b[\w'-]+\b", prose)
    word_count = len(words) or 1
    paras = [p for p in prose.split("\n") if p.strip()]
    para_lens = [len(re.findall(r"\b[\w'-]+\b", p)) for p in paras]
    return {
        "words": len(words),
        "sentences": len(lengths),
        "avg_sentence_len": round(statistics.mean(lengths), 1) if lengths else 0,
        "sentence_len_stdev": round(statistics.pstdev(lengths), 1) if len(lengths) > 1 else 0,
        "longest_sentence": max(lengths) if lengths else 0,
        "short_sentence_pct": round(100 * sum(1 for n in lengths if n <= 6) / len(lengths), 1) if lengths else 0,
        "long_sentence_pct": round(100 * sum(1 for n in lengths if n > 28) / len(lengths), 1) if lengths else 0,
        "contractions_per_100w": round(100 * len(CONTRACTIONS.findall(prose)) / word_count, 1),
        "second_person_per_100w": round(100 * len(SECOND_PERSON.findall(prose)) / word_count, 1),
        "para_len_stdev": round(statistics.pstdev(para_lens), 1) if len(para_lens) > 1 else 0,
    }


def warnings_from(m):
    warns = []
    if m["sentences"] >= 6:
        if m["sentence_len_stdev"] < 6:
            warns.append(f"monotone rhythm: sentence length stdev {m['sentence_len_stdev']} (want 6+). "
                         "Break some sentences, let one run long.")
        if m["short_sentence_pct"] < 12:
            warns.append(f"only {m['short_sentence_pct']}% of sentences are 6 words or fewer (want 12%+). "
                         "Add real short sentences.")
        if m["avg_sentence_len"] > 20:
            warns.append(f"average sentence {m['avg_sentence_len']} words (want 12 to 16).")
        if m["long_sentence_pct"] > 12:
            warns.append(f"{m['long_sentence_pct']}% of sentences run past 28 words. Split them.")
    if m["words"] >= 120:
        if m["contractions_per_100w"] < 1.5:
            warns.append(f"contraction rate {m['contractions_per_100w']} per 100 words. Reads written, not spoken.")
        if m["second_person_per_100w"] < 1.5:
            warns.append(f"second-person density {m['second_person_per_100w']} per 100 words. "
                         "Talk to one reader directly.")
        if 0 < m["para_len_stdev"] < 4:
            warns.append("paragraphs are uniform in length. Vary the blocks.")
    return warns


def main():
    ap = argparse.ArgumentParser(description="Check content for AI-slop tells.")
    ap.add_argument("path")
    ap.add_argument("--extra-banned", help="file with one extra banned phrase per line")
    ap.add_argument("--json", action="store_true", help="machine readable output")
    ap.add_argument("--max-report", type=int, default=40)
    args = ap.parse_args()

    path = Path(args.path)
    if not path.is_file():
        print(f"file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    prose = prose_only(text)

    banned = list(BANNED_WORDS)
    if args.extra_banned:
        extra = Path(args.extra_banned)
        if extra.is_file():
            banned += [w.strip() for w in extra.read_text(encoding="utf-8").splitlines() if w.strip()]

    hard = find_punct(text) + find_words(text, banned, "vocabulary") + find_shapes(text)
    soft = find_words(text, SOFT_WORDS, "context-sensitive")
    hard.sort(key=lambda h: h["line"])
    soft.sort(key=lambda h: h["line"])

    m = metrics(prose)
    warns = warnings_from(m)

    if args.json:
        print(json.dumps({"file": str(path), "hard_failures": hard, "soft_flags": soft,
                          "metrics": m, "warnings": warns, "passed": not hard}, indent=2))
        return 1 if hard else 0

    print(f"slop_check: {path.name}")
    print(f"  {m['words']} words, {m['sentences']} sentences, avg {m['avg_sentence_len']}, "
          f"spread {m['sentence_len_stdev']}, contractions {m['contractions_per_100w']}/100w, "
          f"you-density {m['second_person_per_100w']}/100w")

    if hard:
        print(f"\nHARD FAILURES ({len(hard)}):")
        for h in hard[:args.max_report]:
            print(f"  line {h['line']:>4}  [{h['type']}] {h['detail']}")
            print(f"             ...{h['context']}...")
        if len(hard) > args.max_report:
            print(f"  and {len(hard) - args.max_report} more")
    else:
        print("\nNo hard failures.")

    if soft:
        print(f"\nCONTEXT-SENSITIVE ({len(soft)}) - keep if genuinely correct, say why in the notes:")
        for h in soft[:12]:
            print(f"  line {h['line']:>4}  {h['detail']}  ...{h['context']}...")

    if warns:
        print(f"\nWARNINGS ({len(warns)}):")
        for w in warns:
            print(f"  - {w}")

    print("\nRESULT: " + ("FAIL - fix the hard failures and rerun." if hard else
                          ("PASS with warnings." if warns else "PASS.")))
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
