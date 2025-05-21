import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from rag_pipeline.rag_agent import RAGAgent
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
from crew.crew_setup import run_crew
from dotenv import load_dotenv
load_dotenv()

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', minute='*')
def run_main_script():
    subprocess.call(['python', 'main.py'])
    print("Main script executed.")

scheduler.start()

# Initialize
st.set_page_config(page_title="🧠 Indian Financial Market Analyst", layout="wide")
st.title("📈 Indian Financial Analyst")
st.caption("🔎 Ask questions about Indian companies, news, and markets.")

# Init RAG
rag = RAGAgent()

# Input box
query = st.text_input("💬 Ask your question here:", placeholder="e.g. What happened with Infosys last week?")

if query:
    with st.spinner("Analyzing market data..."):
        response, sources = rag.ask(query)

    st.markdown("### 🤖 Answer")
    st.success(response)

    st.markdown("---")
    st.markdown("### 📚 Sources")
    for src in sources:
        st.markdown(f"- [{src.metadata['title']}]({src.metadata['url']})")
