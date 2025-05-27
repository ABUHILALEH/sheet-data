import streamlit as st
import pandas as pd

st.set_page_config(page_title="Push Data Extractor", layout="wide")
st.title("📊 Push Data Extractor")

# Read Excel file locally (must be in the same folder as this script)
try:
    df = pd.read_excel("push.xlsx", engine="openpyxl")
    st.success("✅ Excel file loaded successfully!")

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # User selects the extraction option
    option = st.radio("Select what to extract:", ["Check for Label Lost", "Check for Pulled"])

    # User selects which column to search
    column = st.selectbox("Select column to search in", df.columns)

    # Filter data based on option
    if option == "Check for Label Lost":
        filtered_df = df[df[column].astype(str).str.contains("label lost", case=False, na=False)]
    else:  # Check for Pulled
        filtered_df = df[df[column].astype(str).str.contains("pulled", case=False, na=False)]

    st.subheader("Filtered Results")
    st.dataframe(filtered_df)

    # Download button for filtered data
    st.download_button(
        label="📥 Download Filtered Data as Excel",
        data=filtered_df.to_excel(index=False, engine='openpyxl'),
        file_name='filtered_push.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

except FileNotFoundError:
    st.error("❌ File 'push.xlsx' not found in the app directory. Please upload it to the repo.")
except Exception as e:
    st.error(f"❌ Error loading Excel file: {e}")

