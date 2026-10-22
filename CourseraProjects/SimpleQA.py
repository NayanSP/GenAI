import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def load_answer(query):
    llm = ChatOpenAI(temperature=0.0)
    answer = llm.invoke(query)
    return answer.content

a = load_answer("What is capital of France?")
print(a)

st.set_page_config(page_title="LangChain Simple QA",
                   page_icon=":robot:")
st.header("LangChain Simple QA")

def get_query():
    ip = st.text_input("Please enter your query here:")
    return ip

query = get_query()


submit = st.button('Generate')
if submit:
    answer = load_answer(query)    
    st.subheader("Answer: ")
    st.write(answer)
