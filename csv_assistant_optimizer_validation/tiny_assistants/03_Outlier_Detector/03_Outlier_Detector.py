import pandas as pd
import streamlit as st

def outlier_detector(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Flags statistical outliers in numeric fields.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame to validate.
        kwargs (dict): Optional parameters (e.g., thresholds, column list).

    Returns:
        pd.DataFrame: Validation results or annotated DataFrame.
    """
    df_validated = df.copy()

    try:
        st.info("Running assistant: Outlier Detector")
        # TODO: Implement validation logic here
        pass
    except Exception as e:
        st.error(f"Error in assistant 'Outlier Detector': {e}")

    return df_validated

def run_ui():
    st.title("Outlier Detector")
    st.write("Flags statistical outliers in numeric fields.")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("Original Data")
        st.dataframe(df)

        # Optional parameters (e.g., threshold sliders)

        result_df = outlier_detector(df)
        st.subheader("Validation Results")
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Validated CSV", csv, "validated_data.csv", "text/csv")


if __name__ == "__main__":
    import sys
    if "streamlit" in sys.argv[0]:
        run_ui()
    else:
        sample_data = {
            'id': [1, 2, 2, 4],
            'email': ['a@example.com', 'b@example.com', 'c@example.com', None],
            'score': [99, 105, 87, 73]
        }
        df = pd.DataFrame(sample_data)
        result_df = outlier_detector(df)
        print(result_df)
