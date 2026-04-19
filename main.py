import sys
from pathlib import Path

# Add src to Python path if necessary so module can be imported
sys.path.insert(0, str(Path(__file__).parent))

from src.document_converter import convert_pdf_to_word, convert_word_to_pdf

def get_file_selection(files: list[Path]):
    """Prompts the user to select specific files from a list."""
    if not files:
        return []
    
    print("\nFound the following files:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file.name}")
    
    print("-" * 40)
    print("Enter the numbers of the files you want to convert (e.g., '1, 3, 5') or type 'all'.")
    choice = input("Your selection: ").strip().lower()

    if choice == 'all':
        return files
    
    try:
        # Parse comma-separated numbers
        indices = [int(idx.strip()) - 1 for idx in choice.split(',') if idx.strip()]
        selected_files = [files[i] for i in indices if 0 <= i < len(files)]
        return selected_files
    except (ValueError, IndexError):
        print("Invalid input. No files selected.")
        return []

def main():
    print("Welcome to the Document Converter CLI!")
    print("-" * 40)
    print("1. Convert Word to PDF")
    print("2. Convert PDF to Word")
    print("-" * 40)
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    dir_input = input("Enter the directory path containing your files: ").strip()
    directory = Path(dir_input)

    if not directory.exists() or not directory.is_dir():
        print(f"Error: The path '{dir_input}' is not a valid directory.")
        return

    if choice == '1':
        # Scan for Word files
        word_files = sorted(list(directory.glob("*.docx")) + list(directory.glob("*.doc")))
        if not word_files:
            print("No Word files found in the directory.")
        else:
            selected = get_file_selection(word_files)
            convert_word_to_pdf(selected)
    elif choice == '2':
        # Scan for PDF files
        pdf_files = sorted(list(directory.glob("*.pdf")))
        if not pdf_files:
            print("No PDF files found in the directory.")
        else:
            selected = get_file_selection(pdf_files)
            convert_pdf_to_word(selected)
        
    print("-" * 40)
    print("Processing complete!")

if __name__ == "__main__":
    main()
