---
name: contentwright
description: Write organic, platform-native content that sounds like a human talking, not an AI writing. Use whenever the user wants content for a feed or channel, meaning YouTube long-form scripts, Shorts and Reels scripts, LinkedIn posts, X posts and threads, newsletters. Handles one post, a week of posts, ten video scripts, a month of ideas, a content calendar, or a batch repurposed from one idea. Triggers on "write me a LinkedIn post", "script for a video on X", "give me a week of content", "10 video ideas with scripts", "turn this into a thread", "make my posts sound less like AI", "rewrite this so it sounds like me", "content plan for next month", and on any request to plan, draft, batch, repurpose or de-slop published content. Also use when the user pastes their own draft and wants it sharper, shorter, more human or more native to the platform. Do NOT use for Instagram carousels (use instagram-carousel) or direct-response sales assets like cold email, ads, landing pages and sales letters (use copywright).
license: MIT
metadata:
  version: 1.0.0
  display_name: Contentwright
---

# Contentwright

Organic content that reads like one person talking to one person. The output scale follows the input. The voice follows a stored profile, not a guess.

## What this owns, what it hands off

Owns: anything published to a feed or channel on a recurring basis. YouTube, LinkedIn, X, newsletter, Shorts, Reels scripts, plus the idea banks and calendars behind them.

Hands off: Instagram carousels go to `instagram-carousel`. Cold email, ads, landing pages, sales letters and anything sold directly go to `copywright`. A LinkedIn post that promotes a launch stays here, borrowing the hook discipline in `references/hook-bank.md` rather than switching skills.

## Pipeline

Run these in order. Do not skip step 1 or step 5.

### 1. Load the voice

Look for a filled voice profile in this order: pasted in the conversation, in project files or memory, in a file the user points at. If none exists, run the voice intake in `references/voice-profile.md` once, then echo the finished profile block back so the user can save it and reuse it forever. Never invent a voice. A skipped profile is the single biggest cause of generic output.

If the user names a profile ("use the company one"), load that one. Profiles are per identity, not per request: a personal profile and a company profile sound different and must not be blended.

### 2. Gate on missing context

Before writing anything substantial, ask 5 to 10 batched questions, each with a stated default, in one message. Never drip-feed questions one at a time.

Three gates are hard. Do not draft until each is answered or defaulted explicitly:

1. **Audience.** Who exactly reads this, and what do they already believe?
2. **The one thing.** What single idea should survive if they forget the rest?
3. **Desired action.** What do they do at the end - comment, subscribe, reply, book, nothing?

The rest scale with the job: platform and count, publish window, tone dial, proof the user can cite (numbers, client stories, personal receipts), what is off limits, whether there is a product or launch attached, reference posts that landed well, and links or assets to include.

Fast path: if the user says "just write it", skip the questions, draft from the profile plus assumptions, and list the assumptions in a short block at the top of the file. They correct from a draft, which is faster than answering ten questions.

### 3. Detect scale from the ask

| What they say | What you produce |
|---|---|
| "a LinkedIn post about X" | 1 post, plus 2 alternate hooks |
| "a week of LinkedIn" | 5 posts, varied formats, one idea thread running through them |
| "a month of content" | 16 to 20 pieces mapped to pillars, plus a calendar |
| "script for a video on X" | 1 full script: cold open, beat map, CTA, title options, thumbnail text, description, chapters |
| "10 video ideas with scripts" | 10 full scripts, each with its own hook, no repeated structure |
| "ideas only" / "what should I post" | ranked idea bank, 15 to 25 lines, no drafts |
| "turn this into a thread" / "repurpose this" | run the repurposing engine below |
| "make this sound like me" | rewrite in profile voice, then a short diff note on what changed and why |

When the ask is ambiguous between two rows, produce the smaller one and offer the larger. Nobody is annoyed by a fast small draft. Everybody is annoyed by twenty pieces in the wrong voice.

### 4. Generate angles before drafting

