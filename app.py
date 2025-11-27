import streamlit as st
import os
import tempfile
from agents.orchestrator import Orchestrator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="Campus TaskFlow Agent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .task-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 5px solid #2196F3;
        color: #333333; /* Force dark text */
    }
    .task-card h4 {
        color: #1E1E1E;
        margin-top: 0;
    }
    .task-card p {
        color: #555555;
    }
    .priority-high { border-left-color: #f44336 !important; }
    .priority-medium { border-left-color: #ff9800 !important; }
    .priority-low { border-left-color: #4CAF50 !important; }
    
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .metric-container {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
        color: #333333; /* Force dark text */
    }
    .metric-container h3 {
        color: #2196F3; /* Brand color for numbers */
        margin: 0;
    }
    .metric-container p {
        color: #666666;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/clouds/100/000000/student-male.png", width=100)
    st.title("Campus TaskFlow")
    st.markdown("Your AI Academic Assistant")
    st.divider()
    
    with st.expander("⚙️ Settings"):
        # API Key handling - Hidden by default
        env_key = os.getenv("GEMINI_API_KEY")
        if env_key:
            st.success("API Key loaded from environment")
            use_custom_key = st.checkbox("Override API Key")
            if use_custom_key:
                api_key = st.text_input("Enter Gemini API Key", type="password")
                if api_key:
                    os.environ["GEMINI_API_KEY"] = api_key
        else:
            st.warning("API Key not found")
            api_key = st.text_input("Enter Gemini API Key", type="password")
            if api_key:
                os.environ["GEMINI_API_KEY"] = api_key

    st.info("Upload your course syllabus or assignment PDF to automatically extract tasks, plan your schedule, and generate study aids.")
    st.markdown("---")
    st.caption("v1.0.0 | Powered by Gemini 2.0 Flash")

# Main Content
st.title("🎓 Academic Workflow Automation")
st.markdown("### Transform your chaotic PDF files into an organized study plan.")

uploaded_file = st.file_uploader("Drop your course PDF here", type="pdf", help="Upload a syllabus, assignment, or reading material.")

if uploaded_file is not None:
    # Save to temp
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    col1, col2 = st.columns([3, 1])
    with col1:
        st.success(f"📄 File uploaded: **{uploaded_file.name}**")
    with col2:
        process_btn = st.button("🚀 Process Document")

    if process_btn:
        if not os.getenv("GEMINI_API_KEY"):
            st.error("❌ Please configure your Gemini API Key in Settings.")
        else:
            with st.spinner("🤖 Agents are analyzing your document..."):
                try:
                    orchestrator = Orchestrator()
                    results = orchestrator.process_and_return(tmp_file_path)
                    
                    # Metrics Row
                    m1, m2, m3 = st.columns(3)
                    with m1:
                        st.markdown(f"<div class='metric-container'><h3>{len(results.get('tasks', []))}</h3><p>Tasks Extracted</p></div>", unsafe_allow_html=True)
                    with m2:
                        st.markdown(f"<div class='metric-container'><h3>{len(results.get('plan', []))}</h3><p>Study Steps</p></div>", unsafe_allow_html=True)
                    with m3:
                        st.markdown(f"<div class='metric-container'><h3>{len(results.get('flashcards', []))}</h3><p>Flashcards</p></div>", unsafe_allow_html=True)
                    
                    st.markdown("---")

                    # Tabs for content
                    tab_tasks, tab_plan, tab_summary, tab_cards = st.tabs(["📋 Tasks & Deadlines", "📅 Study Plan", "📝 Smart Summary", "🗂️ Flashcards"])
                    
                    with tab_tasks:
                        st.subheader("Extracted Action Items")
                        tasks = results.get('tasks', [])
                        if tasks:
                            for task in tasks:
                                priority = task.get('priority', 'low').lower()
                                p_class = f"priority-{priority}"
                                
                                st.markdown(f"""
                                <div class="task-card {p_class}">
                                    <h4>{task.get('title')}</h4>
                                    <p><strong>Type:</strong> {task.get('type')} &nbsp;|&nbsp; <strong>Due:</strong> {task.get('deadline')}</p>
                                    <p>{task.get('description')}</p>
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.info("No specific tasks found in the document.")

                    with tab_plan:
                        st.subheader("AI-Generated Study Schedule")
                        plan = results.get('plan', [])
                        if plan:
                            for i, item in enumerate(plan):
                                with st.container():
                                    c1, c2 = st.columns([1, 4])
                                    with c1:
                                        st.markdown(f"**{item.get('suggested_day')}**")
                                        st.caption(item.get('estimated_duration'))
                                    with c2:
                                        st.markdown(f"**{item.get('action')}**")
                                        st.caption(f"For: {item.get('related_task')}")
                                    st.divider()
                        else:
                            st.info("No study plan could be generated.")

                    with tab_summary:
                        st.subheader("Executive Summary")
                        st.markdown(f"""
                        <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); color: #333333;">
                            {results.get('summary', "No summary available.")}
                        </div>
                        """, unsafe_allow_html=True)

                    with tab_cards:
                        st.subheader("Revision Flashcards")
                        flashcards = results.get('flashcards', [])
                        if flashcards:
                            # Custom CSS for Flip Card effect (simplified for Streamlit)
                            st.markdown("""
                            <style>
                            .flashcard {
                                background-color: white;
                                border: 1px solid #ddd;
                                border-radius: 10px;
                                padding: 20px;
                                margin-bottom: 20px;
                                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                                transition: transform 0.2s;
                            }
                            .flashcard:hover {
                                transform: translateY(-5px);
                                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
                            }
                            .flashcard-q {
                                font-weight: bold;
                                color: #333;
                                font-size: 1.1em;
                                margin-bottom: 10px;
                                border-bottom: 1px solid #eee;
                                padding-bottom: 10px;
                            }
                            .flashcard-a {
                                color: #555;
                                font-size: 1em;
                            }
                            </style>
                            """, unsafe_allow_html=True)

                            cols = st.columns(2)
                            for i, card in enumerate(flashcards):
                                with cols[i % 2]:
                                    st.markdown(f"""
                                    <div class="flashcard">
                                        <div class="flashcard-q">Q: {card.get('front')}</div>
                                        <div class="flashcard-a"><strong>A:</strong> {card.get('back')}</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                        else:
                            st.info("No flashcards generated.")
                            
                except Exception as e:
                    st.error(f"An error occurred during processing: {str(e)}")
                    import traceback
                    st.code(traceback.format_exc())
                finally:
                    if os.path.exists(tmp_file_path):
                        os.remove(tmp_file_path)
