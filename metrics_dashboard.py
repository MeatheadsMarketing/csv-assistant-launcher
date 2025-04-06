
import streamlit as st
import pandas as pd
import ast

st.set_page_config(page_title="📊 Assistant Metrics Dashboard", layout="wide")
st.title("📊 Assistant Usage & Metrics Dashboard")

logs = st.session_state.get("logs", [])

if not logs:
    st.warning("No logs available from this session.")
else:
    data = [ast.literal_eval(log) for log in logs if isinstance(log, str) and log.startswith("{")]
    df_logs = pd.DataFrame(data)
    st.dataframe(df_logs)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Assistants Used", len(df_logs))
        st.metric("Average Runtime (s)", round(df_logs["runtime_sec"].mean(), 3))
    with col2:
        st.metric("Rows Changed (Total)", (df_logs["rows_before"] != df_logs["rows_after"]).sum())
        st.metric("Unique Assistants", df_logs["assistant"].nunique())

    st.bar_chart(df_logs["runtime_sec"])
