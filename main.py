import sys
from pathlib import Path

# Add src to Python path if necessary so module can be imported
sys.path.insert(0, str(Path(__file__).parent))

from src.document_converter import convert_pdf_to_word, convert_word_to_pdf

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
        convert_word_to_pdf(directory)
    elif choice == '2':
        convert_pdf_to_word(directory)
        
    print("-" * 40)
    print("Processing complete!")

if __name__ == "__main__":
    main()
