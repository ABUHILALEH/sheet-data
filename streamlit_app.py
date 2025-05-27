import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Filter Tool", layout="wide")

st.title("🌐 Excel Filter Tool via URL")

excel_url = st.text_input("Paste the URL of your Excel file:")

if excel_url:
    try:
        df = pd.read_excel(excel_url)
        st.success("Excel file loaded from URL!")

        st.subheader("Preview of Data")
        st.dataframe(df.head())

        column = st.selectbox("Choose column to filter", df.columns)
        keyword = st.text_input("Enter a value to search for")

        if keyword:
            filtered_df = df[df[column].astype(str).str.contains(keyword, case=False, na=False)]
            st.subheader("Filtered Results")
            st.dataframe(filtered_df)

            st.download_button(
                label="📥 Download Filtered Data as Excel",
                data=filtered_df.to_excel(index=False, engine='openpyxl'),
                file_name='filtered_data.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
    except Exception as e:
        st.error(f"❌ Failed to load file from URL: {e}")

