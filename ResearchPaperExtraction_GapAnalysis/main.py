from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from preprocessing import Extraction
from chunking import Chunking
from embed import Embedding
from prompts import Prompting
from RAG import R_A_G

import tempfile

st.header("Research Paper Analysis + Gap Finder")
st.subheader("This LLM helps in doing the analysis of the whole paper + helps in finding the gap in paper " \
"that should be present in Research Paper")

# Pdfs uploaded
pdfs = st.file_uploader(label="Please upload the PDFs"
                        , type= 'pdf')

#submitted button
submit = st.button("Submit")

if submit:
    #checking for pdf present or not
    if pdfs is None:
        print("No Pdfs found")
        st.error("Please upload a PDF file")
        st.stop()

    print("Pdf found and uploaded")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdfs.read())
        temp_path = tmp.name

    extract = Extraction(temp_path)
    text = extract.preprocess()

    chunks = Chunking(text) 
    ch = chunks.text_chunk()
    #st.write(ch)

    context_em = Embedding(ch)
    store = context_em.text_embed()

    pr = Prompting().input_prompt()
    pr1 = pr.format_prompt(context = "", query_input="")
    #st.write(pr1)

    rag = R_A_G(store)
    ret = rag.Reteriver(pr1)
    prm1 = pr.format_prompt(context=text, query_input="")
    gen = rag.Generator(ret, prm1)
    st.write(gen)
    print("Process Ends")







     
    

