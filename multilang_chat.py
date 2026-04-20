from langchain_openai import ChatOpenAI
from langchain_classic.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

prompt = PromptTemplate(template="Your can convert {lang} to english which is typed in english:{ip_text}")

model = ChatOpenAI()

chain = prompt | model
lang_Sel = st.selectbox("Select language you want to written the text in",
                         options=['marathi','hindi','telgu', 'chinese', 'urdu'])
text = st.text_input("Please enter sentence in any language for conversion")

if text:
    st.write(text)
    res = chain.invoke({'lang': lang_Sel,'ip_text':text})
    st.write(res.content)