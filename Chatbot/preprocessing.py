from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
import pymupdf
from dotenv import load_dotenv
load_dotenv()

print("PreProcessing Begins")

class PreProcessing:
    def __init__(self):
        print("PreProcessing Initialization")
        #initialization Text Splitter
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
        )
        #initialization embedding
        self.embed = OpenAIEmbeddings(model="text-embedding-3-small")
    
    def PDFReader(self,file):
        print("PDF Reading Begins")
        # reading the pdf files
        pdfs = pymupdf.open(file)
        text = ""
        with pdfs as doc:
            text = " ".join([pg.get_text() for pg in doc])
        #getting the text from pages in PDFs
        return text
    
    def Chunking(self,text):
        print("Chunking Begins")
        # splitting the text based on the pages
        words = self.splitter.split_text(text)
        return words
    
    def Embedding(self, token):
        print("Embedding Begins")
        # embedding the token and storing in token and embed format
        embed1 = self.embed.embed_documents(texts = token)
        store = [
            {"text": token, "embedding": embed1}
            for chunk, em in zip(token, embed1)
        ]
        return store
    
class QueryPreProcessing:
    def __init__(self,query_text):
        print("Query PreProcessing Initizalization")
        self.query_text = query_text
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 20,
        )
        self.embed = OpenAIEmbeddings(model="text-embedding-3-small")
    
    def Query(self):
        print("Query Chunking and Embedding Begins")
        # converting query to tokens
        #token = self.query_text.split()
        # converting tokens to embed
        embed = self.embed.embed_query(text=self.query_text, chunk_size = 100)
        
        return embed
    
# pre = PreProcessing()
# text = pre.PDFReader("C:/Users/Nayan/Downloads/GenAIProjects/ResearchPaperExtraction_GapAnalysis/test/1-s2.0-S0160791X25000375-main.pdf")
# print(text)
# print("=============================================")
# token = pre.Chunking(text)
# print(token)
# print("=============================================")
# embed = pre.Embedding(token)
# print(embed)
# print("=============================================")

# ques =  QueryPreProcessing("As i have uploaded the PDF, can you let me know the key points in the PDFs")
# q = ques.Query()
# print(q)