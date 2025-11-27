import subprocess
import time
import sys
import os
import requests

def wait_for_backend(url, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code != 500: # 404 is fine, means server is up
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    return False

def run_app():
    print("🚀 Starting Campus TaskFlow Agent...")
    
    # 1. Start Backend
    print("🔹 Starting Backend API (FastAPI)...")
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"],
        cwd=os.getcwd()
    )
    
    # Wait for backend to be ready
    print("⏳ Waiting for backend to initialize...")
    if wait_for_backend("http://localhost:8000/docs"):
        print("✅ Backend is ready!")
    else:
        print("❌ Backend failed to start. Check logs.")
        backend_process.terminate()
        return

    # 2. Start Frontend
    print("🔹 Starting Frontend (Streamlit)...")
    frontend_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "app.py"],
        cwd=os.getcwd()
    )
    
    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping services...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ Services stopped.")

if __name__ == "__main__":
    run_app()
