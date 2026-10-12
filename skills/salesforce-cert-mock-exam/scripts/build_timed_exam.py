#!/usr/bin/env python3
"""Fill the timed exam template with exam data and validate it.

Usage: python3 build_timed_exam.py exam.json output.html

exam.json shape:
{
  "id": "pab-2026-10-02-a",            # unique per exam (keys saved progress)
  "title": "Platform App Builder mock exam",
  "subtitle": "Winter '27 exam guide",   # optional
  "mode": "practice",                     # optional: instant feedback, no countdown (omit for a timed exam)
  "timeLimitMinutes": 105,
  "passPercent": 63,
  "questions": [
    {"id": "q01", "domain": "Salesforce Fundamentals",
     "prompt": "...",
     "options": [{"id": "a", "text": "..."}, {"id": "b", "text": "..."}, ...],
     "correct": "b",
     "why": "Why the correct answer is right.",
     "wrong": ["A (Option text): why it's wrong / what it's for.", "..."],
     "review": [{"title": "Trailhead unit or Help article title", "url": "https://..."}]}
  ]
}
"""
import json, sys, pathlib

def fail(msg):
    sys.exit("ERROR: " + msg)

src, out = sys.argv[1], sys.argv[2]
exam = json.loads(pathlib.Path(src).read_text())
for k in ("title", "timeLimitMinutes", "passPercent", "questions"):
    if k not in exam: fail(f"missing '{k}'")
qs = exam["questions"]
if not qs: fail("no questions")
ids, letters = set(), {}
for i, q in enumerate(qs, 1):
    for k in ("id", "prompt", "options", "correct", "why"):
        if k not in q: fail(f"question {i} missing '{k}'")
    if q["id"] in ids: fail(f"duplicate question id {q['id']}")
    ids.add(q["id"])
    opt_ids = [o["id"] for o in q["options"]]
    if len(opt_ids) < 2 or len(set(opt_ids)) != len(opt_ids): fail(f"question {i} has bad options")
    if q["correct"] not in opt_ids: fail(f"question {i}: correct '{q['correct']}' not in options")
    if len(q.get("wrong", [])) != len(opt_ids) - 1:
        fail(f"question {i}: needs one 'wrong' line per incorrect option ({len(opt_ids)-1})")
    for r in q.get("review", []):
        if r.get("url") and not r["url"].startswith(("https://", "http://")): fail(f"question {i}: bad review url")
    pos = opt_ids.index(q["correct"])
    letters[pos] = letters.get(pos, 0) + 1

tpl = pathlib.Path(__file__).resolve().parent.parent / "assets" / "timed-exam.html"
html = tpl.read_text()
# Escape "</" so exam text can never close the JSON script tag
payload = json.dumps(exam, ensure_ascii=False).replace("</", "<\\/")
html = html.replace("__EXAM_JSON__", payload)
# Static <title> names the published page, so set it to the exam title
import html as htmlmod
html = html.replace("<title>Mock exam</title>", "<title>" + htmlmod.escape(exam["title"]) + "</title>", 1)
pathlib.Path(out).write_text(html)
dist = ", ".join(f"{chr(65+k)}={v}" for k, v in sorted(letters.items()))
print(f"OK: {len(qs)} questions, {exam['timeLimitMinutes']} min, pass {exam['passPercent']}%. Correct-letter spread: {dist}")
print(f"Wrote {out}")
