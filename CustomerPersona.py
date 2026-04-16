# this project will create ads based on the customer demographics and company allocated budget
# Provide the genere, product details, product name, budget and any discount you want to provide

import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(
    model = 'gpt-5.1',
    temperature= 1.8,
)

from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, EmailStr, Field

class Output(TypedDict):
    genere: str = Field(description='Enter the genere of the product'),
    age_group: str = Field(description='Enter the age group if provided in the statement, if not then consider it is for above 15 years')
    product_details:str = Field(description='Enter the details of the product'),
    product_name:str = Field(description='Enter the name of the product'),
    budget:float = Field(description='Enter the budget of the product, it should be present in $ with round off 2 demcimal point'),
    discount:float = Field(description='Enter the discount of the product, it should be in $ with round off 2 decimal point, if not present assign value 0'),
    output_ad:str = Field(description='Provide the model output with ads details'),
    output_line:str = Field(description='Provide a catchy line for the product')

op_model = llm.with_structured_output(Output)

op = op_model.invoke("I want to design an advertise for the 10-18 years childern who are intersted in badminton. " \
"the product details are my badmintion has good string strength which provide strongs smash and light weight as it made from lightest material" \
"product name is Zondu Hit" \
"the busget for this advertisment and product is $1M and discount for first 100 buyer is 20percent off" \
"your task is to create a advertisement and catchy line to attract for this product ")

print(op)


op1 = op_model.invoke("create a advertisement for insurance compnay who is dealing in term insurance. they are pro vide large coverance till $10M with affordable premoum. if purchase for family, they provide more benefits to first nominee with huge amount. if you are" \
"first buyer of insurance you will receive 5 percent discount for first 3 years. the claim settlement is done in first 3 hours of filling. provide gifts for your marriage anniversary, for your child born and any achivement you make in this lifetime." \
"the age group is mostly working class from 20-50 years. you have been task to create ad for this compnay." \
"the line should be so catchy that the customer should be attracted to it. ")
print(op1)

