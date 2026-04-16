import streamlit as st
import tempfile
from Ingestion import chunker, preprocessing
from embedding import embed, vector_store
from LLMs.prompts import get_prompt
from LLMs.output_parser import get_parser
from GetData.reteriver import RetrieverClass
from GetData.generator import Generator

st.header("Legal Document Analyzer")
st.subheader("Analyzing the legal document and returns the output in the structured format" \
"which will help in understanding more.")
pdf = st.file_uploader(label="Please enter Legal Document",
                type='pdf')
option = st.selectbox(label="Select the type of response you want to know:",
             options = [    "Answer",    "Summary",    "Risk Analysis",    "Key Clauses",
                            "Obligations",    "From Claimant Side",    "From Defendant Side"])

submit = st.button('Submit')

if submit:
    if pdf is None:
        st.error("Please upload a PDF file")
        st.stop()
    
    st.write("File is submitted the processing will begin now")
    if pdf is not None:
        print("Reading the PDF(s)")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf.read())
            temp_path = tmp.name

    #preprocessing the uploaded PDF file
    preprocess = preprocessing.PDFReader(temp_path)
    text, length = preprocess.loading_PDF()

    #Chunking the preprocessed text
    ch = chunker.Chunking()
    textual = ch.chunk(text)
    
    #Embedding the chunked text
    embed = embed.Embedding(textual)
    em = embed.embed_pdf()

    #Vector Storing the chunked and embeded text
    vs = vector_store.VectorStore()
    vs.reset_chroma()
    vs1 = vs.vector_store(textual)

    #Query Handling
    ip_prompt = get_prompt(option=option)

    #Output Parser
    op_parser = get_parser(option=option)

    #Generator
    gen = Generator()
    result = gen.generate(prompt=ip_prompt,
                          parser = op_parser,
                          mode=option)    

    #Output from reteriver

    st.success("Analysis Completed")
    st.subheader("Result as below")
    try:
        st.json(result.dict())
    except:
        st.write(result)

    if option == "Risk Analysis" and hasattr(result, "risks"):
        st.subheader("⚠️ Risk Breakdown")

        for r in result.risks:
            st.markdown(f"**Clause:** {r.clause}")
            st.markdown(f"**Risk Level:** {r.risk_level}")
            st.markdown(f"**Reason:** {r.reason}")
            st.markdown("---")    

    
    

    