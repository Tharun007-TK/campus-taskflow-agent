import os
import sys

# Add project root to sys.path to allow importing backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.rag import SimpleRAGEngine
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("No API Key")
        # exit(1) # SimpleRAGEngine handles missing key gracefully
        
    print("Initializing Simple RAG Engine...")
    try:
        rag = SimpleRAGEngine()
        
        print("Adding documents...")
        docs = [
            ("id1", "Artificial Intelligence is the simulation of human intelligence processes by machines."),
            ("id2", "Machine learning is a subset of AI that involves training algorithms on data.")
        ]
        
        for doc_id, text in docs:
            rag.add_document(doc_id, text)
        
        print("Documents added.")
        
        print("Querying for 'AI'...")
        results = rag.query("What is AI?", n_results=1)
        print(f"Query Results: {results}")
        
        print("Querying for 'ML'...")
        results = rag.query("training algorithms", n_results=1)
        print(f"Query Results: {results}")

    except Exception as e:
        print(f"CRASHED: {e}")
        import traceback
        traceback.print_exc()
