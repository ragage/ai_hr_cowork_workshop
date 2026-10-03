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
  deck (47 slides) opens cleanly.
- **Not yet run end to end in a real tenant.**

## Architecture

- **Folders by audience:** `participant/` (workbook, quick-reference card, sample-data zip,
  after-the-workshop pack), `instructor/` (instructor deck, facilitator guide, answer key, readiness
  checklist, seed content), `communication/` (overview deck and emails), and `summary/` (this file).
  Only `README.md` and its Word copy stay at the root.
- **Guides:** [README.md](../README.md), [participant-workbook.md](../participant/participant-workbook.md),
  [facilitator-guide.md](../instructor/facilitator-guide.md), [facilitator-answer-key.md](../instructor/facilitator-answer-key.md),
  [readiness-checklist.md](../instructor/readiness-checklist.md), [seed-content.md](../instructor/seed-content.md),
  [after-the-workshop.md](../participant/after-the-workshop.md).
- **Reference pages:** `reference/00`–`10`
  ([02](../reference/02-settings-and-models.md) holds the sample custom instructions,
  [09](../reference/09-plugins.md) the plugins spotlight with the SuccessFactors note,
  [10](../reference/10-cowork-browser.md) browser use). Screenshots are in `reference/media/`.
- **Example skill:** [skills/hr-policy-answer/SKILL.md](../skills/hr-policy-answer/SKILL.md). Its Word
  copy sits outside the skill folder.
- **Sample data:** `sample-knowledge/` holds the .docx/.xlsx files plus their editable .md/.csv
  sources; `participant/zava-sample-knowledge.zip` holds the six Word/Excel files inside an
  `ai_hr_cowork_workshop/` folder (the same name as the OneDrive folder the prompts use).
- **Communication:** `communication/` holds the training overview deck (`training-overview.pptx`,
  8 slides) and two paste-ready Outlook emails (`participant-email.html`, `instructor-email.html`).
  Both decks' "Workshop kit" slide and the emails link to files on `main` in this repo
  (`/raw/main/...` downloads), so update them together when files move.
- **Prompt colour coding:** exercise prompts (Ex 2–8; Ex 1 is deliberately left plain) highlight
  their elements instead of labelling them: Goal (blue), Source (green), Expectations (orange),
  Constraints (purple). In Markdown this is `<span class="goal|source|expect|constraint">`, which
  `tools/callouts.lua` maps to the Word character styles "Prompt Goal" etc.; in `tools/content.py`
  the deck uses `{g}…{/g}`, `{s}`, `{e}`, `{c}` markers. Workbook Setup step F and deck slide 14
  teach the four elements with a weak vs. strong open-enrollment prompt.
- **Other outputs:** `instructor/instructor-deck.pptx` (47 slides),
  `participant/quick-reference-card.docx`, and a `.docx` copy of every guide (19 in total).
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

- **Generators** live in `tools/` (see [tools/README.md](../tools/README.md)):
  - `build_deck.py` and `content.py`: the instructor deck.
  - `build_overview.py`: the training overview deck. It reuses `build_deck.py`'s helpers and shared
    slides (agenda, objectives, workshop-kit links) by running the part of that file before the
    `# 1 — Title` marker, so keep that marker and the shared-slide functions above it.
  - `make_word_docs.py` and `callouts.lua`: Markdown to Word.
  - `finalize_word.ps1`: Word COM updates contents pages and exports QA PDFs.
  - `make_quickref.py`: the quick-reference card.
  - `make_download_hint.py`: the "select the Download icon" tip picture
    (`reference/media/download-hint.png`) used in the guides, emails, and both decks' kit slide.
  - `make_office_samples.py`: the Word/Excel sample files (not the zip; see Build Instructions).
  - `art/ex1-8.png`: Fluent Emoji pictures for the dividers.
  - `assets/cowork-home.png`: the Cowork home-page screenshot.
  - All paths are relative to the repo. The only external input is the source PowerPoint template,
    which isn't committed: set `DECK_TEMPLATE` to a local copy.

