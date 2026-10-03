# SF-AI-Tools

AI skills for Salesforce work, packaged for Claude.

## Skills

| Skill | What it does |
|---|---|
| [`salesforce-cert-mock-exam`](skills/salesforce-cert-mock-exam/SKILL.md) | Builds hard, scenario-based mock exams, quizzes, flashcards and timed exams for any Salesforce certification (Administrator, Platform App Builder, Platform Developer, Agentforce Specialist, Data Cloud, architect exams and more). Grounded in the official exam guide, Trailhead prep trails and Salesforce Help, with explanations for every option and review links. |

## Structure

```
skills/
└── salesforce-cert-mock-exam/
    ├── SKILL.md                 # Skill instructions
    ├── references/retrieval.md  # How to find exam guides, trails and Help articles
    ├── scripts/build_timed_exam.py  # Fills and validates the timed-exam template
    └── assets/timed-exam.html   # Timed exam / practice mode HTML template
```

## Using the skill

**Claude.ai:** zip the `skills/salesforce-cert-mock-exam` folder and upload it under Settings → Capabilities → Skills.

**Claude Code:** copy the folder into `~/.claude/skills/` (personal) or `.claude/skills/` in a project.

Then just ask, e.g. *"Quiz me on Platform App Builder"* or *"Give me a timed Administrator mock exam."*

## Disclaimer

Not affiliated with or endorsed by Salesforce. Practice questions are generated from public Salesforce material and are not real exam questions.
