import requests
import os

def test_upload():
    url = "http://localhost:8000/upload/"
    
    # Get project root (parent of tests dir)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filename = os.path.join(project_root, "test_docs", "sample_course.pdf")
    
    if not os.path.exists(filename):
        print(f"Sample PDF not found at {filename}. Run tests/create_sample_pdf.py first.")
        return

    files = {'file': (filename, open(filename, 'rb'), 'application/pdf')}
    
    try:
        print("Sending request...")
        response = requests.post(url, files=files)
        print(f"Status Code: {response.status_code}")
        # print(f"Response: {response.text}") # Might be too long
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_upload()
