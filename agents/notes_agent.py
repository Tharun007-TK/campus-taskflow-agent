from agents.base_agent import BaseAgent
from tools.pdf_tools import PDFTools

class NotesAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def summarize_content(self, file_path: str) -> str:
        """
        Generates a summary of the PDF content.
        """
        print(f"Summarizing {file_path}...")
        text = PDFTools.extract_text(file_path)
        if not text:
            return ""

        prompt = f"""
        Summarize the following academic text. Provide key takeaways and a brief overview.
        
        Text:
        {text[:10000]}
        """
        
        return self.generate_response(prompt)

    def create_flashcards(self, file_path: str) -> list:
        """
        Generates flashcards from the PDF content.
        """
        print(f"Creating flashcards for {file_path}...")
        text = PDFTools.extract_text(file_path)
        if not text:
            return []
            
        prompt = f"""
        Create 5 flashcards based on the following text.
        Format as a JSON list of objects with 'front' and 'back' keys.
        
        Text:
        {text[:10000]}
        
        Output JSON only.
        """
        
        response = self.generate_response(prompt)
        response = response.replace("```json", "").replace("```", "").strip()
        
        import json
        try:
            return json.loads(response)
        except:
            return []
