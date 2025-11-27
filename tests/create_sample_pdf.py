from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, 750, "CS101: Introduction to Artificial Intelligence")
    
    # Subtitle
    c.setFont("Helvetica", 14)
    c.drawString(100, 720, "Fall 2025 Syllabus")

    # Content
    c.setFont("Helvetica", 12)
    text_lines = [
        "Instructor: Dr. Alan Turing",
        "Office Hours: Mon/Wed 2-4 PM",
        "",
        "Course Description:",
        "This course introduces the basic principles of artificial intelligence.",
        "Topics include search, machine learning, and logic.",
        "",
        "Assignments & Exams:",
        "1. Assignment 1: Search Algorithms",
        "   - Due Date: October 15, 2025",
        "   - Description: Implement BFS and DFS in Python.",
        "",
        "2. Midterm Exam",
        "   - Date: November 1, 2025",
        "   - Location: Hall A",
        "",
        "3. Assignment 2: Neural Networks",
        "   - Due Date: November 20, 2025",
        "   - Description: Build a simple MLP using NumPy.",
        "",
        "4. Final Project Proposal",
        "   - Due Date: December 5, 2025",
        "",
        "5. Final Exam",
        "   - Date: December 15, 2025",
    ]

    y = 680
    for line in text_lines:
        c.drawString(100, y, line)
        y -= 20

    c.save()

if __name__ == "__main__":
    import os
    # Get project root (parent of tests dir)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    test_docs_dir = os.path.join(project_root, "test_docs")
    
    os.makedirs(test_docs_dir, exist_ok=True)
    output_path = os.path.join(test_docs_dir, "sample_course.pdf")
    create_sample_pdf(output_path)
    print(f"Created {output_path}")
