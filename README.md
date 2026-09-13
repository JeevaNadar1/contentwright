# contentwright

A Claude Skill for writing organic, platform-native content that does not read like AI wrote it.

One post or fifty. A single LinkedIn draft, a week of posts, ten full YouTube scripts, a month of ideas mapped to pillars. The output scale follows what you asked for, the voice follows a stored profile, and every file goes through a mechanical slop check before it is handed back.

## What it does

1. **Scales to the ask.** "A post about pricing" gives you one post with three hooks. "10 video ideas with scripts" gives you ten full scripts, each with its own cold open, beat map, titles, thumbnail text and description.
2. **Keeps your voice.** A reusable voice profile built from your own samples, so you stop re-explaining how you write. Personal and company profiles stay separate.
3. **Asks before it writes.** Five to ten batched questions with defaults, gated on audience, the one idea, and the desired action. Say "just write it" to skip straight to a draft with assumptions listed.
4. **Kills the tells.** No em dashes. No "delve", no "it's not X, it's Y", no rhetorical question openers, no summary close. Spoken second-person English, uneven sentence rhythm, concrete over abstract.
5. **Checks its own work.** `slop_check.py` hard-fails on banned punctuation, banned vocabulary and banned sentence shapes, then reports rhythm, contraction rate and second-person density.
6. **Repurposes without copy-paste.** One idea rewritten for each channel rather than trimmed down from the longest version.

Covers LinkedIn, YouTube long form, Shorts and Reels, X posts and threads, and newsletters.

## Install

**Claude.ai and the Claude apps:** download `contentwright.skill`, open it in the chat, and click Save skill.

**Claude Code:** clone into your skills directory.

```bash
git clone https://github.com/<your-username>/contentwright.git ~/.claude/skills/contentwright
```

**Anything else that reads SKILL.md:** point it at the folder. The skill is plain markdown plus two stdlib-friendly Python scripts.

## Use

Just ask. The skill triggers on requests like:

```
write me a LinkedIn post about why we killed our best feature
give me a week of content, LinkedIn and X
10 video ideas with full scripts for a channel about Indian tax filing
turn this blog post into a thread and a Short
make this post sound like me, not like ChatGPT
```

First run, it asks for a voice profile. Give it five to ten of your own posts. That single step does more for output quality than every other setting combined.

## Scripts

```bash
# hard-fail slop check, exits 1 on failure
python scripts/slop_check.py batch.md
python scripts/slop_check.py batch.md --extra-banned my_banned_words.txt
python scripts/slop_check.py batch.md --json

# turn a batch file into an xlsx content calendar
python scripts/calendar_export.py batch.md calendar.xlsx
```

`slop_check.py` is stdlib only. `calendar_export.py` needs `openpyxl`.

## Layout

```
contentwright/
├── SKILL.md                        pipeline, scale detection, delivery format
├── references/
│   ├── voice-profile.md            intake questions and the profile template
│   ├── anti-slop.md                banned words, banned shapes, rewrite examples
│   ├── platform-formats.md         structures and length targets per platform
│   └── hook-bank.md                openings that work, openings that do not
├── scripts/
│   ├── slop_check.py               mechanical slop detector
│   └── calendar_export.py          batch markdown to xlsx calendar
└── examples/
    └── sample-output.md            what a finished batch looks like
```

Progressive disclosure: SKILL.md stays lean and the references load only when the relevant step runs.

## Not in scope

Instagram carousels and direct-response sales assets are handled by separate skills. Cold email, ads, landing pages and sales letters are a different job with different rules, and mixing them into a feed-content skill makes both worse.

## Tuning it

1. Add your own banned words to a text file and pass it with `--extra-banned`.
2. Edit `references/anti-slop.md` to change what counts as a hard failure in judgement terms, and `scripts/slop_check.py` to change what the checker enforces mechanically.
3. Adjust length targets in `references/platform-formats.md` if your audience reads longer.

## License

MIT. Use it, fork it, sell what you make with it.
