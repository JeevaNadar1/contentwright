# copywright

**A Claude Skill for writing copy that sells and reads like a person wrote it.**

Built by [Jeeva Nadar](https://github.com/) · MIT licensed · Works in Claude.ai, the Claude apps, and Claude Code

Most AI copy fails in one of two directions. It goes loud, generic and adjective-stuffed, the way a landing page did in 2013. Or it goes smooth, balanced, hedged and structurally identical paragraph after paragraph, which is worse, because it feels competent right up until nobody replies.

copywright runs a direct-response spine over a literary finish. Hormozi, Halbert, Schwartz, Ogilvy and Bencivenga decide what the copy says. Rhythm, antithesis and monosyllabic landings decide how it lands. A hard anti-slop pass runs on every deliverable before it reaches you.

The standard it holds itself to: a good human copywriter reading the output should not be able to tell a model wrote it, and should be able to point at the mechanism that makes it work.

---

## What it writes

1. **Outbound.** Cold emails, follow-up sequences, LinkedIn DMs, pitch notes.
2. **Long-form sales.** Sales letters, landing pages, VSL scripts, offer construction.
3. **Content.** Blog posts, newsletters, LinkedIn and X posts, case studies.
4. **Short and sharp.** Subject lines, taglines, ad sets, headlines, CTAs.
5. **Awkward.** Apology letters, price rise notices, outage posts, layoff announcements, cover letters.
6. **Editing.** Existing copy that is too long, too vague, too corporate, or too obviously machine-made.

## What it will not do

1. Invent a statistic, a testimonial, a client name or a result. If a number is needed and missing, it writes `[NEEDS: metric]` and tells you.
2. Guarantee outcomes inside compliance-bound copy.
3. Imitate a named writer's tics. It takes the mechanics, because copying the mannerisms produces parody.
4. Pad to look thorough. If the right answer is 40 words, you get 40 words.

---

## Install

**Claude.ai and the Claude apps:** download `copywright.skill`, open it in a chat, click Save skill.

**Claude Code:**

```bash
git clone https://github.com/<your-username>/copywright.git ~/.claude/skills/copywright
```

**Anything else that reads SKILL.md:** point it at the folder. It is plain markdown, no dependencies, nothing to build.

---

## Use it

Just ask. It triggers on the natural phrasing, not a command syntax:

```
write me a cold email to CFOs at mid-size manufacturers
landing page for a bookkeeping service, cold traffic
10 subject lines for a re-engagement send
punch this up, it reads like AI
draft the price increase email, we are going up 12%
rewrite my about page so it sounds like me
```

First it classifies the job: format, temperature (cold, warm, hot), the one action, and the shortest length that still does the job. Then it asks five to ten questions in a single batch, each with a default, so you can reply "defaults" and move. Say **"just write it"** and it drafts immediately, listing the three assumptions it made at the top so you correct the premise instead of the prose.

---

## How it works

1. **Classify.** Format, temperature, job to be done, length ceiling. Loads only the reference files that job needs.
2. **Intake.** Five to ten batched questions with defaults. Never serial, never asking what the brief already answered.
3. **Reader Contract.** One specific reader, the belief they hold now, the belief they need, one action, one reason to believe, and the cost of doing nothing in their terms. Fuzzy here means fuzzy copy, so it gets fixed here.
4. **Doctrine.** Twelve laws that settle most drafting decisions. Specificity over adjectives. Demonstrations over claims. One person, one idea, one ask.
5. **Pipeline.** Mine the real material, pick the angle in plain language, choose the lead type against awareness level, draft hot at 130% of target, impose structure, cut 25 to 35%, fix cadence out loud, place proof beside the claim it supports, audit.
6. **Specificity engine.** Eight mechanical drills that upgrade weak lines. "Most clients" becomes "9 of the last 11". "Quickly" becomes "before your next payroll run". "Improved compliance posture" becomes "an auditor asks for the log and you send it in four minutes".
7. **Cadence pass.** Sentence lengths varied hard. Endings landing on short hard words. One turn where the argument pivots. One single-line paragraph, used once.
8. **Anti-slop enforcement.** No stock openers, no LLM vocabulary, no "not just X, it's Y", no colon-reveal titles, no tricolon addiction, no uniform paragraph blocks, no hedge stacking, no summary paragraph before the CTA, no em dash tic, no invented proof.
9. **Texture injection.** One oddly specific detail that could only come from real experience. One admitted cost or trade-off. One line in the reader's own vocabulary. One deliberate rhythm break. One line carrying an actual opinion.
10. **Self-audit.** Ten scores out of ten. Anything at 7 or below gets fixed before delivery, not shipped with a caveat.

---

## What comes back

1. The copy, clean and ready to paste. No commentary inside it, no placeholder brackets except where a real fact is genuinely missing.
2. Two or three alternate hooks or subject lines underneath, labelled by angle (curiosity, proof, cost-of-inaction), so there is something to test.
3. Three specific refinement levers at the end. Harder CTA, longer proof section, different awareness level. Not a generic offer to help.

Anything over roughly 400 words, or anything you will publish or edit elsewhere, arrives as a `.md` file. Short copy stays inline where you can read it at a glance.

---

## What it looks like in practice

Before, the version most tools produce:

> Our innovative platform leverages cutting-edge automation to streamline your month-end close, empowering finance teams to unlock new levels of efficiency and focus on what truly matters.

After:

> Your close takes nine days. Six of them are one person matching invoices to a bank statement, by hand, on a Sunday.
>
> We read every invoice twice before a human sees it. Last month that pulled the close to two days for 9 of our last 11 clients.
>
> Send me one month of statements. I will run them and send back the exceptions by Friday. If the list is not shorter than yours, you owe nothing.

Same product. One of them names a mechanism, puts proof next to the claim, and makes the ask a physical action with a date on it.

---

## Layout

```
copywright/
├── SKILL.md                    classification, intake, doctrine, pipeline, audit
└── references/
    ├── frameworks.md           awareness and sophistication levels, lead types,
    │                           hook mechanics, value equation, proof stacks, CTAs
    ├── formats.md              per-format playbooks with structure, target lengths
    │                           and worked examples
    ├── voices.md               the influence bench: Hormozi, Halbert, Schwartz,
    │                           Ogilvy, Sugarman, Bencivenga, Caples, plus the
    │                           literary side
    └── anti-slop.md            full banned list, structural tells, humanizing
                                drills, rewrite exercises
```

Progressive disclosure. SKILL.md stays lean and the references load only when the job in front of it needs them, so a three-line subject line request does not drag in the sales-letter playbook.

---

## Pairs with

1. **contentwright** for organic feed content: YouTube scripts, LinkedIn posts, X threads, newsletters, weekly batches and calendars.
2. **instagram-carousel** for carousels with a locked visual style.

copywright owns anything sold directly. Feed content and carousels belong to the other two, and keeping the boundary clean is what stops all three from turning into the same generic writer.

---

## Tuning it

1. Add brand vocabulary and banned claims to your intake answers once, and it carries them for the rest of the conversation.
2. Feed it two or three samples of your real writing when you want your own voice. It matches habits, not topics.
3. Edit `references/anti-slop.md` to add words you personally hate. The list is meant to grow.

---

## Credits

Written and maintained by **Jeeva Nadar**.

The doctrine leans on the people who worked this out long before any of it was automated: Gary Halbert, Eugene Schwartz, David Ogilvy, Gary Bencivenga, Joseph Sugarman, John Caples and Alex Hormozi, with the cadence layer borrowed from Shakespeare, Hemingway, Didion and Vonnegut.

## License

MIT. Copyright (c) 2026 Jeeva Nadar. Use it, fork it, sell what you write with it.
