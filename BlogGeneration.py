import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def getLLMResponse(ip_text, no_words, blog_style):
    #ip_text: prompt
    #no_words: no of words present in the output
    #blog_style: genere 

    llm = ChatOpenAI()
    template = """
    Write a blog for {blog_style}  a topic {ip_text} within {no_words} words.
    It should include facts and technical detail related to {blog_style}"""

    prompt = PromptTemplate(
    input_variables=['blog_style', 'no_words', 'ip_text'],
    template=template
    )
    
    response = llm.invoke(
    prompt.format(
        blog_style=blog_style,
        ip_text=ip_text,
        no_words=no_words
    )
    )
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon=':Ideas:',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('Generate Blogs')

input_text = st.text_input('Enter the Blog Topic Here:')

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words:")

with col2:
    blog_style = st.text_input(label='Writing the blog for')

submit = st.button('Generate')

if submit:
    st.write(getLLMResponse(input_text, no_words, blog_style))