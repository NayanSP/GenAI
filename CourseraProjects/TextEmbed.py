import streamlit as st
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
embed = OpenAIEmbeddings()
llm = ChatOpenAI()

#text = "Hi Buddy"
#print(embed.embed_query(text))

col = ['school','college','car','bike','cycle','apple','fruits','oranges','education']
df = pd.DataFrame()
df['Words'] = col
print(df)
df['embed'] = df['Words'].apply(lambda x: embed.embed_query(x))

text = 'mango'
text_embed = embed.embed_query(text)

from sklearn.metrics.pairwise import cosine_similarity

df['similar'] = df['embed'].apply(lambda x: cosine_similarity(x, text_embed))
print(f'checking similarity of {text} with the list')
print(df)