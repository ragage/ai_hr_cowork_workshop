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

- **Done and pushed** to the private repo https://github.com/cragage_microsoft/ai_hr_cowork_workshop
  (`main`).
- **Last verification passed:** no stale text, no broken links in Markdown or Word files, and the
  deck (45 slides) opens cleanly.
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
- **Sample data:** `sample-knowledge/` holds the .docx/.xlsx files plus their editable .md/.csv
  sources; `zava-sample-knowledge.zip` holds the six Word/Excel files inside an
  `ai_hr_cowork_workshop/` folder (the same name as the OneDrive folder the prompts use).
- **Other outputs:** `instructor-deck.pptx` (45 slides), `quick-reference-card.docx`, and a `.docx`
  copy of every guide (19 in total).
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

- **Generators (not in this repo)** live in the authoring session folder
  `c:\Users\cragage\.copilot\session-state\051732a1-5bba-4dda-a082-a71c80e8bdca\files\deck-generator\`:
  - `build_deck.py` and `content.py`: the deck.
  - `make_word_docs.py` and `callouts.lua`: Markdown to Word.
  - `finalize_word.ps1`: Word COM updates contents pages and exports QA PDFs.
  - `make_quickref.py`: the quick-reference card.
  - `make_office_samples.py`: the Word/Excel sample files (not the zip; see Build Instructions).
  - `art/ex1-8.png`: Fluent Emoji pictures for the dividers.
- **External inputs the deck build needs:** a local copy of the source PowerPoint template, and the
  Cowork home-page screenshot (`UI_SHOT` in `build_deck.py`).

## Files Modified

Latest work:

- **Deck:**
  - a divider before each exercise, with number, picture, time and a 1–8 tracker
  - one PowerPoint section per exercise
  - a new custom-instructions setup slide
  - the spotlight slide now highlights SAP SuccessFactors and links to the plugin catalog
  - template references and metadata removed
- **Workbook:**
  - the inbox exercise removed and Exercises 1–3 renumbered
  - a new browser exercise
  - setup steps for the OneDrive folder (B), custom instructions with samples (D) and approvals (E)
  - new-hire name changed to Sofia Alvarez; Ex 5a is now an inclusive job posting
- **New files:** `reference/10-cowork-browser.md`, `reference/09-plugins.md`, `.gitignore`, and two
  screenshots in `reference/media/`.
- **All other guides and Word copies** updated to the new numbering, the
  `Documents/ai_hr_cowork_workshop` folder, the spending-policy access model, and the
  "Getting Things Done" title.

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

```powershell
$g = "<path to deck-generator folder>"
cd c:\source\ai_hr_cowork_workshop
New-Item -ItemType Directory -Force .build | Out-Null; Copy-Item "$g\*" .build\ -Recurse -Force
cd .build; $env:PYTHONIOENCODING = "utf-8"
python build_deck.py      # close PowerPoint first, or set $env:DECK_OUT to a preview path
python make_quickref.py
python make_word_docs.py
powershell -ExecutionPolicy Bypass -File finalize_word.ps1
# copy any edited generator back to $g; then:
cd ..; Remove-Item .build -Recurse -Force; git add -A; git commit -m "..."; git push
```

If the sample Word/Excel files change, rebuild the zip so the six files sit inside an
`ai_hr_cowork_workshop/` folder:

```powershell
cd c:\source\ai_hr_cowork_workshop
$z = New-Item -ItemType Directory -Force "$env:TEMP\zava-zip\ai_hr_cowork_workshop"
Copy-Item sample-knowledge\*.docx, sample-knowledge\*.xlsx $z -Force
Compress-Archive -Path $z -DestinationPath zava-sample-knowledge.zip -Force
Remove-Item "$env:TEMP\zava-zip" -Recurse -Force
```

Requirements:

- Python 3.14 with python-pptx, python-docx, openpyxl, PyMuPDF, pypandoc_binary, Pillow.
- PowerPoint and Word, for COM rendering.
- The gh CLI, signed in.
- Don't use npm or pptxgenjs; LibreOffice isn't required.

## Test Instructions

- **Slides:** open with PowerPoint COM (`Presentations.Open(path,-1,0,0)`), export with
  `Slides.Item(n).Export(jpg,"JPG",1600,900)`, and inspect visually.
- **Word:** render pages from the QA PDFs (in `.build`) with PyMuPDF and inspect.
  `quick-reference-card.docx` must stay 1 page.
- **Links:** a Python check that every Markdown link and anchor resolves, and every external target in
  each `.docx` exists.
- **Stale text:** scan all .md files and the XML inside the Office files for the template name, the old
  sample folder `Documents/Cowork` (except `/skills`), and the old title. Expect zero hits.
- **Live:** a dry run in the tenant with one attendee account, compared against
  [facilitator-answer-key.md](facilitator-answer-key.md).

## Remaining Work

1. Move the generators and art into the repo (for example `tools/`) and make the template and
   screenshot paths configurable.
2. Do the tenant dry run (browser use, skill evaluation score, "Activate and run now") and update the
   answer key.
3. Optionally:
   - add dividers for the spotlight and wrap-up
   - script loading the seed content into 25 accounts
   - rebuild the zip if the samples change
4. Re-check the Microsoft Learn pages before each delivery: cowork-available-plugins,
   cowork-local-browser, cowork-admin-governance, cowork-customize.

## Known Issues

- The deck build depends on absolute local paths (template and screenshot), so it breaks on another
  machine.
- Product facts are dated October 1, 2026: plugin catalog, Edge 152 requirement, limits.
- Browser use needs an admin setting, the Edge policy, Edge 152+ and an Edge profile signed in with the
  workshop account. Any of these can block Exercise 3.
- The large divider number falls back to another font when Segoe Sans Display Bold isn't installed
  (cosmetic).
- The `{placeholders}` in the Word copies looked like parentheses in a low-resolution render; confirm in
  Word.
- Schedules from Exercises 1 and 7 keep costing money until paused.

## Next Session Starting Prompt

> Continue work on the HR Copilot Cowork workshop kit in `c:\source\ai_hr_cowork_workshop` (GitHub:
> cragage_microsoft/ai_hr_cowork_workshop, private, `main`). Read `README.md` and `PROJECT-SUMMARY.md`
> first. The generators live in the authoring session's `deck-generator` folder (copy them to `.build\`
> to run; `build_deck.py` also needs the local PowerPoint template). First task: move the generators
> and `art/` into the repo under `tools/`, make the template and screenshot paths configurable
> (environment variables or relative paths), add a "How to build" section to the README, rebuild
> everything, run the link and stale-text checks, then commit and push. Keep the "Getting Things Done"
> title, the `Documents/ai_hr_cowork_workshop` sample folder, and the Exercise 1–8 order. Don't name
> the source template in any artifact.
