from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI()

prompt = PromptTemplate(template="You are an HR in the ZackMack company. The manager will provide you the job title and years of experience needed to hire new employee. Your task is to create a Job description for this role. the job title is {position} and years of experience is {yoe}")
chain = prompt | llm
ip1 = input("please enter the job position: ")
ip2 = str(input("Please enter no of years needed for the position: "))
print("------------------------------------------------------------")
res = chain.invoke({'position':ip1, 'yoe':ip2})
print(res.content)
print("------------------------------------------------------------")
query = PromptTemplate(template="""
You are an expert interviwer, based on the Job description {res}.
Now you need to create a questionaire for the interview round. each round will have atleast 10 questions
Your task in to create questions for 2 techincal round and 1 HR round as follows:
2 techincal round:
    1. first techincal round will ask simple but distinct question realted to skills needed for this job
    2. it will also have few code level questions if necessary
    3. the second techincal round, will ask question in more details with case study included
    4. the coding will be realted to case study
1 HR round:
    1. the HR round will be of simple personal and professional question
""")
print("------------------------------------------------------------")
chain2 = query | llm
res1 = chain2.invoke({'res':res.content})
print(res1.content)
print("------------------------------------------------------------")
select = PromptTemplate(template="""Once the candidate is selected for the job role, you need to ask his notice period, if notice period is serving, any offer in hand and salary expecation.
                        then create a offer letter based on the data provided.
                        notice period: {np}
                        serving notice period: {snp}
                        offer in hand: {oh}
                        salary expectation:{se}
""")
np = str(input("Please enter the notice period in days?"))
snp = str(input("Are you serving notice period?"))
oh = str(input("Are you holding offer in hand?"))
se = str(input("enter your salary expecation?"))
chain2 = select | llm
res3 = chain2.invoke({'np':np,'snp':snp,'oh':oh,'se':se})
print(res3.content)
print("------------------------------------------------------------")