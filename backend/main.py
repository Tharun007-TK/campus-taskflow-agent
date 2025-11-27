from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, rag
from agents.orchestrator import Orchestrator
import shutil
import os
import uuid
# Initialize DB
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Campus TaskFlow API")

# Initialize RAG
try:
    rag_engine = rag.SimpleRAGEngine()
except Exception as e:
    print(f"Failed to init RAG: {e}")
    rag_engine = None

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Save file temporarily
    file_id = str(uuid.uuid4())
    file_ext = file.filename.split(".")[-1]
    temp_filename = os.path.join("temp_docs", f"temp_{file_id}.{file_ext}")
    
    # Ensure directory exists
    os.makedirs("temp_docs", exist_ok=True)
    
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        # 1. Run Orchestrator
        orchestrator = Orchestrator()
        results = orchestrator.process_and_return(temp_filename)
        
        # 2. Save Document to DB
        db_doc = models.Document(
            filename=file.filename,
            summary=results.get('summary', '')
        )
        db.add(db_doc)
        db.commit()
        db.refresh(db_doc)
        
        # 3. Save Tasks to DB
        tasks = results.get('tasks', [])
        for t in tasks:
            db_task = models.Task(
                title=t.get('title'),
                description=t.get('description'),
                deadline=t.get('deadline'),
                priority=t.get('priority')
            )
            db.add(db_task)
        db.commit()
        
        # 4. Add to RAG
        # We need the raw text for RAG. 
        # The orchestrator extracts it internally, but we might need to expose it or re-read it.
        # For now, let's re-read using PDFTools (we need to import it)
        # Add to RAG
        if rag_engine:
            try:
                from tools.pdf_tools import PDFTools
                text = PDFTools.extract_text(temp_filename)
                rag_engine.add_document(doc_id=str(db_doc.id), text=text, metadata={"filename": file.filename})
            except Exception as e:
                print(f"RAG Indexing failed: {e}")
        
        return {
            "message": "File processed successfully",
            "document_id": db_doc.id,
            "results": results
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

@app.get("/tasks/")
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks

@app.post("/query/")
def query_knowledge_base(query: str):
    results = rag_engine.query(query)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
