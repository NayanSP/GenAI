from langchain_text_splitters import RecursiveCharacterTextSplitter

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class Chunking():
    print("PDF chunking starts")

    def __int__(self, textual: list, length: int):
        print("PDF initialization begins")
        self.textual = textual
        self.length = length

    def chunk(self, textual:list):
        print("Chunking begins")
        splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200)
        textual = [text for text in textual]
        text = splitter.split_documents(textual)
        return text
    
    def length_of_document(self,length):
        print("Length of document")
        len_of_doc = length
        return len_of_doc

# from Ingestion.preprocessing import PDFReader  
# textual, leng = PDFReader(r"C:\Users\Nayan\Downloads\GenAIProjects\Legal Risk Analyzer\test\camp-david-accords-egypt-1978.pdf").loading_PDF()
# ch = Chunking()
# print(ch.length_of_document(leng))
# print(ch.chunk(textual))
