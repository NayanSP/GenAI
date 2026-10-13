import streamlit as st
import dotenv
dotenv.load_dotenv()

from langchain_openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings()

from langchain_core.vectorstores import FAISS

st.header("Hi! Please enter the words, we will find the similar word from my data")

import pandas as pd
from langchain_core.documents import Document

# Load Excel
df = pd.read_excel("words.xlsx")

# Convert each word into a LangChain Document
documents = [
    Document(
        page_content=str(word),
        metadata={"row": index + 1}
    )
    for index, word in enumerate(df["words"])
]

# Check the documents
for doc in documents:
    print(doc.page_content)

vectors = embedding.embed_documents(
    [doc.page_content for doc in documents]
)

print(len(vectors))
print(len(vectors[0]))