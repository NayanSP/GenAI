import langchain_openai 
from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv
load_dotenv()

llm_model = ChatOpenAI( model="gpt-4.1",)

if __name__ == "__main__":
    response = llm_model.invoke("What are the ingredient used in making cake")
    print(response.content)