---
name: "salesforce-cert-mock-exam"
description: Build hard, use-case-based mock exams and quizzes for any Salesforce certification the user names (Administrator, Advanced Administrator, Platform App Builder, Platform Developer, Sales/Service Cloud Consultant, Agentforce Specialist, Data Cloud, Marketing Cloud, architect exams and others), grounded in that exam's official exam guide, its Trailhead preparation trail or trailmix, and Salesforce Help. Each answer explains why the correct option is right, why every other option is wrong, and links the Trailhead unit or Help article to review. Use whenever the user asks for a Salesforce mock exam, practice test, practice questions, exam-style quiz, flashcards or a timed exam with a countdown for a Salesforce certification or exam topic, even if they just say "quiz me on Platform App Builder" or "another mock exam". For the Salesforce Certified Slack Administrator exam, use slack-admin-mock-exam instead.
---

# Salesforce Certification Mock Exam Builder

Produce exam-realistic practice questions for whichever Salesforce certification the user names. The right answer should never be obvious: every option should look plausible to someone who has only skimmed the material, and only someone who knows the precise rule (which feature, which setting, which limit, which order of execution) gets it right.

If the user hasn't named a certification and the conversation doesn't make it clear, ask which one before doing anything else.

## 1. Look up the exam you are simulating (every run)

Exam details change with releases, so never rely on memory for them. At the start of each run, find the current official exam guide for the named certification and capture:

- Exam name and current version or release
- Number of scored questions, time limit and passing score
- Exam outline: each domain (section) and its weighting %
- The official preparation trail or trailmix

How to find them is in `references/retrieval.md`. If an earlier search in this conversation already found the guide, reuse it.

If the guide can't be found, tell the user plainly, use whatever official details you did find, and say which details are unconfirmed. Don't invent weightings or a pass mark.

**Question count.** Default to a full exam matching the real scored-question count, split across domains by weighting (round, then adjust so the total matches). If the user asks for a shorter quiz, scale proportionally or focus on the domain or topic they name.

## 2. Gather source material

Use the retrieval routes in `references/retrieval.md`. Gather only what the requested scope needs: for a full exam, cover every domain in the outline; for a topic quiz, just that topic's units and Help articles. Reuse material already in the conversation rather than searching again.

As you gather, keep a running note per fact of where it came from (module slug + unit slug, Help article URL or title). The review links in section 4 come from this note, so record them as you go rather than reconstructing them later.

## 3. Write use-case questions that are genuinely hard

Every question must be traceable to something in the sources. Never invent limits, numbers, edition entitlements or permission names. If you are unsure of a fact, drop the question rather than guess.

### Why use cases matter

The real Salesforce exams are built from business use cases, not fact recall. A learner who scored around 90% on short "which role does X?" practice questions scored around 70% on the real exam, because the real questions bury the deciding rule inside a realistic scenario with competing requirements. Practice that only tests recall gives false confidence. Write every question so the learner has to read a situation, decide which details matter, and apply the rule.

### Shape of every question

