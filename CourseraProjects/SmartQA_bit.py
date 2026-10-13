"""
Section 1 Project: Smart Q & A bot
A production-ready question-answering bot with structured output
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv
from langsmith import traceable, Client
load_dotenv()
import os

class QAResponse(BaseModel):
    answer: str  = Field(..., description="The answer to the user's question")
    confidence: str = Field(..., description="confidence level: high, medium, low")
    reasoning: str = Field(..., description="The reasoning behind the answer provided")
    follow_up_questions : List[str] = Field(..., description="A list of follow-up questions relatedd to the topic",
                                            default_factory=list)
    sources_needed: bool = Field(default=False,description="Indicates whether sources are needed for the answer"
                                 )

class SmartQABot:
    def __init__(self, model:str="gpt-4o-mini", temperature:float=0.0):
        self.model = ChatOpenAI(model="gpt-4o-mini", temperature=0.2).with_structured_output(QAResponse)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system",
             """You are a knowledgeable assistant that provided detailed answer to user questions.
             Your guidelines:
             - Answerr questions accuretly and concisely
             - be honest about uncertainty -set confidence to low if unsure
             - provided clear reasoning for your answers
             - suggest relvant follow-up questions
             - indicate if external soruces would help
             always respond with accurate, helpful information
             """             ),
             ("human","{question}")
        ])
        self.chain = self.prompt | self.model

    @traceable(name = "ask_question", run_type="chain")
    def ask(self, question: str) -> QAResponse:
        try:
            response = self.chain.invoke(question = question)
            return response
        except Exception as e:
            return QAResponse(answer = "I am sorry, I could not proceed with your request",
            confidence = "low",
            reasoning = str(e),
            follow_up_questions=['Could you please try again later?'],
            sources_needed = True,)

    @traceable(name = "ask_batch", run_type="chain")
    def ask_batch(self, question: List[str]) -> List[QAResponse]:
        """Ask multiple question in parallel"""
        inputs = [{"question":q} for q in question]
        return self.chain.batch(inputs)

def demo_QA_bot():
    bot = SmartQABot()

    question = [
        "What is the capital of France?",
        "Explain probability?",
        "How does photosynthesis work?"
    ]

    for q in question:
        resp = bot.ask(q)
        print(f"Question: {q}")
        print(f"Answer: {resp.answer}")
        print(f"Confidence: {resp.confidence}")
        print(f"Reasoning: {resp.reasoning}")
        print(f"follow-up questions: {resp.follow_up_questions}")
        print(f"sources needed: {resp.sources_needed}")
        print("-"*60)

if __name__ == "__main__":
    demo_QA_bot()
        

        