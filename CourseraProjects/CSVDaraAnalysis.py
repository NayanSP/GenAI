import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from utils import query_qgent

load_dotenv()

st.title("Let's do analysis on CSV")
st.header("Please upload CSV file here")
data = st.file_uploader("Upload CSV file", type="csv")

query = st.text_area("Enter your query here:")
button = st.button("Analyze")

if button:
    answer = query_agent(data, query)
    st.write(answer)