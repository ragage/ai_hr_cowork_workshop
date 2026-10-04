# Project Summary

Handoff notes for maintainers of the "Getting Things Done with Copilot Cowork for HR Tasks" kit
(as of October 3, 2026).

## Goal

A 4-hour, no-code, hands-on workshop kit, **"Getting Things Done with Copilot Cowork for HR Tasks"**,
that teaches HR staff to use Microsoft Copilot Cowork for day-to-day work and ends with a non-Cowork
exercise in Agent Builder.

- **Audience and data:** about 25 attendees sign in with their **own work accounts** in their
  organization's (production) tenant. Exercise 1 runs on each attendee's own mail, calendar, and Teams
  (private: no screen sharing); every other exercise uses the Zava sample files. Nothing is provisioned
  for attendees. The facilitator demos from a separate demo tenant, seeded for Exercise 1.
- **Sample data:** the fictional company Zava.
- **Deliverables:** Markdown guides with Word copies, an instructor PowerPoint, Word/Excel sample
  data, and a zip of the sample files.

## Current Status

- **Done and pushed** to the private repo https://github.com/cragage_microsoft/ai_hr_cowork_workshop
  (`main`).
- **Last verification passed:** no stale text, no broken links in Markdown or Word files, and the
  deck (57 slides) opens cleanly.
- **Not yet run end to end in a real tenant.**

## Architecture

