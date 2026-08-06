import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_classic.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Langchain Demo", page_icon=":robot:")
st.header('Hi! I am a Bot')

if 'sessionMessages' not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content = "You are a helpful assistant")
    ]

def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content = question))
    assistant_answer = chat.invoke(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content = assistant_answer.content))
    return assistant_answer.content

def get_Text():
    ip = st.text_input("You: ", key = input)
    return ip

chat = ChatOpenAI()

user_ip = get_Text()
submit = st.button("Submit")

if submit:
    resp = load_answer(user_ip)
    st.subheader("Answer: ", resp)
    st.write(resp)
