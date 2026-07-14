# PDF Merger Tool

## About
A Python command-line tool that merges multiple PDF files into a single document. Built for developers, IT and Computer Science students, system administrators handling batch PDF processing, and data analysts combining automatically generated reports — anyone who wants a faster, scriptable alternative to online tools or Adobe.

## Features
- **Interactive File Collection** — add PDF files one at a time, type "done" when finished
- **Path and Extension Validation** — checks that each file exists and is actually a `.pdf` before adding it, with specific error messages for each failure case
- **Minimum File Check** — requires at least 2 files before allowing the merge to proceed
- **Custom Output Naming** — name your merged file yourself, `.pdf` is auto-appended if you forget it
- **Overwrite Protection** — if the output filename already exists, asks for confirmation before overwriting
- **Error Handling** — if the merge fails for any reason, displays the exact cause instead of crashing
- **Batch Repeat** — merge another set of files immediately after finishing, or exit cleanly

## Why CLI Instead of Online Tools or Adobe
Online PDF tools require opening a browser, uploading files, waiting for processing and downloading — often 2 to 5 minutes per merge. This tool does it in one line, in under 10 seconds. It also runs entirely locally, meaning your files never leave your computer, unlike browser-based tools that upload to someone else's server. No internet connection, file size limits or subscription cost required — and because it's scriptable, it can be automated into larger workflows, unlike manual GUI tools.

## How to Run

**Requirements:** Python 3 installed on your machine, plus the `pypdf` library.

**Clone the repository:**
```bash
git clone https://github.com/GeekOryan/PDFMerger.git
```

**Navigate into the folder:**
```bash
cd PDFMerger
```

**Install the required library:**
```bash
pip install pypdf
```

**Run the program:**
```bash
python pdf_merger.py
```

**When prompted, enter full file paths without quotation marks, for example:**
