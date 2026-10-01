# Project Summary

Handoff notes for maintainers of the "Getting Things Done with Copilot Cowork for HR Tasks" kit
(as of October 1, 2026).

## Goal

A 4-hour, no-code, hands-on workshop kit, **"Getting Things Done with Copilot Cowork for HR Tasks"**,
that teaches HR staff to use Microsoft Copilot Cowork for day-to-day work and ends with a non-Cowork
exercise in Agent Builder.

- **Audience:** about 25 customer attendees sharing one tenant, each with their own account. The
  facilitator demos from a separate tenant.
- **Sample data:** the fictional company Zava.
- **Deliverables:** Markdown guides with Word copies, an instructor PowerPoint, Word/Excel sample
  data, and a zip of the sample files.

## Current Status

- **Done and pushed** to the private repo https://github.com/cragage_microsoft/ai_hr_cowork_workshop.
- **Last verification passed:** `python tools\check_kit.py` reports no broken links, anchors, or
  stale text; the deck (54 slides) opens cleanly in PowerPoint.
- **Not yet run end to end in a real tenant.**

## Architecture

- **Guides:** [README.md](README.md), [participant-workbook.md](participant-workbook.md),
  [facilitator-guide.md](facilitator-guide.md), [facilitator-answer-key.md](facilitator-answer-key.md),
  [readiness-checklist.md](readiness-checklist.md), [seed-content.md](seed-content.md),
  [after-the-workshop.md](after-the-workshop.md).
- **Reference pages:** `reference/00`–`10`
  ([02](reference/02-settings-and-models.md) holds the sample custom instructions,
  [09](reference/09-plugins.md) the plugins spotlight with the SuccessFactors note,
  [10](reference/10-cowork-browser.md) browser use). Screenshots are in `reference/media/`.
- **Example skill:** [skills/hr-policy-answer/SKILL.md](skills/hr-policy-answer/SKILL.md). Its Word
  copy sits outside the skill folder.
- **Sample data:** `zava-sample-knowledge.zip` holds the six Word/Excel files attendees use; their
  editable .md/.csv sources are in `tools/zava-sample-data/` (`tools/make_office_samples.py` rebuilds
  the zip).
- **Other outputs:** `instructor-deck.pptx` (54 slides), `quick-reference-card.docx`, and a `.docx`
  copy of every guide (19 in total).
- **Deck flow per exercise:** divider → scenario card → **Demo** slide (empty media placeholder for a
  recorded run) → hands-on. Exercise 1 adds the Output folder and **`/cost`** slides; Exercise 8 carries
  a red **Not Cowork** banner on its divider, card, and demo slide.
- **Customer preview deck:** `customer-preview-deck.pptx` (17 slides) for a pre-sales or pre-delivery
  meeting: overview, agenda, exercises, safety, takeaways, prerequisites, cost, feedback questions,
  tailoring options, a feedback capture table, and next steps. Built from scratch by
  `tools/build_preview_deck.py` (no template), reusing the exercise text in `tools/content.py`.
- **Agenda (240 min):**

| Time | Segment |
| --- | --- |
| 0:00–0:40 | Welcome, Copilot vs Cowork, UI tour + setup (including custom instructions) |
| 0:40–1:05 | Ex 1 · Executive Command Center |
| 1:05–1:25 | Ex 2 · Deep Research |
| 1:25–1:35 | Break |
| 1:35–2:00 | Ex 3 · Navigate websites with Cowork's browser |
| 2:00–2:30 | Ex 4 · Custom skill |
| 2:30–2:45 | Ex 5 · Recruiting + reporting |
| 2:45–2:55 | Break |
| 2:55–3:15 | Ex 6 · Onboarding pack |
| 3:15–3:30 | Ex 7 · Automate & share |
| 3:30–3:35 | Plugins spotlight (talk only) |
| 3:35–3:55 | Ex 8 · Agent Builder |
| 3:55–4:00 | Wrap-up |

