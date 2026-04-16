from langchain_openai import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()

print("In Embedding Process")
class Embedding:

    def __init__(self,chunks):
        print("Embedding Initialization")
        self.embed = OpenAIEmbeddings( model="text-embedding-3-large",)
        #self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.chunks = chunks

    def text_embed(self):
        print("Embedding Starts")
        em = self.embed.embed_documents(texts=self.chunks)
        #em = self.model.encode(self.chunks) 
        #above statement while using groq 

        #print(em)
        store = [
            {"text": chunk, "embedding": em}
            for chunk, em in zip(self.chunks, em)
        ]
        return store


# from preprocessing import Extraction
# from chunking import Chunking
# extract = Extraction(pdf=r"C:\Users\Nayan\Downloads\GenAIProjects\ResearchPaperExtraction_GapAnalysis\test\1-s2.0-S0160791X25000375-main.pdf")
# text = extract.preprocess()
# ch = Chunking(text).text_chunk()
# print(ch)
# em = Embedding(ch).text_embed()
# print(em)