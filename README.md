# Campus TaskFlow Agent

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.28%2B-FF4B4B)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-8E44AD)

**Campus TaskFlow Agent** is an intelligent, multi-agent system designed to revolutionize academic productivity. By leveraging the power of Google's **Gemini 2.0 Flash**, it transforms chaotic course materials into structured, actionable study plans.

---

## Key Features

### Multi-Agent Architecture
A sophisticated orchestration of specialized AI agents working in harmony:
- **Orchestrator Agent**: The central brain that manages workflow and data flow.
- **PDF Extraction Agent**: Intelligently parses syllabi and assignments to identify key dates.
- **Planner Agent**: Breaks down large tasks into manageable daily study blocks.
- **Notes Agent**: Generates executive summaries and revision flashcards.

### Core Capabilities
- **Smart Extraction**: Automatically identifies assignments, exams, and deadlines from PDF documents.
- **Intelligent Planning**: Creates a personalized, day-by-day study schedule based on task difficulty.
- **Auto-Summarization**: Distills complex academic texts into concise summaries.
- **Active Recall**: Automatically generates flashcards for efficient revision.
- **Professional Dashboard**: A sleek, interactive UI built with Streamlit.

---

## Technology Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| **Core Logic** | Python 3.10+ | The backbone of the application. |
| **LLM** | Google Gemini 2.0 Flash | Provides reasoning and content generation. |
| **Interface** | Streamlit | Delivers a responsive and modern web UI. |
| **PDF Engine** | pypdf | Handles robust document parsing. |
| **Environment** | python-dotenv | Manages secure configuration. |

---

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- A Google Cloud Project with Gemini API access

### Step-by-Step Guide

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Tharun007-TK/campus-taskflow-agent.git
    cd campus-taskflow-agent
    ```

2.  **Create Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```
    *(Note: You can also enter the API key directly in the application settings)*

---

## Usage

Launch the application using Streamlit:

```bash
streamlit run app.py
```

1.  **Upload**: Drag and drop your course syllabus or assignment PDF.
2.  **Process**: Click "Process Document" to let the agents analyze the file.
3.  **Review**: Explore your extracted tasks, study plan, summary, and flashcards in the dashboard.

---

## Project Structure

```plaintext
campus-taskflow-agent/
├── agents/                 # AI Agent Logic
│   ├── orchestrator.py     # Workflow manager
│   ├── pdf_agent.py        # Document parser
│   ├── planner_agent.py    # Schedule generator
│   └── notes_agent.py      # Content summarizer
├── tools/                  # Utility Tools
│   └── pdf_tools.py        # PDF processing utilities
├── memory/                 # Data Persistence
│   └── memory_store.py     # JSON-based storage
├── app.py                  # Streamlit User Interface
├── main.py                 # CLI Entry Point
├── requirements.txt        # Project Dependencies
└── README.md               # Documentation
```

---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Made with ❤️by <a href="https://github.com/Tharun007-TK">Tharun</a>
</p>
