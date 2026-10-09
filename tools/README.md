# Kit generators

These scripts build the kit's PowerPoint decks, Word copies, quick-reference card, and pictures.
Edit the content here (or in the Markdown guides), then rebuild; don't hand-edit the generated
`.pptx` and `.docx` files, because the next build overwrites them.

| Script | Builds |
| --- | --- |
| `build_deck.py` + `content.py` | `instructor/instructor-deck.pptx` |
| `build_overview.py` | `communication/training-overview.pptx` (reuses `build_deck.py`'s helpers and shared slides: keep the `# 1 — Title` marker and the shared-slide functions above it) |
| `build_preview_deck.py` | `instructor/customer-preview-deck.pptx` (no template needed; exercise text from `content.py`; `PREVIEW_CUSTOMER` and `PREVIEW_DATE` fill the title slide, `PREVIEW_OUT` changes the output path) |
| `make_word_docs.py` + `callouts.lua` | a `.docx` copy of every guide's `.md` (not `sample-knowledge/`, `summary/`, or `tools/`) |
| `finalize_word.ps1` | updates contents pages in Word, one process per file with a time limit; `-Pdf` also exports QA PDFs to `.build/` |
| `make_quickref.py` | `participant/quick-reference-card.docx` (must stay 1 page) |
| `make_prompt_key.py` | `reference/media/prompt-key*.png`: the Goal / Source / Expectations / Constraints legend (workbook, prompt library, quick-reference card, deck) |
| `make_download_hint.py` | `reference/media/download-hint.png` |
| `check_download_links.py` | builds nothing: checks the GitHub download links in the decks, emails, workbook, and quick-reference card against the working copy and `origin/main`; `--online` also opens each one without signing in |
| `check_kit.py` | builds nothing: checks Markdown links and anchors, Word links, stale text (the old title and sample folder, plus any terms in `KIT_STALE_TERMS`, separated by semicolons), and duplicate PowerPoint text highlights that trigger repair warnings; exits 1 on a problem |
| `art/ex1.png`–`ex8.png` | Fluent Emoji pictures for the exercise dividers |
| `assets/cowork-home.png` | the Cowork home-page screenshot on the "What is Copilot Cowork?" slide |
| `assets/cowork-spending-policy.png` | supplied admin-policy screenshot on the Appendix's "Cowork settings — Edge browsing & Copilot Credits" slide; example settings, not recommended unlimited spending |
| `assets/cowork-browser-settings.png` | supplied browser-access screenshot on the same Cowork settings slide; use attendee-scoped access rather than copying the example's All users setting |
| `assets/prompt-coach-agent-picker.png` + `assets/prompt-coach-example.png` | supplied screenshots on "Prompt Coach — improve a weak prompt": the Microsoft-created agent page and example open-enrollment prompt |
| `assets/cowork-new-task.png` + `assets/cowork-starter-prompts.png` + `assets/cowork-task-ideas.png` | supplied screenshots on "Sample Cowork prompts to get started", immediately before Exercise 1 |
| `assets/cowork-cost-command.png` + `assets/cowork-usage.png` | supplied screenshots on Exercise 1's closing cost-check slide: the `/cost` skill picker and monthly Usage panel |

## Requirements

- Windows with PowerPoint and Word (Word runs `finalize_word.ps1`; PowerPoint is only for checking).
- Python 3.13 or later, and the packages in `requirements.txt`.
- The **source PowerPoint template** (instructor deck and overview deck only). It isn't in the repo;
  keep a local copy and point `DECK_TEMPLATE` at it, or save it as `tools/template.pptx` (git-ignored).

## Build

From the repo root, in PowerShell:

```powershell
python -m venv .venv; .venv\Scripts\python -m pip install -r tools\requirements.txt   # first time only
$env:PYTHONIOENCODING = "utf-8"
$env:DECK_TEMPLATE = "C:\path\to\template.pptx"

.venv\Scripts\python tools\make_prompt_key.py   # only if the legend changes
.venv\Scripts\python tools\build_deck.py       # close PowerPoint first, or set $env:DECK_OUT to a preview path
.venv\Scripts\python tools\build_overview.py   # or set $env:OVERVIEW_OUT to a preview path
.venv\Scripts\python tools\build_preview_deck.py   # or set $env:PREVIEW_OUT to a preview path
.venv\Scripts\python tools\make_quickref.py
.venv\Scripts\python tools\make_word_docs.py
powershell -ExecutionPolicy Bypass -File tools\finalize_word.ps1
.venv\Scripts\python tools\check_kit.py
.venv\Scripts\python tools\check_download_links.py --online   # before sending the emails
```

Other settings: `KIT_REPO` changes the base URL of the download links on the "Workshop kit" slide.
Build files and previews go to `.build/` (ignored by Git).

Prompt highlights replace any highlighting inherited from the template; unmarked prompt text has
no highlight. Keep this behavior when changing the template or generator: duplicate `a:highlight`
elements in a run's properties violate the PowerPoint XML schema and can trigger a repair warning.

The Word/Excel files in `sample-knowledge/` are the masters (edit them directly). If they change, rebuild
`sample-knowledge/zava-sample-knowledge.zip` as described in
[summary/PROJECT-SUMMARY.md](../summary/PROJECT-SUMMARY.md#build-instructions).
