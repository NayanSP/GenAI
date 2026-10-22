import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS

print("Imports successful")
embed = OpenAIEmbeddings()

st.set_page_config(page_title="Find Similar Text", page_icon=":education:")
st.header("Ask your doubt here")
loader = CSVLoader(file_path='myData.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})

data = loader.load()
print(data)

db = FAISS.from_documents(data,embed)

def get_text():
    ip = st.text_input("Enter your question here")
    return ip

ip = get_text()

submit = st.button("Answer")

if submit:
    answer = db.similarity_search(ip)
    print(answer)
    st.subheader("Answer:")
    st.text(answer[0])
    st.text(answer[1].page_content)

