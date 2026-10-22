import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.header("Conversationall Message Application")
st.set_page_config(page_icon=":robot:", page_title="Conversational Message App")

if "SessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content = "You are a helpful assistant who answer as 70's person")
    ]

def load_answer(query):
    chat = ChatOpenAI(model = 'gpt-3.5-turbo',temperature = 0.0)

    st.session_state.sessionMessages.append(HumanMessage(content=query))
    answer = chat.invoke(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=answer.content))

    return answer.content

def get_text():
    input_text = st.text_input("You: ", key= input)
    return input_text

ip = get_text()
submit = st.button('Generate')

if submit:
    resp = load_answer(ip)
    st.subheader("Answer: ")
    st.write(resp)
