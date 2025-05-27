import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# Streamlit page settings
st.set_page_config(page_title="Push Data Extractor", layout="wide")
st.title("📊 Push Data Extractor from GitHub Excel File")

# Input: GitHub raw Excel file URL
excel_url = st.text_input("📎 Paste the GitHub raw file URL for `push.xlsx`:")

if excel_url:
    try:
        # Download file from GitHub
        response = requests.get(excel_url)
        if response.status_code == 200:
            file_data = BytesIO(response.content)

            # Load Excel using openpyxl explicitly
            df = pd.read_excel(file_data, engine="openpyxl")
            st.success("✅ Excel file loaded successfully!")

            # Show preview
            st.subheader("🔍 Preview of Data")
            st.dataframe(df.head())

            # User selects the operation
            st.subheader("🧭 Choose What to Extract")
            option = st.radio("Select an option:", ["Check for Label Lost", "Check for Pulled"])

            # Let user pick column
            column = st.selectbox("Select column to search in", df.columns)

            # Apply filter
            if option == "Check for Label Lost":
                filtered_df = df[df[column].astype(str).str.contains("label lost", case=False, na=False)]
            elif option == "Check for Pulled":
                filtered_df = df[df[column].astype(str).str.contains("pulled", case=False, na=False)]

            # Show filtered data
            st.subheader("📋 Filtered Results")
            st.dataframe(filtered_df)

            # Download button
            st.download_button(
                label="📥 Download Filtered Data as Excel",
                data=filtered_df.to_excel(index=False, engine='openpyxl'),
                file_name='filtered_push.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

        else:
            st.error(f"❌ Failed to fetch the file. HTTP Status: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Error loading file: {e}")