- **Generators** live in [tools/](tools) (see the README's "How to build" section):
  - `build_deck.py` and `content.py`: the deck.
  - `build_preview_deck.py`: the customer preview deck (`PREVIEW_CUSTOMER`, `PREVIEW_DATE`).
  - `make_word_docs.py` and `callouts.lua`: Markdown to Word.
  - `finalize_word.ps1`: Word COM updates contents pages and exports QA PDFs.
  - `make_quickref.py`: the quick-reference card.
  - `make_office_samples.py`: sample files and zip.
  - `check_kit.py`: link, anchor, Word-link and stale-text checks.
  - `art/ex1-8.png`: Fluent Emoji pictures for the dividers; `assets/cowork-home.png`: the Cowork
    home-page screenshot.
- **External input the deck build needs:** a local copy of the source PowerPoint template, passed
  in `DECK_TEMPLATE` or saved as the git-ignored `tools/template.pptx`. Paths are otherwise relative
  to the repo.

## Files Modified

Latest work:

- **Build:** generators and art moved into `tools/`; template, screenshot, output and scratch paths
  are configurable (`DECK_TEMPLATE`, `DECK_UI_SHOT`, `DECK_OUT`, `KIT_BUILD`); the template's stale
  slide titles are now removed from the deck metadata without naming the template; the samples
  script now also builds the zip; new `tools/check_kit.py`; README "How to build" section.
- **Deck (54 slides):** a **Demo** slide with an empty video frame (media placeholder) for every
  exercise; an Exercise 1 **"Check what the task cost"** slide (`/cost`); **Not Cowork** banners on
  Exercise 8's divider, card, and demo slide.
- **Guides:** workbook Exercise 1 step 7 (`/cost`) and an Exercise 8 "not Cowork" callout; matching
  facilitator-guide, answer-key, readiness-checklist (record demo videos, `/cost`), reference 02 and
  08, and quick-reference card updates.
- **Customer preview deck** (new): 17 slides plus the README, readiness-checklist (T − 4 to 6 weeks
  preview meeting), and build-instruction updates.

## Key Decisions

- **Sample files are .docx/.xlsx,** because Agent Builder rejects .md and .csv as knowledge.
- **Shared-tenant safety:** each attendee uses their own OneDrive copy, keeps skills "Only you", and
  sends only to themselves.
- **Browser use is its own exercise.** It's a built-in capability, not a skill, and the exercise is
  read-only on dol.gov and lni.wa.gov.
- **Approvals** are taught in setup step E and in Exercise 1.
- **Access** comes from a Cowork spending policy, per Microsoft Learn.
- **SuccessFactors:** no catalog plugin exists, so the kit points to the Employee Self-Service agent
  extension pack or a custom MCP plugin.
- **Total time stays 240 minutes.** The repo is private. The divider pictures are Fluent Emoji (MIT,
  credited in the README).
- **Custom skills keep the documented `/Documents/Cowork/skills/` path.** Only the sample-data
  folder moved.

## Build Instructions

Full details are in the README's "How to build (maintainers)" section. In short:

```powershell
cd c:\source\ai_hr_cowork_workshop
$env:DECK_TEMPLATE = "<local copy of the source template>"   # or save it as tools\template.pptx
$env:PYTHONIOENCODING = "utf-8"
python tools\make_office_samples.py
python tools\build_deck.py      # close PowerPoint first, or set $env:DECK_OUT to a preview path
python tools\build_preview_deck.py
python tools\make_quickref.py
python tools\make_word_docs.py
powershell -ExecutionPolicy Bypass -File tools\finalize_word.ps1
python tools\check_kit.py
git add -A; git commit -m "..."; git push
```

Requirements:

- Python 3.14 with python-pptx, python-docx, openpyxl, PyMuPDF, pypandoc_binary, Pillow, lxml.
- PowerPoint and Word, for COM rendering.
- The gh CLI, signed in.
- Don't use npm or pptxgenjs; LibreOffice isn't required.

## Test Instructions

- **Slides:** open with PowerPoint COM (`Presentations.Open(path,-1,0,0)`), export with
  `Slides.Item(n).Export(jpg,"JPG",1600,900)`, and inspect visually. The Demo slides' video frame is
  a media placeholder (`PlaceholderFormat.Type` 10); it's invisible in exports until a video is added.
- **Word:** render pages from the QA PDFs (in `.build`) with PyMuPDF and inspect. Check that
  `quick-reference-card.docx` keeps its page count.
- **Links and stale text:** `python tools\check_kit.py`, with `KIT_STALE_TERMS` set to the template's
  name (kept out of the repo). It checks every Markdown link and anchor, every relative link in each
  `.docx`, and scans the .md files and the XML inside the Office files for the old title, the old
  sample folder (except `/skills`), and the extra terms. Expect "OK".
- **Live:** a dry run in the tenant with one attendee account, compared against
  [facilitator-answer-key.md](facilitator-answer-key.md).

## Remaining Work

1. Do the tenant dry run (browser use, skill evaluation score, "Activate and run now", `/cost` output)
   and update the answer key.
2. Record the eight demo videos in the facilitator tenant and insert them in a facilitator copy of the
   deck (not in the repo).
3. Optionally:
   - add dividers for the spotlight and wrap-up
   - script loading the seed content into 25 accounts
4. Re-check the Microsoft Learn pages before each delivery: cowork-available-plugins,
   cowork-local-browser, cowork-admin-governance, cowork-customize,
   usage-based-billing-copilot-credits-cost.

## Known Issues

- The deck build needs the source template, which isn't in the repo.
- Product facts are dated October 1, 2026: plugin catalog, Edge 152 requirement, limits, `/cost`.
- Browser use needs an admin setting, the Edge policy, Edge 152+ and an Edge profile signed in with the
  workshop account. Any of these can block Exercise 3.
- The large divider number falls back to another font when Segoe Sans Display Bold isn't installed
  (cosmetic).
- The `{placeholders}` in the Word copies looked like parentheses in a low-resolution render; confirm in
  Word.
- Schedules from Exercises 1 and 7 keep costing money until paused.
- Rebuilding the deck replaces `instructor-deck.pptx`, so any videos inserted into it are lost; keep the
  facilitator copy with videos separately.
- After the October 1, 2026 Office update, Word on the authoring machine got slow and could hang on
  quit after the editing pass in `finalize_word.ps1`. If it stalls after listing all 19 documents,
  stop that `WINWORD` process: the documents are already saved. Export the QA PDFs from a fresh Word
  instance.

## Next Session Starting Prompt

> Continue work on the HR Copilot Cowork workshop kit in `c:\source\ai_hr_cowork_workshop` (GitHub:
> cragage_microsoft/ai_hr_cowork_workshop, private). Read `README.md` (including "How to build") and
> `PROJECT-SUMMARY.md` first. The generators are in `tools/`; the deck build needs the source
> PowerPoint template via `DECK_TEMPLATE`. Next task: run the tenant dry run with one attendee account
> (including the browser exercise, the skill evaluation score, "Activate and run now", and `/cost`),
> update the answer key with what you see, rebuild, run `python tools\check_kit.py`, then commit and
> push. Keep the "Getting Things Done" title, the `Documents/ai_hr_cowork_workshop` sample folder, and
> the Exercise 1–8 order. Don't name the source template in any artifact.
