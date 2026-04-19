import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# Ensure src is in the python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.document_converter import convert_pdf_to_word, convert_word_to_pdf

class TestDocumentConverter(unittest.TestCase):
    
    @patch('src.document_converter.Converter')
    def test_convert_pdf_to_word_success(self, MockConverter):
        # Setup mock directory
        mock_dir = MagicMock(spec=Path)
        
        # Setup mock PDF file
        mock_pdf_file = MagicMock(spec=Path)
        mock_pdf_file.name = "test.pdf"
        mock_pdf_file.__str__.return_value = "test.pdf"
        
        # Setup mock DOCX file (target)
        mock_docx_file = MagicMock(spec=Path)
        mock_docx_file.name = "test.docx"
        mock_docx_file.__str__.return_value = "test.docx"
        mock_docx_file.exists.return_value = False
        
        mock_pdf_file.with_suffix.return_value = mock_docx_file
        
        # Set the directory.glob to return our mock pdf
        mock_dir.glob.return_value = [mock_pdf_file]
        
        # Mock converter instance
        mock_cv_instance = MockConverter.return_value
        
        # Call function
        convert_pdf_to_word(mock_dir)
        
        # Assertions
        mock_dir.glob.assert_called_with("*.pdf")
        MockConverter.assert_called_with("test.pdf")
        mock_cv_instance.convert.assert_called_with("test.docx")
        mock_cv_instance.close.assert_called_once()
        
    def test_convert_pdf_to_word_skip_existing(self):
        mock_dir = MagicMock(spec=Path)
        
        mock_pdf_file = MagicMock(spec=Path)
        mock_docx_file = MagicMock(spec=Path)
        mock_docx_file.exists.return_value = True # File already exists!
        mock_pdf_file.with_suffix.return_value = mock_docx_file
        
        mock_dir.glob.return_value = [mock_pdf_file]
        
        with patch('src.document_converter.Converter') as MockConverter:
            convert_pdf_to_word(mock_dir)
            MockConverter.assert_not_called()

    @patch('src.document_converter.subprocess.run')
    def test_convert_word_to_pdf_success(self, mock_subprocess_run):
        # Setup mock directory
        mock_dir = MagicMock(spec=Path)
        mock_dir.__str__.return_value = "/mock/dir"
        
        # Setup mock Word file
        mock_word_file = MagicMock(spec=Path)
        mock_word_file.name = "test.docx"
        mock_word_file.__str__.return_value = "/mock/dir/test.docx"
        
        # Setup mock PDF file (target)
        mock_pdf_file = MagicMock(spec=Path)
        mock_pdf_file.name = "test.pdf"
        mock_pdf_file.exists.return_value = False
        
        mock_word_file.with_suffix.return_value = mock_pdf_file
        
        # Set dir.glob for .docx to return word file, and .doc to return empty
        def glob_side_effect(pattern):
            if pattern == "*.docx":
                return [mock_word_file]
            return []
        
        mock_dir.glob.side_effect = glob_side_effect
        
        # Mock successful subprocess
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess_run.return_value = mock_result
        
        convert_word_to_pdf(mock_dir)
        
        mock_subprocess_run.assert_called_with([
            "libreoffice", "--headless", "--convert-to", "pdf", 
            "/mock/dir/test.docx", "--outdir", "/mock/dir"
        ], capture_output=True, text=True)
        
    @patch('src.document_converter.subprocess.run')
    def test_convert_word_to_pdf_skip_existing(self, mock_subprocess_run):
        # Setup mock directory
        mock_dir = MagicMock(spec=Path)
        
        # Setup mock Word file
        mock_word_file = MagicMock(spec=Path)
        
        # Setup mock PDF file (target) that exists
        mock_pdf_file = MagicMock(spec=Path)
        mock_pdf_file.exists.return_value = True # File already exists!
        
        mock_word_file.with_suffix.return_value = mock_pdf_file
        mock_dir.glob.side_effect = lambda pattern: [mock_word_file] if pattern == "*.docx" else []
        
        convert_word_to_pdf(mock_dir)
        
        # subprocess.run should not be called since file exists
        mock_subprocess_run.assert_not_called()

if __name__ == '__main__':
    unittest.main()
