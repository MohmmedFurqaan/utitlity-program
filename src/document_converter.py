import sys
import subprocess
from pathlib import Path

try:
    from pdf2docx import Converter
except ImportError:
    print("The 'pdf2docx' library is not installed.")
    print("Please install it by running: uv add pdf2docx")
    sys.exit(1)

def convert_pdf_to_word(directory: Path):
    """Converts all PDF files in the specified directory to Word (DOCX)."""
    print(f"Scanning '{directory}' for PDF files...")
    pdf_files = list(directory.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    for pdf_file in pdf_files:
        docx_file = pdf_file.with_suffix(".docx")
        
        # Skip if the target DOCX file already exists
        if docx_file.exists():
            print(f"Skipping '{pdf_file.name}' - '{docx_file.name}' already exists.")
            continue

        print(f"Converting '{pdf_file.name}' to Word...")
        try:
            cv = Converter(str(pdf_file))
            cv.convert(str(docx_file))
            cv.close()
            print(f"Successfully converted to '{docx_file.name}'.")
        except Exception as e:
            print(f"Failed to convert '{pdf_file.name}': {e}")

def convert_word_to_pdf(directory: Path):
    """Converts all Word (DOCX/DOC) files in the specified directory to PDF."""
    print(f"Scanning '{directory}' for Word files...")
    
    # Matches both .doc and .docx
    word_files = list(directory.glob("*.docx")) + list(directory.glob("*.doc"))
    
    if not word_files:
        print("No Word files found in the directory.")
        return

    for word_file in word_files:
        pdf_file = word_file.with_suffix(".pdf")
        
        # Skip if the target PDF file already exists
        if pdf_file.exists():
            print(f"Skipping '{word_file.name}' - '{pdf_file.name}' already exists.")
            continue

        print(f"Converting '{word_file.name}' to PDF...")
        try:
            # We use libreoffice headless to convert to pdf on Linux
            result = subprocess.run([
                "libreoffice", "--headless", "--convert-to", "pdf", 
                str(word_file), "--outdir", str(directory)
            ], capture_output=True, text=True)

            if result.returncode == 0:
                print(f"Successfully converted to '{pdf_file.name}'.")
            else:
                print(f"Failed to convert '{word_file.name}'. Error:")
                print(result.stderr)
        except FileNotFoundError:
            print("Error: LibreOffice is not installed or not found in PATH.")
            print("Please ensure LibreOffice is installed for Word to PDF conversion on Linux system.")
            sys.exit(1)
        except Exception as e:
            print(f"Failed to convert '{word_file.name}': {e}")