- **Vary the stem length at random.** Real exams mix short and long questions, so a set should not settle into one rhythm. Let each question's length follow what it needs, and mix roughly: about 25% short (one or two sentences, around 15-40 words, still applied to a situation, e.g. "A Pro workspace wants X without Y. What should the admin do?"), about 40% medium (around 40-80 words), about 25% long (around 80-130 words, with more context and irrelevant detail), and about 10% very long (around 150-230 words; at least one per 10 questions, at a random position). Shuffle the lengths through the set so long and short questions don't cluster, and never let length hint at difficulty or at the answer. Most stems open with a fictional company (Universal Containers, Cloud Kicks, Northern Trail Outfitters, Ursa Major Solar and similar), its edition or plan, who is involved, and what they need; short stems can compress this to a single clause. Pure recall stems ("Which feature does X?") are capped at 10% of a set.
- **Very long questions read like a real case study.** Use them for merges and acquisitions, migrations, rollouts, security incidents and multi-team projects. Give the background (companies, plans or editions, team sizes, tools already in use), name two or three stakeholders who each want something, add three or four irrelevant details, and bury the deciding requirements in the middle of the story, not at the end. Close with one clear question. The options stay short and parallel; the length is in the stem only.
- **Requirements or constraints in most questions.** For example: a business need plus a limit such as least privilege, no code, fewest steps, lowest maintenance, minimal licence cost, an existing tool that must be kept, or a data-volume or timing constraint. The constraint is usually what decides between two otherwise valid options.
- **Irrelevant details in medium and long questions.** Include one or two realistic facts that don't change the answer (team size, a past project, a feature already in use elsewhere), so the learner practises filtering, as on the real exam. Never let an irrelevant detail make a second option correct.
- **Ask for a judgement, not a definition.** Prefer: "What should the administrator recommend?", "What is the best solution?", "What should the consultant do first?", "Which approach meets the requirements with the least effort?", "What will happen when...?", "Why is ... not working?". Use plain recall ("Which feature does X?") only for the small allowance above.
- **Two plausible options.** At least two options should solve the stated business need; only one also satisfies every constraint. The explanation must name the constraint that eliminates the near-miss.
- **Troubleshooting and consequence items.** In each full exam, make roughly 15-20% "something isn't working, why?" or "what happens to existing records/users/data after this change?" questions.

### Multi-requirement questions (mix them in at random)

Real exams sometimes list several requirements, and only one option meets every one of them. Use this format for roughly 25-40% of a set, placed at random. It should appear unpredictably, not in every question, not on a fixed rotation (such as every third question), and not grouped together. Vary how the requirements are presented, so the format itself doesn't become a pattern:

- **A numbered list** after the scenario ("The solution must:" with 2-4 numbered requirements, one per line; the page keeps line breaks). Use this for some of the multi-requirement questions, not all.
- **Inline requirements** woven into the prose ("...must be live by Friday, can't involve code, and mustn't change access for anyone else.").
- **Implied constraints** the learner has to spot in the story ("The company has no developers" or "Legal has asked that nothing else changes").

The other questions should rely on a single deciding constraint, a troubleshooting angle, or a consequence ("what happens to existing records?").

For every multi-requirement question, whichever format is used:

- **Keep each requirement specific and testable**: a business outcome, a constraint (no code, least privilege, available on the current edition), or a scope limit ("without changing retention for anyone else").
- **Every wrong option meets most requirements but fails at least one.** Build options by starting from the correct answer and breaking one requirement at a time. Avoid options that fail everything; they're too easy to eliminate.
- **Options can be short combinations** ("Feature X with setting Y, plus Z") when the answer needs more than one piece. Keep them parallel in structure, so each differs from the correct one in one element.
- **Explanations map to the requirements.** In `why`, confirm how the answer meets each one; in each `wrong` line, name the requirement it fails ("Fails requirement 2: ..." for numbered lists, or "Fails the no-code requirement" for inline or implied ones).

Example stem:
> Cloud Kicks (Pro) is bringing in a freelance designer for three months.
> The solution must:
> 1. Give access to #design and #brand only
> 2. Keep the rest of the workspace hidden from them
> 3. End their access automatically when the contract ends
>
> What should the admin do?

Correct: multi-channel guest with an expiration date. Near-misses: a single-channel guest with an expiry (fails 1), a multi-channel guest with no expiry (fails 3), a full member removed later (fails 2 and 3).

### Example: recall style vs use-case style

Recall style (avoid):
> Which feature lets an admin control field visibility by profile?

Use-case style (write this):
> Cloud Kicks has 40 sales reps and 6 sales managers, all on the same profile. The company recently rolled out Dynamic Forms on the Opportunity page. Managers must be able to edit the Discount field on opportunities, but reps must only see it, and the admin wants a solution that won't need a new profile each time a manager is hired. What should the administrator do?
> A. Create a permission set granting edit access to Discount and assign it to managers *(correct)*
> B. Use Dynamic Forms to show the field as read-only to reps
> C. Create a separate profile for managers with edit access
> D. Add a validation rule that blocks reps from changing Discount

Here B is a near-miss (Dynamic Forms controls display, not field-level security), C meets the need but breaks the "no new profile" constraint, and D works but is a workaround, not access control. The team size and the Dynamic Forms rollout are deliberate irrelevant details.

