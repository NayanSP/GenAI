from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# Step 1: Translate to English
translate_to_english_prompt = PromptTemplate.from_template(
    "Translate the following text from {lang} to English:\n\n{text}"
)

translate_chain = translate_to_english_prompt | model

# Step 2: Generate response in English
response_prompt = PromptTemplate.from_template(
    "Answer the following question in English:\n\n{question}"
)

response_chain = response_prompt | model

# Step 3: Translate back to original language
translate_back_prompt = PromptTemplate.from_template(
    "Translate the following English response to {lang}:\n\n{text}"
)

translate_back_chain = translate_back_prompt | model


# Streamlit UI
lang_sel = st.selectbox(
    "Select language",
    options=['Marathi', 'Hindi', 'Telugu', 'Chinese', 'Urdu']
)

text = st.text_input("Enter your text")

if text:
    st.write("Original:", text)

    # Step 1: to English
    english_text = translate_chain.invoke({
        "lang": lang_sel,
        "text": text
    }).content

    st.write("Translated to English:", english_text)

    # Step 2: Generate response
    english_response = response_chain.invoke({
        "question": english_text
    }).content

    st.write("Response in English:", english_response)

    # Step 3: Back to original language
    final_response = translate_back_chain.invoke({
        "lang": lang_sel,
        "text": english_response
    }).content

    st.write("Final Response:", final_response)