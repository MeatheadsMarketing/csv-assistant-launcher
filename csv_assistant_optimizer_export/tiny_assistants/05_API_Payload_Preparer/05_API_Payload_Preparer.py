import pandas as pd
import streamlit as st

def api_payload_preparer(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Formats rows for use as JSON payloads to external APIs.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        kwargs (dict): Export options, schema settings, file config.

    Returns:
        pd.DataFrame: Optionally returns the exported (or final) DataFrame.
    """
    df_export = df.copy()

    try:
        st.info("Running assistant: API Payload Preparer")
        # TODO: Add export formatting, transformation, or delivery logic here
        pass
    except Exception as e:
        st.error(f"Error in assistant 'API Payload Preparer': {e}")

    return df_export

def run_ui():
    st.title("API Payload Preparer")
    st.write("Formats rows for use as JSON payloads to external APIs.")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("Input Data")
        st.dataframe(df)

        result_df = api_payload_preparer(df)
        st.subheader("Export Preview")
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Export", csv, "exported_output.csv", "text/csv")


if __name__ == "__main__":
    import sys
    if "streamlit" in sys.argv[0]:
        run_ui()
    else:
        sample_data = {
            'id': [1, 2],
            'name': ['Alpha', 'Beta'],
            'value': [100, 200]
        }
        df = pd.DataFrame(sample_data)
        result_df = api_payload_preparer(df)
        print(result_df)
