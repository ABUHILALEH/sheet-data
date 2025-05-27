import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Filter Tool", layout="wide")

st.title("📊 Excel Data Filter Tool")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("Excel file loaded!")

    st.subheader("Preview of Uploaded Data")
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
