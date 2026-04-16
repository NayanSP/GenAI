from dotenv import load_dotenv

load_dotenv() 
import streamlit as st

jd = st.text_input(label="Enter your job Description here")

resume = st.file_uploader(label="Enter your pdf resume file here", accept_multiple_files=False)

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

embed = OpenAIEmbeddings()
llm = ChatOpenAI(temperature=0.2)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are an expert technical recruiter, resume reviewer and interviewer.
Analyze the job description and resume present below, you need to provide feedback in the following structure
Below struture is for resume
1. Overall Summary 3 lines - should provide the quality of resume 
2. Strengths
3. weakness
4. Missing sections - why is it necessary
5. Bullet point for improvemnet - why is it necessary
6. ATS friendly check for each section out of 10 with reasoning. you can provide a table here with title and ats score to it
7. Final actionable suggestion

Once resume analysis is done, you can check how compatible the resume is with the job description provided.
Here you can provide as below:
1. Overall compatiblity score
2. Common points between job description and resume
3. Points which are essential as per job description - put it in 2 parts, one that was present in resume and 2nd which was not present with reasoning

Once this is completed, you can provide the question interviewer may ask
you can think this as below
1. based on resume provided
2. based on job description

Job Description:
{job_d}

Resume:
{resume1}

Analyze the resume and give feedback.
""")
chain = prompt | llm

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    res = chain.invoke({'job_d': jd, 'resume1':resume})
    st.write(res.content)