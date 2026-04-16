from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

class RetrieverClass:
    print('Retriever initialization')

    def __init__(self, dir = 'chroma_db'):
        print('Retriever begins')
        self.embed = OpenAIEmbeddings(model="text-embedding-3-large",)
        self.vector_db = Chroma(persist_directory=dir, embedding_function=self.embed)
    
    def get_documents(self, query, k=5):
        retrieve = self.vector_db.as_retriever(search_kwargs = {"k":k})
        docs = retrieve.invoke(query)
        return docs