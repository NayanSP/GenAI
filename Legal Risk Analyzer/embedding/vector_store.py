import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_classic.schema import Document
import shutil
import os

class VectorStore:
    print('Vector Store begins')

    def __init__(self, dir="chroma_db"):
        print('Vector store initialization')
        self.dir = dir
        self.embedding = OpenAIEmbeddings( model="text-embedding-3-large", )
        self.vs = None

    def vector_store(self, chunk):
        print('Vector Storing')
        texts = [doc.page_content for doc in chunk]
        metadatas = [doc.metadata for doc in chunk]

        vector_db = Chroma.from_documents(
        documents=chunk,
        embedding=self.embedding,
        persist_directory= self.dir    )
        if vector_db:
            vector_db.persist()
        return vector_db

    def reset_chroma(self):   # ✅ correct
        import shutil, os
        if os.path.exists("chroma_db"):
            shutil.rmtree("chroma_db")
        
# from Ingestion.preprocessing import PDFReader
# from Ingestion.chunker import Chunking
# from embedding.embed import Embedding
# text,_ = PDFReader(r"C:\Users\Nayan\Downloads\GenAIProjects\Legal Risk Analyzer\test\camp-david-accords-egypt-1978.pdf").loading_PDF()
# chunk = Chunking().chunk(text)
# em = Embedding(chunk=chunk)
# a = em.embed_pdf()
# vs = VectorStore()
# store = vs.vector_store(chunk)
# print(store)

