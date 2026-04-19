# Document Converter CLI

A simple and efficient utilities module providing Command Line Interface (CLI) application capabilities for bulk-converting documents bi-directionally between Word (DOCX) and PDF formats.

## Features

- **Convert Word to PDF**: Read `.docx` or `.doc` files safely and translate them natively to `.pdf` while preserving formatting constraints natively.
- **Convert PDF to Word**: Extract texts properly from `.pdf` documents and save those as directly editable `.docx` files securely.
- **Smart Skipping**: Automatically detects existing equivalent converted documents and strategically skips re-processing them to limit latency constraints redundantly.
- **Batch Processing**: Point natively to a targeted directory and all matching documents will dynamically convert as natively intended.

## Prerequisites

Before running the tool effectively locally, ensure these standard systemic libraries are initialized.

### 1. Python Version 
You predictably need functionally recent versions of Python (Python 3.6+ standard). Verify:

```bash
python --version
```

### 2. Required Python Library
The system seamlessly leverages `pdf2docx` internally to compute and construct PDFs into functional Word elements textually. Simply execute:

```bash
pip install pdf2docx
```

### 3. LibreOffice Configuration (Crucial on Linux)
The systemic Word-to-PDF module heavily assumes native interactions with robust background functionality given natively by `LibreOffice` standard packages running headlessly over explicit `subprocess` directives securely without impacting user screens.

Ensure it installs effectively standardially mapping on apt. Ubuntu/Debian logic works as implicitly provided:
```bash
sudo apt update
sudo apt install libreoffice
```

## How to Use Usage 

1. Launch explicitly through its natural CLI via routing main constraints:
```bash
python main.py
```

2. The UI interaction will functionally present options securely:
   - Type **1** to functionally initiate batch conversions handling 'Word specifically to PDF' translation sequences.
   - Type **2** handling functionally specific 'PDF intelligently to Word' execution modes securely.

3. Complete execution constraints dynamically by supplying functional parameters requiring explicitly accurate targeted root level subdirectories encompassing validly structured processing material.

4. Enjoy optimized outputs directly inside identically passed targeted execution paths.

## Testing Locally Functionality 

Safely unit tested implicitly ensuring secure mock configurations prevent actual systemic executions testing functional mapping logically. Standard execution works natively optimally:

```bash
python -m unittest test/test_document_converter.py
```

## Structure Setup

- `main.py`: Interactive user CLI initialization setup logic logically separated perfectly.
- `src/document_converter.py`: Conversion handler internally processing functionally. 
- `test/test_document_converter.py`: Robust mocks testing handler seamlessly securely ensuring no native dependencies internally overlap manually manually inherently.
