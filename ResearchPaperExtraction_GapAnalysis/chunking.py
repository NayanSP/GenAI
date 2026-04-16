print("In Chunking Process")
from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunking:
    def __init__(self, textual):
        print("Chunking Initialization")
        self.textual = textual
    
    def text_chunk(self):
        print("Chunking Begins")
        chunks = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
        )
        words = chunks.split_text(self.textual)
        #print(words)
        return words
    
# from preprocessing import Extraction
# extract = Extraction(pdf=r"C:\Users\Nayan\Downloads\GenAIProjects\ResearchPaperExtraction_GapAnalysis\test\1-s2.0-S0160791X25000375-main.pdf")
# text = extract.preprocess()
# ch = Chunking(text)
# ch.text_chunk()




