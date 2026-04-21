import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# task 1 : response to the user query based on the task the user sends 

# task 1 : response to the user query based on the task the user sends
ip_text = st.text_input(label="Enter your query")
submit = st.button("Submit")

ip_prompt = PromptTemplate(template="""
You are expert teacher in every field. You are provided with the input query: {ip_text}.
Also provide the options for the question.
""")
llm = ChatOpenAI()
chain = ip_prompt | llm
if submit:
    res = chain.invoke({'ip_text':ip_text})
    st.write(res.content)
