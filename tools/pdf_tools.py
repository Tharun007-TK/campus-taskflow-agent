import pypdf
import os

class PDFTools:
    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extracts text from a PDF file.
        
        Args:
            file_path (str): The path to the PDF file.
            
        Returns:
            str: The extracted text.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        text = ""
        try:
            with open(file_path, 'rb') as file:
                reader = pypdf.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""
            
        return text

    @staticmethod
    def get_metadata(file_path: str) -> dict:
        """
        Extracts metadata from a PDF file.
        """
        if not os.path.exists(file_path):
             raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with open(file_path, 'rb') as file:
                reader = pypdf.PdfReader(file)
                return reader.metadata
        except Exception as e:
            print(f"Error reading metadata: {e}")
            return {}