- **Folders by audience:** `participant/` (workbook, quick-reference card, sample-data zip,
  after-the-workshop pack), `instructor/` (instructor deck, facilitator guide, answer key, readiness
  checklist, the facilitator's demo seed content), `communication/` (overview deck and emails), and `summary/` (this file).
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
- **Prompt colour coding:** all exercise prompts (Ex 1 keeps its exact wording; only colours were added) highlight
  their elements instead of labelling them: Goal (blue), Source (green), Expectations (orange),
  Constraints (purple). In Markdown this is `<span class="goal|source|expect|constraint">`, which
  `tools/callouts.lua` maps to the Word character styles "Prompt Goal" etc.; in `tools/content.py`
  the deck uses `{g}…{/g}`, `{s}`, `{e}`, `{c}` markers. Workbook Setup step F and deck slide 15
  teach the four elements with a weak vs. strong open-enrollment prompt.
  Every exercise card in the deck has a "Prompt key" legend picture (bottom right). Stretch prompts live at the
  end of each workbook exercise; the hands-on slides, the closing slide, and the facilitator guide
  link to the workbook.
- **Other outputs:** `instructor/instructor-deck.pptx` (57 slides),
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
  - `finalize_word.ps1`: Word COM updates contents pages and fields, one child PowerShell process
    and Word instance per file, with a time limit; QA PDFs only with `-Pdf`.
  - `make_quickref.py`: the quick-reference card.
  - `make_prompt_key.py`: the Goal / Source / Expectations / Constraints legend pictures
    (`reference/media/prompt-key*.png`) used by the workbook, prompt library, quick-reference card,
    deck slide 15, and the "Prompt key" corner of every exercise card. Run it before the deck and
    Word builds if the colours or wording change.
  - `make_download_hint.py`: the "select the Download icon" tip picture
    (`reference/media/download-hint.png`) used in the guides, emails, and both decks' kit slide.
  - `make_office_samples.py`: the Word/Excel sample files (not the zip; see Build Instructions).
  - `art/ex1-8.png`: Fluent Emoji pictures for the dividers.
  - `assets/cowork-home.png`: the Cowork home-page screenshot.
  - All paths are relative to the repo. The only external input is the source PowerPoint template,
    which isn't committed: set `DECK_TEMPLATE` to a local copy.

## Files Modified

Latest work:

- **Demo video slides (October 4):** ported from `main` (PR #1) into `build_deck.py`: a **Demo** slide
  after every scenario card, plus one after the Copilot and Cowork UI walkthrough (slide 7) and one
  after Prompting best practices (slide 16). Each has a 16:9 media placeholder, "Watch for" cues, and
  notes on inserting the recording. The facilitator guide and readiness checklist cover recording them.
- **Data model (October 3):** attendees use their own work accounts and real data for Exercise 1
  only; the participant seed step is gone. `instructor/seed-content.md` is now for the facilitator's
  demo account and recommends loading it with VS Code + GitHub Copilot (Agent mode) + the **Work IQ
  MCP server**, with the alternatives compared. Workbook, guides, emails, both decks, and the
  quick-reference card were updated (privacy etiquette, "Keep real data private" rule).
- **Prompt legend graphic:** `tools/make_prompt_key.py` draws the colour legend; it replaces the
  text legend on the exercise cards and slide 15, and appears in the workbook, prompt library, and
  quick-reference card. Hands-on slides link to the stretch prompts in the workbook.
- **`finalize_word.ps1`** rewritten to stop the hangs (see Known Issues).
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
- **Real data, kept private:** attendees share one production tenant, so Exercise 1 results stay on
  their own screen (no screen sharing), every other exercise uses the Zava files in their own
  OneDrive, skills stay "Only you", and they send only to themselves.
- **Demo seeding uses the Work IQ MCP server** (one endpoint for mail, calendar, and Teams; acts as
  the signed-in user; approvals per tool call). Writes are blocked by default: the demo-tenant admin
  allows them under Agents → Tools → Work IQ MCP → Policy (up to 24 h). Mail must come from
  other senders, so loading runs one pass per sender. MCP Server for Enterprise (read-only directory)
  and the Agent 365 per-workload servers (legacy) weren't suitable.
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
powershell -ExecutionPolicy Bypass -File tools\finalize_word.ps1   # add -Pdf for QA PDFs
```

Run `.venv\Scripts\python tools\make_prompt_key.py` first if the legend colours or wording change.

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
- **Word:** run `finalize_word.ps1 -Pdf`, then render pages from the QA PDFs (in `.build`) with PyMuPDF
  and inspect.
  `quick-reference-card.docx` must stay 1 page.
- **Links:** a Python check that every Markdown link and anchor resolves, and every external target in
  each `.docx` exists.
- **Stale text:** scan all .md files and the XML inside the Office files for the template name, the old
  sample folder `Documents/Cowork` (except `/skills`), and the old title. Expect zero hits.
- **Live:** a dry run in the attendees' tenant with one licensed work account, compared against
  [facilitator-answer-key.md](../instructor/facilitator-answer-key.md).

## Remaining Work

1. Do the tenant dry run (browser use, skill evaluation score, "Activate and run now") and update the
   answer key.
2. Optionally:
   - add dividers for the spotlight and wrap-up
   - script the demo seeding (Graph PowerShell) if you reseed often
   - rebuild the zip if the samples change
3. Re-check the Microsoft Learn pages before each delivery: cowork-available-plugins,
   cowork-local-browser, cowork-admin-governance, cowork-customize, and the Work IQ MCP pages
   (overview, policy governance) used in seed-content.md.

## Known Issues

- The deck build needs a local copy of the source PowerPoint template (`DECK_TEMPLATE`); it isn't in
  the repo.
- `finalize_word.ps1` used to hang intermittently (one Word instance for all files never returned).
  It now runs each file in its own child PowerShell process and Word instance with a time limit,
  stops only the Word processes it started, and logs to `.build/finalize.log`. A file that times
  out shows FAILED; rerun it alone (single path in `.build/made.txt`). PDF export is opt-in (`-Pdf`)
  because it often stalls right after an update. Never stop a Word you have open yourself.
- Product facts are dated October 1, 2026: plugin catalog, Edge 152 requirement, limits.
- Browser use needs an admin setting, the Edge policy, Edge 152+ and an Edge profile signed in with the
  attendee's work account. Any of these can block Exercise 3.
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
