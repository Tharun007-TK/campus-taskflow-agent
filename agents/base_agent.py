import os
import google.generativeai as genai
from colorama import Fore
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, model_name="gemini-2.0-flash"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            # Fallback or warning - for now just print warning
            print(Fore.YELLOW + "Warning: GEMINI_API_KEY environment variable not set.")
        else:
            genai.configure(api_key=self.api_key)
            
        self.model_name = model_name
        self.model = genai.GenerativeModel(model_name)

    def generate_response(self, prompt: str) -> str:
        """
        Generates a response from the LLM.
        """
        if not self.api_key:
            return "Mock Response: API Key missing."
            
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(Fore.RED + f"Error generating response: {e}")
            return ""