Draft the idea list first, show it only if the batch is five pieces or more, then write. For a batch, every piece needs a different job. Rotate across: personal story with a lesson, contrarian take, teardown of something public, tactical how-to, numbers and receipts, myth correction, behind the scenes, question that earns replies. Two consecutive pieces with the same shape is the fastest way a feed starts looking automated.

Anchor to pillars. If the user has none, propose three or four from their profile and confirm in the same message as the draft.

### 5. Write, then strip the slop

Draft using the platform structures in `references/platform-formats.md` and the openings in `references/hook-bank.md`. Load only the sections you need.

Then read `references/anti-slop.md` and do a full pass. This is not optional polish. It is where the output stops sounding like a model.

The short version, expanded in that file:

1. No em dash. No en dash used as punctuation. Commas, full stops, and shorter sentences instead.
2. Talk to one person as "you". Second person, present tense, contractions on.
3. No bookish register. If nobody would say it out loud, cut it.
4. Vary sentence length hard. Three, four, then a long one that earns its length. Monotone rhythm is the tell.
5. Concrete over abstract. A number, a name, a time, a place beats an adjective every time.
6. Ban the tell-tale vocabulary and the tell-tale shapes, including "it's not X, it's Y", the rule-of-three padding, the rhetorical question opener, and the summary paragraph that repeats what was just said.

### 6. Run the checker

```bash
python scripts/slop_check.py <output-file.md>
```

It hard-fails on banned punctuation and banned phrasing, and reports rhythm, sentence length spread, contraction rate and second-person density. Fix what it flags, rerun, and only present the file once it exits clean. Report the final scores in one line when handing over. If a flagged phrase is genuinely correct in context, keep it and say why rather than mangling the sentence.

### 7. Deliver

One `.md` file per batch, written to the output directory and presented for download. Structure:

```
# <Batch name> - <date range>
Voice profile: <name>  |  Pieces: <n>  |  Slop check: pass

## 1. <Platform> - <slot, e.g. Mon 14 Apr> - <format type>
**Hook options:** three, best first
**Post / Script:**
<body, ready to paste, no commentary inside it>
**Notes:** length, CTA, assets needed, why this angle
```

For a week or more, also offer the calendar:

```bash
python scripts/calendar_export.py <output-file.md> <calendar.xlsx>
```

Never mix commentary into the body text. The user copies the body straight out. Anything they have to delete first is a defect.

## Repurposing engine

One idea, several homes, no copy-paste. Each version must be rewritten from the idea, not trimmed from the longest one. Trimmed content reads like leftovers.

1. YouTube script: the full argument, with the story intact and the tangent kept.
2. LinkedIn post: one beat of the argument, the one with the strongest personal receipt.
3. X thread: the argument stripped to claims, one claim per line.
4. Short or Reel: the single most surprising sentence, expanded to 45 seconds.
5. Newsletter: the argument plus the part that was cut from the video for time.

## Edge cases

**No profile and no time.** Draft anyway, mark it "voice unverified", and ask for one reference post afterwards. One real sample beats ten adjectives.

**User pastes their own draft.** Keep their sentences wherever they already sound human. Rewriting a working line to prove effort is a downgrade. Flag what changed.

**Claims that need proof.** Do not invent statistics, client names, revenue figures or outcomes. If a slot needs a number, leave `[your number here]` and say so in the notes. Fabricated receipts are the one failure the user cannot fix in editing.

**Sensitive or regulated topics.** Medical, legal, financial advice: keep it descriptive, avoid promises, and say plainly when a claim needs a professional check.

**Very long batches.** Above 20 pieces, write in chunks of 10, run the checker on each chunk, and keep a running idea list so angles do not repeat across chunks.

## Reference files

1. `references/voice-profile.md` - the intake and the profile template. Read at step 1.
2. `references/anti-slop.md` - banned vocabulary, banned shapes, rewrite examples. Read at step 5, every time.
3. `references/platform-formats.md` - structures for YouTube, LinkedIn, X, Shorts, newsletter, with length targets. Read the sections in play.
4. `references/hook-bank.md` - opening lines by content type, plus the endings that earn a reply. Read when drafting hooks.
