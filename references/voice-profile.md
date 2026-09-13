# Voice profile

A voice profile is the difference between content that sounds like the user and content that sounds like a model imitating a LinkedIn influencer. Fill it once, reuse it forever, update it when the user says "that is not how I talk".

Profiles are per identity. A person and their company are two profiles. Never blend them in one batch.

## The intake

Ask these in one batched message with the defaults shown. Eight questions, not eighty. If the user answers only half, fill the rest from their samples and mark those lines "inferred".

1. **Who is this for?** The reader in one sentence, with their job, their stage, and the thing keeping them stuck. Default: the audience visible in their existing posts.
2. **What do you want to be known for?** Three to five topics you would defend in public. These become the content pillars.
3. **What is your actual position?** The thing you believe that most people in your space do not. Content without a position is a summary, and summaries get scrolled.
4. **How do you talk?** Blunt, warm, dry, funny, technical, teacherly. Pick two. Default: blunt and dry.
5. **What proof can you use?** Numbers, client work, failures, screenshots, years in the trade, things you built. List the ones you are allowed to publish.
6. **What is off limits?** Clients, employers, family, revenue figures, politics, anything under NDA.
7. **Words you never use.** Both slop words and personal dislikes. Default bans are in `anti-slop.md`, this adds to them.
8. **Five to ten samples.** Their own posts, scripts, voice notes, even Slack messages. This is worth more than questions one to seven combined. If they have nothing written, ask them to answer question three out loud in two minutes and paste the transcript.

Also ask for one piece of content they think is slop. A negative reference is as useful as a positive one, because it names the exact register to avoid.

## Reading the samples

Extract and record these, with evidence from the samples rather than adjectives:

1. Average sentence length and how wide the spread is.
2. Opening move. Do they open with a story, a claim, a number, a scene?
3. Paragraph size. One line, two, three.
4. Contractions, slang, profanity. Present or not.
5. Signature constructions they repeat.
6. How they handle the ending. Question, callback, flat stop, CTA.
7. Vocabulary level and any trade jargon they use without explaining.
8. What they never do. No emoji, no hashtags, no lists, no self-deprecation.

## The profile block

Write the finished profile in this shape and hand it back to the user to save. Keep it under one page so it can be pasted into any conversation.

```markdown
# Voice profile: <name>

Identity: <personal | company | client>
Audience: <one sentence>
Position: <the belief that drives everything>
Pillars: <3 to 5>

## Register
Tone: <two words>
Sentence length: avg <n> words, spread <narrow | wide>
Paragraphs: <1 to 2 lines>
Contractions: <yes | no>
Person: second person, present tense
Emoji: <none | sparing>
Hashtags: <none | 3 max>

## Moves that are mine
- <signature construction, with an example line>
- <how openings usually work>
- <how endings usually work>

## Proof I can cite
- <numbers, stories, credentials that are publishable>

## Never
- <off limits topics>
- <banned words beyond the standard list>
- <structures they hate, e.g. listicles>

## Samples
<2 or 3 short excerpts, verbatim, as calibration>
```

## Keeping it honest

When the user corrects a draft, the correction is a profile update, not a one-off fix. Add the rule to the profile block, carry it for the rest of the conversation, and tell the user which line changed so their saved copy stays current. A correction made twice means the profile was never updated the first time.
