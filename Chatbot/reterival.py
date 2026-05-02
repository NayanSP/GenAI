print("In Reterival and Generation")
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

class ReteriveGenerate:
    def __init__(self, store, question):
        print("ReteriveGenration Intialization")
        self.model  = ChatOpenAI(temperature=0.0, model="gpt-4o-mini")
        self.embedding = OpenAIEmbeddings(model="text-embedding-3-small",)
        self.store = store
        self.query = question
    
    def Reterive(self,k=2):
        print("Reterival Begins")
        query_embed = self.embedding.embed_query(str(self.query))

        scores = [
            cosine_similarity([query_embed], item["embedding"])[0][0]
            for item in self.store
        ]
        top_k_res = sorted(
            range(len(scores)),
            key = lambda i: scores[i],
            reverse=True
        )[:k]

        top_chunks = [self.store[i]["text"] for i in top_k_res]
    
        return top_chunks
    
    def Generator(self):
        """
        retrieved_chunks = top 3 chunks returned from vector DB
        user_query       = original user question (not embedded query)
        """
        retrieved_chunks = self.Reterive(k=2)
        uq = self.query
        print("Generation Started")

        # Build context from retrieved chunks
        context = "\n\n".join(
            [f"Chunk {i+1}:\n{chunk}" for i, chunk in enumerate(retrieved_chunks)]
        )

        prompt = f"""
            You are an intelligent PDF Question Answering Assistant.

            The following text chunks were retrieved using semantic similarity from a PDF.

            Your task:
            1. Read all retrieved chunks carefully.
            2. Answer the user query ONLY from the provided chunks.
            3. If answer is available, provide a clear response.
            4. Mention page number, line number, or heading if present in chunks.
            5. If answer requires combining multiple chunks, infer carefully.
            6. If answer is not found, say:
            "The requested information is not available in the retrieved content."
            7. Do not hallucinate.

            Retrieved Content:
            {context}

            User Query:
            {uq}

            Response Format:

            Answer:
            <your answer>

            Source Reference:
            1. Chunk No: <chunk number>
            Page No: <if available>
            Line No: <if available>
            Section: <if available>

            Final Response:
            """

        response = self.model.invoke(prompt)

        return response.content


# from preprocessing import PreProcessing, QueryPreProcessing
# from prompts import Prompting
# pre = PreProcessing()
# text = pre.PDFReader("C:/Users/Nayan/Downloads/GenAIProjects/ResearchPaperExtraction_GapAnalysis/test/1-s2.0-S0160791X25000375-main.pdf")
# token = pre.Chunking(text)
# embed = pre.Embedding(token)
# ques = str(input("Please enter question: "))
# print("Question",ques)
# rag = ReteriveGenerate(store=embed, question= ques)
# gen = rag.Generator()
# print(gen)