### Distractors and options

- **Distractors from adjacent truths.** Wrong options should be real Salesforce features that are correct in a neighbouring situation: a sharing tool that opens access when the requirement is to restrict it; a declarative tool that can't do the specific thing asked; the right feature on the wrong object or edition; a valid approach that breaks one stated constraint. Avoid joke options and "none of the above".
- **Target the confusable pairs for that exam.** Examples: profiles vs permission sets vs permission set groups; OWD vs role hierarchy vs sharing rules vs manual sharing; lookup vs master-detail; validation rules vs Flow vs Apex triggers; record-triggered before-save vs after-save Flow; formula vs roll-up summary; page layouts vs record types vs Dynamic Forms; change sets vs Salesforce CLI/DevOps Center; reports vs report types vs dashboards. Pick the ones that matter for the exam in hand.
- **"Choose 2" / "Choose 3" questions.** The real exams have these, but the exam page takes one answer per question. Rewrite each as a single-answer question that still tests the same knowledge: ask for the one best option, or ask which option is *not* valid, or make the scenario specific enough that only one option fits. Never combine options ("A and C").
- **Keep options parallel.** Similar length and grammar, so the longest or most detailed option isn't a giveaway. Rotate the correct letter evenly across A-D.
- **One defensible answer.** Re-read each question as a sceptical examiner. If a second option satisfies every requirement and constraint in the stem, add or sharpen a constraint, or rewrite.

### Explanations for use-case questions

In `why`, name the rule and the constraint it satisfies ("Permission sets add access without a new profile, which meets the 'no new profile per hire' requirement."). In each `wrong` line, say what that option is actually right for and which part of the scenario it fails ("C: a separate profile works, but breaks the requirement to avoid a new profile per hire.").

### Quality check before building

Before running the builder, check the whole set:

1. Stem lengths are mixed (roughly 25% short, 40% medium, 25% long, 10% very long, with at least one very long question per 10) and shuffled, with no long or short clusters; at most 10% are pure recall.
2. Multi-requirement questions make up roughly 25-40% of the set, appear at random positions (not every question, not on a fixed rotation), and use a mix of numbered, inline and implied formats; each wrong option in them fails at least one requirement.
3. Every scenario question has a near-miss option, and its `wrong` line names the deciding constraint.
4. Irrelevant details never make a second option correct.
5. Every fact is traceable to the gathered sources.
6. Correct letters are evenly spread.

Fix any question that fails before building.

## 4. Deliver it

Always deliver questions as the exam page built from this skill's template, never as the in-chat quiz card: the quiz card shows explanations as one plain-text paragraph, so bullet points and tappable review links are impossible there. There are two modes:

- **Practice mode (default)**: no countdown. After each answer the page locks the question, marks the right and wrong options, and shows the explanation underneath as bullet points with tappable review links. Use this for any quiz unless the user asks for a timer.
- **Timed mode**: when the user asks for a countdown, timer, timed exam or real exam conditions. See section 4b.

For each question, write:

7. **Why the answer is right** (`why`): one or two sentences naming the exact rule (who, which plan, which level).
8. **Why each other option is wrong** (`wrong`): one line per wrong option, in the form "B (option text): reason". Say what the option is actually correct for, so the learner learns the neighbouring rule too. Cover every wrong option; the builder rejects a question that misses one.
9. **Review links** (`review`): `{title, url}` for the sources the question came from. The page renders them as tappable titled links.
   - Trailhead unit: `https://trailhead.salesforce.com/content/learn/modules/<module-slug>/<unit-slug>`.
   - Help or documentation articles: use the URL as it appears in the sources or search results.
   - Never invent a slug or URL. If the exact unit is uncertain, link the module. If no URL was found, give the title only, and the page will tell the learner to search for it.

