import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage   

st.set_page_config(page_title="COnversational Q&A Chatbot")
st.header("Hey, lets chat:)")

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(temperature=2.0)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="you are a comedian AI Assistant. based on the client mood you make them happy in 5 lines.")
    ]

def get_chat_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = model.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

ip = st.text_input("Enter your text here:")
respone = get_chat_response(ip)

submit = st.button("Proceed")

if submit:
    st.subheader("Response is:")
    st.write(respone)