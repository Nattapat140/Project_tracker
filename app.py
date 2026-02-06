import streamlit as st
import json
import textwrap
from datetime import datetime
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Ball Project Progress Tracker",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the warm, light theme
st.markdown("""
<style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Global styles */
    .stApp {
        background: linear-gradient(135deg, #F7F1DE 0%, #FEFBF3 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
        border-bottom: 2px solid rgba(168, 187, 163, 0.3);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #8A9D85, #B87C4C, #C4A484);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .subtitle {
        color: #6b5d4f;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    
    .last-updated {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: rgba(255, 255, 255, 0.7);
        border: 2px solid rgba(168, 187, 163, 0.3);
        border-radius: 20px;
        font-size: 0.9rem;
        color: #3a3d38;
    }
    
    /* Project card styling */
    .project-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(168, 187, 163, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
        border-color: #8A9D85;
    }
    
    /* Container for project cards */
    .projects-container {
        padding-right: 0.5rem;
    }
    
    .project-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #2a2d28;
        margin-bottom: 0.5rem;
    }
    
    .project-status {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        background: linear-gradient(135deg, #8A9D85, #B87C4C);
        color: white;
        margin-bottom: 1rem;
    }
    
    .section-label {
        font-size: 0.875rem;
        color: #6b5d4f;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .task-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.5rem;
        background: rgba(168, 187, 163, 0.08);
        border-radius: 8px;
        margin-bottom: 0.5rem;
        color: #3a3d38;
    }
    
    .task-item:hover {
        background: rgba(168, 187, 163, 0.15);
    }
    
    .task-bullet {
        color: #8A9D85;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    /* Week section */
    .week-section {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(168, 187, 163, 0.3);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }
    
    .week-task-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        background: rgba(168, 187, 163, 0.08);
        border-radius: 12px;
        margin-bottom: 0.75rem;
        color: #2a2d28;
        font-size: 1.05rem;
    }
    
    .week-task-item:hover {
        background: rgba(168, 187, 163, 0.15);
    }
    
    .week-arrow {
        color: #C4A484;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.75rem;
        font-weight: 700;
        color: #2a2d28;
        margin-bottom: 1.5rem;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Data file path
DATA_FILE = Path(__file__).parent / "progress_data.json"

# Load data from file
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        pass

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Load the data
data = load_data()

# Header
st.markdown("""
<div class="main-header">
    <div class="main-title">📊 Ball Project Progress Tracker</div>
    <div class="last-updated">Last updated: {}</div>
</div>
""".format(datetime.strptime(data['lastUpdated'], "%Y-%m-%d").strftime("%B %d, %Y")), unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="section-header">📁 Projects</div>', unsafe_allow_html=True)

# Display projects in columns with scrollable container
with st.container(height=600):
    st.markdown('<div class="projects-container">', unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, project in enumerate(data['projects']):
        with cols[idx % 3]:
            # Build the HTML for the project card
            tasks_html = ''.join([f'<div class="task-item"><span class="task-bullet">•</span><span>{task}</span></div>' for task in project['tasks']])
            
            project_html = textwrap.dedent(f"""
            <div class="project-card">
                <div class="project-name">{project['name']}</div>
                <div class="project-status">{project['status']}</div>
                
                <div class="section-label" style="margin-top: 1rem;">Tasks:</div>
                {tasks_html}
            </div>
            """)
            
            st.markdown(project_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# This Week's Tasks Section
st.markdown('<div class="section-header">📅 This Week\'s Tasks</div>', unsafe_allow_html=True)

week_tasks_html = ''.join([textwrap.dedent(f"""
<div class="week-task-item">
    <span class="week-arrow">→</span>
    <span>{task}</span>
</div>
""") for task in data['weekTasks']])

st.markdown(f'<div class="week-section">{week_tasks_html}</div>', unsafe_allow_html=True)
