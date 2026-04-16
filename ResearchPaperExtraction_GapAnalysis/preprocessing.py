print("In Document Preprocessing")
import fitz  
import pymupdf
class Extraction:
    
    def __init__(self,pdf):
        print("Data PreProcessing Initialization")
        self.pdf = pymupdf.open(pdf)
    
    def preprocess(self):
        print("Data Preprocessing Begins")
        text = ""
        with self.pdf as doc:
            text = "".join([pg.get_text() for pg in doc])
            #print(text)
        return text

# extract = Extraction(pdf=r"C:\Users\Nayan\Downloads\GenAIProjects\ResearchPaperExtraction_GapAnalysis\test\1-s2.0-S0160791X25000375-main.pdf")
# extract.preprocess()

    



