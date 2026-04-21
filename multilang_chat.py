from langchain_openai import ChatOpenAI
from langchain_classic.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

prompt = PromptTemplate(template="""
You are an general knowlege and language expert. You have knowledge of all fields. 
the user provides question in the language selected: {lang}
the user input is:{ip_text}
You have to do below task:
Task 1. Convert it to English Language
Task 2. provide the details of the query asked in 10 lines
Task 3. convert the task 2 into same language as user selected: {lang}
""")

model = ChatOpenAI()

chain = prompt | model
lang_Sel = st.selectbox("Select language you want to written the text in",
                         options=['marathi','hindi','telgu', 'chinese', 'urdu'])
text = st.text_input("Please enter sentence in any language for conversion")


if text:
    st.write(text)
    res = chain.invoke({'lang':lang_Sel,'ip_text':text})
    st.write(res.content)