## Files Modified

Latest work:

- **Decks:**
  - the instructor deck lives in `instructor/instructor-deck.pptx` (the generator's `OUT` points there)
  - a new training overview deck, `communication/training-overview.pptx`, built by `build_overview.py`
  - a "Workshop kit — download links" slide in both decks (before Setup in the instructor deck), with
    participant and instructor links (base URL in `KIT_REPO`, overridable by environment variable)
  - the Setup slide now says to upload the zip's `ai_hr_cowork_workshop` folder with Folder upload
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
cd c:\source\ai_hr_cowork_workshop
python -m venv .venv; .venv\Scripts\python -m pip install -r tools\requirements.txt   # first time only
$env:PYTHONIOENCODING = "utf-8"; $env:DECK_TEMPLATE = "<path to the source template .pptx>"
.venv\Scripts\python tools\build_deck.py      # close PowerPoint first, or set $env:DECK_OUT to a preview path
.venv\Scripts\python tools\build_overview.py  # or set $env:OVERVIEW_OUT to a preview path
.venv\Scripts\python tools\make_quickref.py
.venv\Scripts\python tools\make_word_docs.py
powershell -ExecutionPolicy Bypass -File tools\finalize_word.ps1
```

If the sample Word/Excel files change, rebuild the zip so the six files sit inside an
`ai_hr_cowork_workshop/` folder:

```powershell
cd c:\source\ai_hr_cowork_workshop
$z = New-Item -ItemType Directory -Force "$env:TEMP\zava-zip\ai_hr_cowork_workshop"
Copy-Item sample-knowledge\*.docx, sample-knowledge\*.xlsx $z -Force
Compress-Archive -Path $z -DestinationPath participant\zava-sample-knowledge.zip -Force
Remove-Item "$env:TEMP\zava-zip" -Recurse -Force
```

Requirements:

- Python 3.13+ with the packages in `tools/requirements.txt`, plus PyMuPDF for the QA renders.
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
  [facilitator-answer-key.md](../instructor/facilitator-answer-key.md).

## Remaining Work

1. Fix `tools/finalize_word.ps1` hanging (see Known Issues).
2. Do the tenant dry run (browser use, skill evaluation score, "Activate and run now") and update the
   answer key.
3. Optionally:
   - add dividers for the spotlight and wrap-up
   - script loading the seed content into 25 accounts
   - rebuild the zip if the samples change
4. Re-check the Microsoft Learn pages before each delivery: cowork-available-plugins,
   cowork-local-browser, cowork-admin-governance, cowork-customize.

## Known Issues

- The deck build needs a local copy of the source PowerPoint template (`DECK_TEMPLATE`); it isn't in
  the repo.
- On October 3, 2026, `finalize_word.ps1` hung with no output (its Word automation instance never
  returned, probably waiting on a hidden dialog) and had to be stopped. Until it's fixed, a Word
  rebuild leaves the contents pages empty: refresh them in Word, or don't commit rebuilt `.docx`
  files whose text didn't change. It hung again later that day on two files. Running each step
  separately (open, TOC update, field update, save, PDF export) on the same files then succeeded
  in 7–22 s each, so the hang is intermittent rather than one bad step. Workaround: finalize one file
  at a time (put a single path in `.build/made.txt`), and stop only the `/Automation` WINWORD
  process, plus its `~$` lock file, if it stalls.
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
> cragage_microsoft/ai_hr_cowork_workshop, private, `main`). Read `README.md`, `summary/PROJECT-SUMMARY.md`
> and `tools/README.md` first. The generators are in `tools/`; `build_deck.py` needs `DECK_TEMPLATE`
> set to the local PowerPoint template. Keep the "Getting Things Done" title, the
> `Documents/ai_hr_cowork_workshop` sample folder, and the Exercise 1–8 order. Don't name the source
> template in any artifact.
