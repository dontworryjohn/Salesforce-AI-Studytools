---
name: "salesforce-cert-mock-exam"
description: Build hard, scenario-based mock exams and quizzes for any Salesforce certification the user names (Administrator, Advanced Administrator, Platform App Builder, Platform Developer, Sales/Service Cloud Consultant, Agentforce Specialist, Data Cloud, Marketing Cloud, architect exams and others), grounded in that exam's official exam guide, its Trailhead preparation trail or trailmix, and Salesforce Help. Each answer explains why the correct option is right, why every other option is wrong, and links the Trailhead unit or Help article to review. Use whenever the user asks for a Salesforce mock exam, practice test, practice questions, exam-style quiz, flashcards or a timed exam with a countdown for a Salesforce certification or exam topic, even if they just say "quiz me on Platform App Builder" or "another mock exam". For the Salesforce Certified Slack Administrator exam, use slack-admin-mock-exam instead.
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

## 3. Write questions that are genuinely hard

Every question must be traceable to something in the sources. Never invent limits, numbers, edition entitlements or permission names. If you are unsure of a fact, drop the question rather than guess.

Make difficulty come from precision, not trickery:

- **Scenario stems.** Open with a short situation (company, edition, user type, business requirement), as the real exams do: "Universal Containers wants sales reps to see only opportunities in their region..." Ask for the best solution, the correct configuration, what happens next, or what the admin or developer should check first.
- **Distractors from adjacent truths.** Wrong options should be real Salesforce features that are correct in a neighbouring situation. Typical examples: a sharing tool that opens access when the requirement is to restrict it; a declarative tool that can't do the specific thing asked; the right feature on the wrong object or edition; a setting that sounds right but does something else. Avoid joke options and "none of the above".
- **Target the confusable pairs for that exam.** Examples: profiles vs permission sets vs permission set groups; OWD vs role hierarchy vs sharing rules vs manual sharing; lookup vs master-detail; validation rules vs Flow vs Apex triggers; record-triggered before-save vs after-save Flow; formula vs roll-up summary; page layouts vs record types vs Dynamic Forms; change sets vs Salesforce CLI/DevOps Center; reports vs report types vs dashboards. Pick the ones that matter for the exam in hand.
- **"Choose 2" / "Choose 3" questions.** The real exams have these, but the exam page takes one answer per question. Rewrite each as a single-answer question that still tests the same knowledge: ask for the one best option, or ask which option is *not* valid, or make the scenario specific enough that only one option fits. Never combine options ("A and C").
- **Keep options parallel.** Similar length and grammar, so the longest or most detailed option isn't a giveaway. Rotate the correct letter evenly across A–D.
- **One defensible answer.** Re-read each question as a sceptical examiner. If a second option could be argued correct, rewrite it.
- **Mix in a few consequence questions.** What happens to existing records, sharing, data or automation after a change.

## 4. Deliver it

Always deliver questions as the exam page built from this skill's template, never as the in-chat quiz card: the quiz card shows explanations as one plain-text paragraph, so bullet points and tappable review links are impossible there. There are two modes:

- **Practice mode (default)**: no countdown. After each answer the page locks the question, marks the right and wrong options, and shows the explanation underneath as bullet points with tappable review links. Use this for any quiz unless the user asks for a timer.
- **Timed mode**: when the user asks for a countdown, timer, timed exam or real exam conditions. See section 4b.

For each question, write:

1. **Why the answer is right** (`why`): one or two sentences naming the exact rule (who, which plan, which level).
2. **Why each other option is wrong** (`wrong`): one line per wrong option, in the form "B (option text): reason". Say what the option is actually correct for, so the learner learns the neighbouring rule too. Cover every wrong option; the builder rejects a question that misses one.
3. **Review links** (`review`): `{title, url}` for the sources the question came from. The page renders them as tappable titled links.
   - Trailhead unit: `https://trailhead.salesforce.com/content/learn/modules/<module-slug>/<unit-slug>`.
   - Help or documentation articles: use the URL as it appears in the sources or search results.
   - Never invent a slug or URL. If the exact unit is uncertain, link the module. If no URL was found, give the title only, and the page will tell the learner to search for it.

