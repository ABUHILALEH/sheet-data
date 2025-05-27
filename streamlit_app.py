import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.set_page_config(page_title="Excel Filter Tool", layout="wide")
st.title("📊 Push & Pull Data Extractor")

excel_url = st.text_input("Paste the direct GitHub file URL:")

if excel_url:
    try:
        response = requests.get(excel_url)
        if response.status_code == 200:
            file_data = BytesIO(response.content)
            df = pd.read_excel(file_data)
            st.success("Excel file loaded from GitHub!")

            st.subheader("Preview of Data")
            st.dataframe(df.head())

            # Option selection
            option = st.radio("Select what to extract:", ["Check for Label Lost", "Check for Pulled"])

            # Select column to search
            column = st.selectbox("Choose column to search in", df.columns)

            if option == "Check for Label Lost":
                filtered_df = df[df[column].astype(str).str.contains("label lost", case=False, na=False)]
            elif option == "Check for Pulled":
                filtered_df = df[df[column].astype(str).str.contains("pulled", case=False, na=False)]

            st.subheader("Filtered Results")
            st.dataframe(filtered_df)

            st.download_button(
                label="📥 Download Filtered Data as Excel",
                data=filtered_df.to_excel(index=False, engine='openpyxl'),
                file_name='filtered_data.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        else:
            st.error(f"Failed to fetch the file. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Error loading file: {e}")

