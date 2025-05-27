import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Push Data Extractor", layout="wide")
st.title("📊 Push Data Extractor (Upload Excel File)")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Read the uploaded Excel file
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.success("✅ Excel file loaded successfully!")

        st.subheader("Preview of Data")
        st.dataframe(df.head())

        # Select filtering option
        option = st.radio("Select what to extract:", ["Check for Label Lost", "Check for Pulled"])

        # Select column to search
        column = st.selectbox("Select column to search in", df.columns)

        # Apply filter based on user choice
        if option == "Check for Label Lost":
            filtered_df = df[df[column].astype(str).str.contains("label lost", case=False, na=False)]
        else:
            filtered_df = df[df[column].astype(str).str.contains("pulled", case=False, na=False)]

        st.subheader("Filtered Results")
        st.dataframe(filtered_df)

        # Download button for filtered data
        towrite = BytesIO()
        filtered_df.to_excel(towrite, index=False, engine='openpyxl')
        towrite.seek(0)

        st.download_button(
            label="📥 Download Filtered Data as Excel",
            data=towrite,
            file_name='filtered_push.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("Please upload an Excel (.xlsx) file to get started.")


