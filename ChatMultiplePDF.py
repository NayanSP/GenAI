import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI

def get_pdf_text(pdf_doc):
    text = ""
    for pdf in pdf_doc:
        pdf_reader = PdfReader(pdf)
        for pg in pdf_reader.pages:
            text = pg.extract_text()
    return text

def get_text_chunk(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunk = text_splitter.split_text(text=raw_text)
    return chunk

def get_vectorStore(text_chunk):
    embed= OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunk, embedding= embed)
    return vectorstore

def get_conversation(vector_Store):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversational_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_Store.as_retriever(),
        memory=memory
    )

    return conversational_chain

def handle_userinput(user_query):
    if st.session_state.conversation is None:
        st.error("⚠️ Please upload and process documents first.")
        return

    response = st.session_state.conversation({'question': user_query})
    st.write(response)                     


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat wit Multiple PDF", page_icon=":books:")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    st.header("Chat wit Multiple PDFs :books:")
    st.text_input("Ask a question about your document:")

    user_query = st.text_input("Ask a question about your document")
    if user_query:
        handle_userinput(user_query)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(label="Upload your PDF here", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
            #get pdf text
                raw_text = get_pdf_text(pdf_docs)
                #st.write(raw_text)
            #get text chunks
                text_chunk = get_text_chunk(raw_text)
                #st.write(text_chunk)
            #Create vector Store
                vector_Store = get_vectorStore(text_chunk)

                #Conversation Chain
                st.session_state.conversation = get_conversation(vector_Store)


if __name__ == '__main__':
    main()