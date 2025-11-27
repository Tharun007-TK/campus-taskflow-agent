from agents.base_agent import BaseAgent
from tools.pdf_tools import PDFTools
import json

class PDFAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def extract_tasks(self, file_path: str) -> list:
        """
        Extracts tasks and events from a PDF file.
        """
        print(f"Extracting text from {file_path}...")
        text = PDFTools.extract_text(file_path)
        if not text:
            return []

        prompt = f"""
        You are an academic assistant. Analyze the following text extracted from a course document (syllabus, assignment, etc.).
        Extract all assignments, exams, deadlines, and key events.
        Return the result as a JSON list of objects, where each object has:
        - 'title': Name of the task/event
        - 'type': 'assignment', 'exam', 'reading', 'other'
        - 'deadline': Date and time if available (or 'TBD')
        - 'description': Brief description
        - 'priority': 'high', 'medium', 'low' (infer based on context)

        Text:
        {text[:10000]}  # Limit text to avoid context window issues if very large
        
        Output JSON only, no markdown formatting.
        """
        
        print("Analyzing text with LLM...")
        response_text = self.generate_response(prompt)
        
        # Clean up response if it contains markdown code blocks
        response_text = response_text.replace("```json", "").replace("```", "").strip()
        
        try:
            tasks = json.loads(response_text)
            return tasks
        except json.JSONDecodeError:
            print("Failed to parse JSON response from LLM.")
            print("Raw response:", response_text)
            return []
