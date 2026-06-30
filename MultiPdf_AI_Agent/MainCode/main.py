import streamlit as st
from pypdf import PdfReader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import openai
from langchain_classic.vectorstores import FAISS
from langchain_classic.chains.question_answering import load_qa_chain
from langchain_classic.prompts import PromptTemplate


load_dotenv()


#get the pdf file
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_read = PdfReader(pdf)
        for pg in pdf_read.pages:
            text += pg.extract_text()
    return text

#get text chunks
def get_chunk_text(text):
    text_split = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap = 1000)
    chunks = text_split.split_text(text)
    return chunks

#get vector
def get_vectore_store(text_chunks):
    embed = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embed)
    vector_store.save_local('faiss_index')


#get prompt and chains
def get_conversational_chains():
    prompt = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatOpenAI(temperature=0.2)
    prompt1 = PromptTemplate(template=prompt, input_variables=['context','question'])
    chain = load_qa_chain(model, main_type='stuff', prompt = prompt1)
    return chain

def user_ip(user_ques):
    embed = OpenAIEmbeddings()
    new_db = FAISS.load_local('faiss_index', embed)
    docs = new_db.similarity_search(user_ques)
    chain = get_conversational_chains()

    response = chain(
        {'input_documnets':docs, 'question':user_ques}
         ,return_only_outputs=True
    )
    print(response)
    st.write('Reply',response['output_text'])

def main():
    st.set_page_config("Multi PDF Chatbot", page_icon = ":scroll:")
    st.header("Multi-PDF's 📚 - Chat Agent 🤖 ")

    user_question = st.text_input("Ask a Question from the PDF Files uploaded .. ✍️📝")

    if user_question:
        user_ip(user_question)

    with st.sidebar:
 
        st.title("📁 PDF File's Section")
        pdf_docs = st.file_uploader("Upload your PDF Files & \n Click on the Submit & Process Button ", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."): # user friendly message.
                raw_text = get_pdf_text(pdf_docs) # get the pdf text
                text_chunks = get_chunk_text(raw_text) # get the text chunks
                get_vectore_store(text_chunks) # create vector store
                st.success("Done")
        
        st.write("---")
    

    

if __name__ == "__main__":
    main()