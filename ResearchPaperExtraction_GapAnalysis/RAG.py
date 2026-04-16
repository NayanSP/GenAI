print("In RAG Process")
from langchain_openai import ChatOpenAI
from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


class R_A_G:
    def __init__(self, store):
        print("RAG Initialization")
        self.llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini")
        self.store = store
        self.embed_model = OpenAIEmbeddings( model="text-embedding-3-large",)
    
    def Reteriver(self,ip_query,k=3):
        print("Reteriver Starts")
        query_embed = self.embed_model.embed_query(str(ip_query))

        scores = [
            cosine_similarity([query_embed],  [item["embedding"]])[0][0]
            for item in self.store
        ]

        top_k_res = sorted(
            range(len(scores)),
            key = lambda i: scores[i],
            reverse=True
        )[:k]

        top_chunks = [self.store[i]["text"] for i in top_k_res]

        return top_chunks
    
    def Generator(self, chunks,prompt):
        print("Generation Start")
        context = "\n\n".join(chunks)
        #print(context)
        response = self.llm.invoke(prompt)
        #print(response)
        return response.content

# from preprocessing import Extraction
# from chunking import Chunking
# from embed import Embedding
# from prompts import Prompting
# extract = Extraction(pdf=r"C:\Users\Nayan\Downloads\GenAIProjects\ResearchPaperExtraction_GapAnalysis\test\1-s2.0-S0160791X25000375-main.pdf")
# text = extract.preprocess()
# ch = Chunking(text).text_chunk()
# em = Embedding(ch).text_embed()
# pr = Prompting().input_prompt()
# prm = pr.format_prompt(context="", query_input="")
# rag = R_A_G(em,prm)
# ret = rag.Reteriver()
# prm1 = pr.format_prompt(context=text, query_input="Explain in the main idea of the document")
# gen = rag.Generator(ret, prm1)
# print(gen)

        