Build steps (both modes):
10. Write `exam.json` in the shape documented at the top of `scripts/build_timed_exam.py`. Set `"mode": "practice"` for practice mode, and give the exam a unique `id` (cert + date + letter) so saved progress from an old quiz isn't picked up. For practice mode, set `timeLimitMinutes` to a suggested pace (real minutes × questions ÷ real question count, rounded up); the page shows it as a suggestion only.
11. Build: `python3 <skill-dir>/scripts/build_timed_exam.py exam.json /mnt/user-data/outputs/<cert>-<practice|timed>-<n>.html`. It validates the data and prints the spread of correct letters; if one letter dominates, rotate options and rebuild.
12. Publish the file with the Artifact tool (favicon "📝" for practice, "⏱️" for timed; title = quiz name). If the Artifact tool isn't available, present the file with present_files instead.
13. In the reply, write two or three sentences (domain split, question count, pass mark as % and count, suggested or real time), then give a tappable Markdown link to the page, e.g. **[Open Slack Administrator Practice Quiz 2](<artifact url>)**, and say that the questions appear after tapping **Start quiz** (or **Start exam**). Don't paste the bare URL and don't reveal answers in chat. Keep the link separate from any skill or file cards in the same reply.

If the user asks for a printable or document version, write plain text with numbered questions and a separate answer key at the end, using the same three parts per question, with titled Markdown links.

Afterwards, offer to review weak domains or generate a fresh set. When the user reports wrong answers or weak domains, list the review links for those questions as a short study list.

**Links in chat.** Whenever a link appears in a chat reply (study lists, review suggestions, the quiz page), write it as a tappable Markdown link with a readable title, never as a bare URL. The user often studies on a phone. A study list is one link per line, grouped by domain or topic.

## 4b. Timed exam mode (countdown)

Use this instead of practice mode when the user asks for a countdown, timer, timed exam, or "real exam conditions". Build it from the same template, without the `mode` field.

What the page does: start screen with question count, time limit and pass mark; a countdown in the header that changes colour at 5 minutes and 1 minute; one question at a time with Previous/Next, a question navigator and flag-for-review; a submit confirmation that warns about unanswered or flagged questions; automatic submission when time runs out. After submitting it shows pass/fail, score by domain, time used, a study list of review links from missed questions, and every question's explanation (filterable to incorrect, flagged or all). Progress and the clock survive closing the page.

Steps:
14. Write the questions exactly as in sections 3 and 4, with no `mode` field (timed is the default) and no hints (the real exam has none). Write `exam.json` in the shape documented at the top of `scripts/build_timed_exam.py`: `why` holds the explanation of the correct answer, `wrong` holds one line per incorrect option (the builder rejects a question that misses one), and `review` holds `{title, url}` links following the same no-invented-URL rule. Give the exam a unique `id` (cert + date + letter) so a new exam doesn't pick up saved progress from an old one.
15. Time limit: the real exam time for a full exam. For a shorter quiz, scale it (real minutes x questions / real question count, rounded up), unless the user names a time.
16. Build: `python3 <skill-dir>/scripts/build_timed_exam.py exam.json /mnt/user-data/outputs/<cert>-timed-exam.html`. It validates the data and prints the spread of correct letters; if one letter dominates, rotate options and rebuild.
17. Deliver: publish the file with the Artifact tool (favicon "⏱️", title = exam name). If the Artifact tool isn't available, present the file with present_files instead.
18. In the reply after publishing, write two sentences (exam name, question count, time limit, pass mark), then give a tappable Markdown link to the published page, e.g. **[Open the Slack Administrator Mock Exam](<artifact url>)**, and say plainly that the questions appear after tapping **Start exam**, which also starts the clock. Don't paste the bare URL, and don't reveal answers in the chat.
19. Keep the exam link separate from any skill or file cards in the same reply, so the user doesn't mistake a skill card for the exam.

When the user wants another timed exam, write new questions and a new `id`; don't edit the old page.

## 5. Repeat runs and score calibration

When the user asks for another exam, write new scenarios rather than reshuffling earlier ones, and vary which rule each question tests within a domain. If they report their score by domain, weight the next set towards their weakest domains while still covering every domain.

When discussing readiness, be honest that practice scores tend to run higher than the real exam. Suggest aiming for 80% or more on fresh use-case sets, including at least one timed run, before booking. Never present a practice score as a guaranteed pass.
