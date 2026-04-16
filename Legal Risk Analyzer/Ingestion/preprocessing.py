from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.schema import Document

class PDFReader():
    print("PDF Reader is called")
    print("PDF reading starts")
    
    def __init__(self,file_path):
        self.file_path = file_path
        self.loader =  PyPDFLoader(file_path)
        print("Initializing PDF Reader")
    
    def loading_PDF(self):
        print('initizaling pdf loading')
        load1 = self.loader.load()
        length = len(load1)
        return load1, length
    
# pdf = PDFReader(r"C:/Users/Nayan/Downloads/GenAIProjects/Legal Risk Analyzer/test/camp-david-accords-egypt-1978.pdf")
# pg, length = pdf.loading_PDF()
# print(pg, length)
