# Lepcha, Rai & Tamang Language Library

A Python starter project for building a source-documented vocabulary library for Lepcha, Rai varieties, and Tamang.

## What is included
- Search and add vocabulary in `app.py`
- Persistent vocabulary in JSON and CSV
- Source catalogue in `data/sources.json` and `data/sources.csv`
- Research notes and links for dictionaries/books in `sources/RESEARCH_NOTES.md`
- A source-aware schema: each word can include dialect, source, page/URL, and verification notes

## Important language-data note
“Rai” is not one single uniform language label: it can refer to multiple Kirati languages/varieties. The project should record the exact variety (for example, Danuwar/Dewas Rai or Wambule Rai) rather than merging translations as if they were interchangeable. Spellings and dialects can vary. Do not invent translations; verify them against a book, reliable dictionary, or fluent speaker.

## Data collection approach
The included catalogue points to relevant online resources and book records. Some are downloadable scans or searchable portals; others have their own copyright or reuse conditions. Review each site's terms and use public-domain/openly licensed content where permitted. Do not bulk-copy or republish copyrighted wordlists without permission. Scanned PDFs may require OCR and manual verification.

The app does not claim to contain every word in these languages yet. The vocabulary dataset starts empty so the project does not present unverified translations as facts.

## Run in Antigravity IDE (Windows)
1. Download and extract the ZIP.
2. Open Antigravity IDE, choose **Open Folder**, and select the extracted project folder.
3. Open the terminal in the IDE.
4. Run `python app.py` (or `py app.py` on Windows).
5. Select `2` to add verified words, `1` to search, `3` to view all words, or `4` to update/export CSV.

## Vocabulary fields
`english`, `lepcha`, `rai`, `tamang`, `part_of_speech`, `dialect`, `notes`, `source`, `source_url`, `page_reference`, `verified_by`

## Project structure
```text
lepcha_rai_tamang_language_library/
├── app.py
├── README.md
├── requirements.txt
├── data/
│   ├── vocabulary.json
│   ├── vocabulary.csv
│   ├── sources.json
│   └── sources.csv
└── sources/
    └── RESEARCH_NOTES.md
```