Build steps (both modes):
1. Write `exam.json` in the shape documented at the top of `scripts/build_timed_exam.py`. Set `"mode": "practice"` for practice mode, and give the exam a unique `id` (cert + date + letter) so saved progress from an old quiz isn't picked up. For practice mode, set `timeLimitMinutes` to a suggested pace (real minutes × questions ÷ real question count, rounded up); the page shows it as a suggestion only.
2. Build: `python3 <skill-dir>/scripts/build_timed_exam.py exam.json /mnt/user-data/outputs/<cert>-<practice|timed>-<n>.html`. It validates the data and prints the spread of correct letters; if one letter dominates, rotate options and rebuild.
3. Publish the file with the Artifact tool (favicon "📝" for practice, "⏱️" for timed; title = quiz name). If the Artifact tool isn't available, present the file with present_files instead.
4. In the reply, write two or three sentences (domain split, question count, pass mark as % and count, suggested or real time), then give a tappable Markdown link to the page, e.g. **[Open Slack Administrator Practice Quiz 2](<artifact url>)**, and say that the questions appear after tapping **Start quiz** (or **Start exam**). Don't paste the bare URL and don't reveal answers in chat. Keep the link separate from any skill or file cards in the same reply.

If the user asks for a printable or document version, write plain text with numbered questions and a separate answer key at the end, using the same three parts per question, with titled Markdown links.

Afterwards, offer to review weak domains or generate a fresh set. When the user reports wrong answers or weak domains, list the review links for those questions as a short study list.

**Links in chat.** Whenever a link appears in a chat reply (study lists, review suggestions, the quiz page), write it as a tappable Markdown link with a readable title, never as a bare URL. The user often studies on a phone. A study list is one link per line, grouped by domain or topic.

## 4b. Timed exam mode (countdown)

Use this instead of practice mode when the user asks for a countdown, timer, timed exam, or "real exam conditions". Build it from the same template, without the `mode` field.

What the page does: start screen with question count, time limit and pass mark; a countdown in the header that changes colour at 5 minutes and 1 minute; one question at a time with Previous/Next, a question navigator and flag-for-review; a submit confirmation that warns about unanswered or flagged questions; automatic submission when time runs out. After submitting it shows pass/fail, score by domain, time used, a study list of review links from missed questions, and every question's explanation (filterable to incorrect, flagged or all). Progress and the clock survive closing the page.

Steps:
1. Write the questions exactly as in sections 3 and 4, with no `mode` field (timed is the default) and no hints (the real exam has none). Write `exam.json` in the shape documented at the top of `scripts/build_timed_exam.py`: `why` holds the explanation of the correct answer, `wrong` holds one line per incorrect option (the builder rejects a question that misses one), and `review` holds `{title, url}` links following the same no-invented-URL rule. Give the exam a unique `id` (cert + date + letter) so a new exam doesn't pick up saved progress from an old one.
2. Time limit: the real exam time for a full exam. For a shorter quiz, scale it (real minutes x questions / real question count, rounded up), unless the user names a time.
3. Build: `python3 <skill-dir>/scripts/build_timed_exam.py exam.json /mnt/user-data/outputs/<cert>-timed-exam.html`. It validates the data and prints the spread of correct letters; if one letter dominates, rotate options and rebuild.
4. Deliver: publish the file with the Artifact tool (favicon "⏱️", title = exam name). If the Artifact tool isn't available, present the file with present_files instead.
5. In the reply after publishing, write two sentences (exam name, question count, time limit, pass mark), then give a tappable Markdown link to the published page, e.g. **[Open the Slack Administrator Mock Exam](<artifact url>)**, and say plainly that the questions appear after tapping **Start exam**, which also starts the clock. Don't paste the bare URL, and don't reveal answers in the chat.
6. Keep the exam link separate from any skill or file cards in the same reply, so the user doesn't mistake a skill card for the exam.

When the user wants another timed exam, write new questions and a new `id`; don't edit the old page.

## 5. Repeat runs

When the user asks for another exam, write new scenarios rather than reshuffling earlier ones, and vary which rule each question tests within a domain. If they report their score by domain, weight the next set towards their weakest domains while still covering every domain.
