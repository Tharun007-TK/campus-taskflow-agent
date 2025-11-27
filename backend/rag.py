import os
import json
import numpy as np
import google.generativeai as genai
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

# Simple persistence file
DB_FILE = "simple_rag_db.json"

class SimpleRAGEngine:
    def __init__(self):
        self.documents = [] # List of {"id": str, "text": str, "metadata": dict, "embedding": list}
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
        else:
            print("Warning: GEMINI_API_KEY not found. RAG will not work.")

        self.load_db()

    def load_db(self):
        if os.path.exists(DB_FILE):
            try:
                with open(DB_FILE, 'r') as f:
                    self.documents = json.load(f)
                print(f"Loaded {len(self.documents)} documents from {DB_FILE}")
            except Exception as e:
                print(f"Error loading DB: {e}")
                self.documents = []

    def save_db(self):
        try:
            with open(DB_FILE, 'w') as f:
                json.dump(self.documents, f)
            print(f"Saved {len(self.documents)} documents to {DB_FILE}")
        except Exception as e:
            print(f"Error saving DB: {e}")

    def _get_embedding(self, text: str) -> List[float]:
        if not self.api_key:
            return [0.0] * 768
        try:
            model = "models/text-embedding-004"
            result = genai.embed_content(
                model=model,
                content=text,
                task_type="retrieval_document",
                title="Custom Query"
            )
            return result['embedding']
        except Exception as e:
            print(f"Embedding error: {e}")
            return [0.0] * 768

    def add_document(self, doc_id: str, text: str, metadata: Dict[str, Any] = None):
        # Check if exists
        for doc in self.documents:
            if doc['id'] == doc_id:
                print(f"Document {doc_id} already exists. Skipping.")
                return

        embedding = self._get_embedding(text)
        doc = {
            "id": doc_id,
            "text": text,
            "metadata": metadata or {},
            "embedding": embedding
        }
        self.documents.append(doc)
        self.save_db()

    def query(self, query_text: str, n_results: int = 3) -> List[str]:
        if not self.documents:
            return []

        query_embedding = self._get_embedding(query_text)
        
        # Calculate Cosine Similarity
        # Sim(A, B) = (A . B) / (||A|| * ||B||)
        
        scores = []
        q_vec = np.array(query_embedding)
        q_norm = np.linalg.norm(q_vec)
        
        if q_norm == 0:
            return []

        for doc in self.documents:
            d_vec = np.array(doc['embedding'])
            d_norm = np.linalg.norm(d_vec)
            
            if d_norm == 0:
                score = 0
            else:
                score = np.dot(q_vec, d_vec) / (q_norm * d_norm)
            
            scores.append((score, doc['text']))
        
        # Sort by score descending
        scores.sort(key=lambda x: x[0], reverse=True)
        
        # Return top N texts
        return [item[1] for item in scores[:n_results]]
