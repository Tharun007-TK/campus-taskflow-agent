# Campus TaskFlow Agent 🎓

**Campus TaskFlow Agent** is an intelligent multi-agent system designed to streamline academic workflows. By leveraging Gemini 2.0 Flash, it parses complex course syllabi and assignment PDFs to automatically extract key deadlines, exams, and reading requirements.

## 🚀 Features

- **📄 Smart Extraction**: Automatically identifies assignments, exams, and deadlines from PDF syllabi.
- **📅 Intelligent Planning**: Generates a detailed, day-by-day study schedule broken down by effort.
- **📝 Auto-Summarization**: Creates executive summaries of course materials.
- **🗂️ Flashcard Generation**: Automatically creates revision flashcards for active recall.
- **💻 Interactive Dashboard**: A professional Streamlit UI to manage your academic life.

## 🛠️ Tech Stack

- **Core**: Python 3.10+
- **AI Model**: Google Gemini 2.0 Flash
- **UI Framework**: Streamlit
- **PDF Processing**: pypdf
- **Environment**: python-dotenv

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/campus-taskflow-agent.git
    cd campus-taskflow-agent
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key**
    - Create a `.env` file in the root directory:
      ```env
      GEMINI_API_KEY=your_api_key_here
      ```
    - *Alternatively, you can enter the key in the UI settings.*

## 🏃‍♂️ Usage

Run the application:
```bash
streamlit run app.py
```

Upload a course PDF (syllabus, assignment, etc.) and watch the agents work!

## 📂 Project Structure

```
campus-taskflow-agent/
├── agents/             # AI Agents (Orchestrator, PDF, Planner, etc.)
├── tools/              # Helper tools (PDF extraction)
├── memory/             # Data persistence
├── app.py              # Streamlit User Interface
├── main.py             # CLI Entry point
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT
