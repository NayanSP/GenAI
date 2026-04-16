import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

class Embedding:
    print("pdf Embedding starts")

    def __init__(self, chunk=None):
        print('pdf embedding initizalization')
        self.embed = OpenAIEmbeddings(model="text-embedding-3-large",)
        self.chunk = chunk
    
    def embed_pdf(self):
        print('pdf embedding')
        texts = [doc.page_content for doc in self.chunk]
        embeddings = self.embed.embed_documents(texts)
        return embeddings

# text,_ = PDFReader(r"C:\Users\Nayan\Downloads\GenAIProjects\Legal Risk Analyzer\test\camp-david-accords-egypt-1978.pdf").loading_PDF()
# chunk = Chunking().chunk(text)
# em = Embedding(chunk=chunk)
# a = em.embed_pdf()
# print(a)