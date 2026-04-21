import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chat_history = [
    SystemMessage(content=""" 
You are an expert Join Entrance Exam teacher. You will provide a question with valid options for the question.
Once the user answer the question, you will provide the explanation even if the option choosen is correct.
""")
]

while True:
    user_ip = input("Enter your response: ")
    chat_history.append(HumanMessage(content=user_ip))
    if user_ip == 'exit':
        print("AI Messages: Thankyou")
        break
    res = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print(res.content)

print(chat_history)
