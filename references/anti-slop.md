# Anti-slop

Read this at step 5, every time, on every piece. The rules below are what separate writing from generated text. `scripts/slop_check.py` enforces the mechanical half. The judgement half is here.

## 1. Punctuation

1. No em dash. Ever. Not in scripts, not in posts, not in titles.
2. No en dash used as punctuation between words. A hyphen in a compound word is fine.
3. Replace the dash with what it was hiding: a full stop, a comma, or a rewritten sentence. Most em dashes exist because two ideas were jammed together without deciding which one mattered.
4. No semicolons in social copy. Nobody speaks a semicolon.
5. No ellipsis for suspense. One per batch at most, and only where a real pause exists.
6. Straight quotes, not curly, so nothing breaks when the user pastes it.

Before: The tool is fast, cheap, and simple, which is exactly why it works.
After: The tool is fast and cheap. That is the whole reason it works.

## 2. Register

Write the way a competent person talks when they are explaining something to one other person and slightly impatient about it.

1. Second person. "You", not "one" or "people" or "businesses today".
2. Present tense wherever the past tense is not load bearing.
3. Contractions on. "You're", "it's", "doesn't". Written-out forms read like a press release.
4. Short paragraphs. One or two lines on LinkedIn and X. Spoken lines in scripts.
5. If a sentence would sound strange said out loud, it is wrong. Read it out loud in your head before keeping it.

Before: It is essential that organisations reconsider their approach to hiring.
After: You are hiring wrong. Here is the part nobody checks.

## 3. Banned vocabulary

Cut on sight. Rewrite the sentence rather than swapping a synonym, because the synonym is usually the same idea wearing a hat.

delve, leverage (as a verb), unlock, elevate, harness, robust, seamless, streamline, empower, foster, navigate the landscape, in today's fast-paced world, in the ever-evolving world of, game-changer, revolutionary, cutting-edge, state of the art, transformative, journey (for anything that is not travel), testament to, tapestry, beacon, realm, landscape (figurative), ecosystem (unless literal or technical), synergy, holistic, curated, bespoke (unless literal), best-in-class, world-class, next-level, paradigm shift, deep dive, let's dive in, buckle up, spoiler alert, plot twist, the reality is, the truth is, at the end of the day, needless to say, it goes without saying, furthermore, moreover, additionally, in conclusion, to summarise, crucial, pivotal, vital, myriad, plethora, boasts, hurdle, resonate, align (figurative), unpack, lean into, double down (unless about actual risk), supercharge, turbocharge, 10x (as filler), insane, wild, absolutely, literally (as intensifier), truly, simply put, essentially, fundamentally, arguably.

Emoji bullets, the sparkle emoji, the rocket emoji, and hashtag walls are part of the same problem.

## 4. Banned shapes

Vocabulary is the easy tell. These structures are the real one.

1. **Not X, it's Y.** "It's not about tools, it's about mindset." Delete. Say the thing you actually mean.
2. **Rule of three padding.** Three adjectives, three clauses, three parallel sentences in a row. One is usually true, the other two are rhythm filler.
3. **Rhetorical question opener.** "Ever wondered why...", "What if I told you...". The reader already knows they are being sold to.
4. **The setup-colon-reveal.** "Here's the thing: most people get this wrong."
5. **The summary close.** A final paragraph restating what the post just said. End on the sharpest line instead and stop.
6. **The hedge stack.** "It's worth noting that it could arguably be said that". Say it or cut it.
7. **Balanced both-sides ending.** Taking a position for eight lines then dissolving it in the ninth. Hold the position.
8. **Fake specificity.** "A recent study found", "experts agree", "studies show". Name the source or drop the claim.
9. **Corporate passive.** "Mistakes were made", "value was delivered". Name who did what.
10. **Uniform paragraphs.** Four blocks of three lines each is a visual tell before a single word is read.

## 5. Rhythm

The single strongest signal that a human wrote something is uneven sentence length.

Target an average around 12 to 16 words with a standard deviation above 6. That means real short sentences. Four words. Then one that runs long enough to carry a full idea across a couple of clauses and land somewhere the reader did not expect.

1. Land hard sentences on one-syllable words. "It broke." beats "It was unsuccessful."
2. Never let three sentences in a row share a length or a shape.
3. Use a fragment where speech would use one. Sparingly.
4. Read the first three lines and the last line out loud. Those four lines do most of the work.

## 6. Specificity

Every abstraction should be swapped for a thing you could photograph.

Before: We improved efficiency significantly across the team.
After: Two people stopped spending Friday afternoons on the report. That is 400 hours a year.

If the user has not supplied a number, do not invent one. Write `[your number here]` and flag it in the notes. An honest gap is fixable. A fabricated figure published under their name is not.

## 7. The pass

Work through in this order. Each pass is fast because it looks for one thing.

1. Punctuation sweep. Dashes, semicolons, ellipses, quotes.
2. Vocabulary sweep against the banned list.
3. Shape sweep against the banned structures.
4. Read out loud. Anything you stumble on gets rewritten.
5. Rhythm check. Vary lengths until the spread is real.
6. Cut 15 percent. Not by deleting sentences, by deleting words inside them. The first draft is always padded.
7. Run `scripts/slop_check.py` and fix what it catches.

## 8. When a banned word is correct

Rules exist to kill defaults, not to mangle accurate sentences. "Leverage" in a finance post about debt is the right word. "Ecosystem" in an ecology script is the right word. Keep it, and say in the handover notes why it stayed. The checker flags, it does not decide.
