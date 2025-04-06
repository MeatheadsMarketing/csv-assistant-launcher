import streamlit as st
import importlib.util
import os
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

ASSISTANT_ROOT = "csv_assistant_optimizer"  # Parent folder containing all Category folders
st.set_page_config(page_title="Unified CSV Assistant Launcher", layout="wide")

def call_gpt_summary(text, model="gpt-4", max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": f"Summarize the purpose of this assistant:\n{text}"}],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"[GPT Summary Error: {e}]"

# Persistent storage for session state
if "recent" not in st.session_state:
    st.session_state.recent = []
if "favorites" not in st.session_state:
    st.session_state.favorites = set()
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "logs" not in st.session_state:
    st.session_state.logs = []
if "versions" not in st.session_state:
    st.session_state.versions = {}

st.title("🧠 Unified CSV Assistant Launcher")

# Theme toggle (light/dark)
st.session_state.theme = st.selectbox("🎨 Theme", ["light", "dark"], index=0 if st.session_state.theme == "light" else 1)

# Global dataset uploader
uploaded_data = st.file_uploader("📤 Upload a dataset (used across all assistants)", type=["csv"])
global_df = pd.read_csv(uploaded_data) if uploaded_data else None
if global_df is not None:
    with st.expander("📊 Preview Uploaded Dataset"):
        st.dataframe(global_df)

# Search bar with autocomplete-like filter
search_query = st.text_input("🔍 Search for assistants or keywords", "")

# Load all categories and assistant folders
def get_all_assistants():
    data = []
    for category in sorted(os.listdir(ASSISTANT_ROOT)):
        category_path = os.path.join(ASSISTANT_ROOT, category, "tiny_assistants")
        if os.path.isdir(category_path):
            for folder in sorted(os.listdir(category_path)):
                folder_path = os.path.join(category_path, folder)
                py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]
                md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
                if py_files:
                    data.append({
                        "category": category,
                        "name": folder,
                        "py_path": os.path.join(folder_path, py_files[0]),
                        "md_path": os.path.join(folder_path, md_files[0]) if md_files else None,
                        "timestamp": datetime.now().isoformat(),
                        "version": "v1.0.0"
                    })
    return data

assistants = get_all_assistants()

# Filter by search query
if search_query:
    assistants = [a for a in assistants if search_query.lower() in a["name"].lower() or (a["category"].lower().find(search_query.lower()) != -1)]

# Sidebar Recent and Favorites
st.sidebar.markdown("### ⭐ Favorites")
for fav in list(st.session_state.favorites):
    if st.sidebar.button(fav, key=f"fav_{fav}"):
        st.session_state.search_query = fav

st.sidebar.markdown("### 🕘 Recent")
for recent in st.session_state.recent[-5:][::-1]:
    st.sidebar.text(recent)

st.sidebar.markdown("### 🧾 Logs")
for log in st.session_state.logs[-3:][::-1]:
    st.sidebar.caption(log)

# Group assistants by category
categories = sorted(set(a["category"] for a in assistants))
for cat in categories:
    with st.expander(f"📁 {cat}", expanded=False):
        cat_assistants = [a for a in assistants if a["category"] == cat]
        for assistant in cat_assistants:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**🧠 {assistant['name']}** \[{assistant['version']}]")
                if assistant['md_path'] and os.path.exists(assistant['md_path']):
                    with open(assistant['md_path'], "r") as f:
                        md_content = f.read()
                        st.markdown(md_content)
                        ai_summary = call_gpt_summary(md_content)
                        st.success(f"🔎 AI Summary: {ai_summary}")
            with col2:
                if st.button("Launch", key=assistant['py_path']):
                    st.session_state.recent.append(assistant['name'])
                    st.session_state.logs.append(f"Launched {assistant['name']} at {datetime.now().strftime('%H:%M:%S')}")
                    spec = importlib.util.spec_from_file_location("assistant_module", assistant['py_path'])
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if hasattr(module, "run_ui"):
                        module.run_ui()
                    else:
                        st.warning("Selected assistant does not have a `run_ui()` function.")
            with col3:
                if st.button("⭐", key=f"star_{assistant['py_path']}"):
                    st.session_state.favorites.add(assistant['name'])
