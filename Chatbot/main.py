import streamlit as st

file = st.file_uploader(label="Please upload the PDF here: ",
                 type='.pdf')

if file:
    st.write("PDFs is uploaded")

    user_query = st.text_input(label="Please input your query here:")
    