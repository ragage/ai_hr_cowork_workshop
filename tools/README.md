# Kit generators

These scripts build the kit's PowerPoint decks, Word copies, quick-reference card, and pictures.
Edit the content here (or in the Markdown guides), then rebuild; don't hand-edit the generated
`.pptx` and `.docx` files, because the next build overwrites them.

| Script | Builds |
| --- | --- |
| `build_deck.py` + `content.py` | `instructor/instructor-deck.pptx` |
| `build_overview.py` | `communication/training-overview.pptx` (reuses `build_deck.py`'s helpers and shared slides: keep the `# 1 — Title` marker and the shared-slide functions above it) |
| `make_word_docs.py` + `callouts.lua` | a `.docx` copy of every guide's `.md` (not `sample-knowledge/`, `summary/`, or `tools/`) |
| `finalize_word.ps1` | updates contents pages in Word, one process per file with a time limit; `-Pdf` also exports QA PDFs to `.build/` |
| `make_quickref.py` | `participant/quick-reference-card.docx` (must stay 1 page) |
| `make_prompt_key.py` | `reference/media/prompt-key*.png`: the Goal / Source / Expectations / Constraints legend (workbook, prompt library, quick-reference card, deck) |
| `make_download_hint.py` | `reference/media/download-hint.png` |
| `make_office_samples.py` | the Word/Excel copies in `sample-knowledge/` (not the zip) |
| `art/ex1.png`–`ex8.png` | Fluent Emoji pictures for the exercise dividers |
| `assets/cowork-home.png` | the Cowork home-page screenshot on the "What is Copilot Cowork?" slide |

## Requirements

- Windows with PowerPoint and Word (Word runs `finalize_word.ps1`; PowerPoint is only for checking).
- Python 3.13 or later, and the packages in `requirements.txt`.
- The **source PowerPoint template**. It isn't in the repo; keep a local copy and point
  `DECK_TEMPLATE` at it.

## Build

From the repo root, in PowerShell:

```powershell
python -m venv .venv; .venv\Scripts\python -m pip install -r tools\requirements.txt   # first time only
$env:PYTHONIOENCODING = "utf-8"
$env:DECK_TEMPLATE = "C:\path\to\template.pptx"

.venv\Scripts\python tools\make_prompt_key.py   # only if the legend changes
.venv\Scripts\python tools\build_deck.py       # close PowerPoint first, or set $env:DECK_OUT to a preview path
.venv\Scripts\python tools\build_overview.py   # or set $env:OVERVIEW_OUT to a preview path
.venv\Scripts\python tools\make_quickref.py
.venv\Scripts\python tools\make_word_docs.py
powershell -ExecutionPolicy Bypass -File tools\finalize_word.ps1
```

Other settings: `KIT_REPO` changes the base URL of the download links on the "Workshop kit" slide.
Build files and previews go to `.build/` (ignored by Git).

If the sample Word/Excel files change, rebuild `participant/zava-sample-knowledge.zip` as described in
[summary/PROJECT-SUMMARY.md](../summary/PROJECT-SUMMARY.md#build-instructions).
