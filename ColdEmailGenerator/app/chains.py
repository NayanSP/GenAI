import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

class Chain:
    def __init__(self):
        self.llm = ChatOpenAI(
    temperature = 0.0,
    model = 'gpt-5.4-mini'
    )
        
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
          """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """  
        )
        chain_extract = prompt_extract | self.llm
        resp = chain_extract.invoke({'page_data':cleaned_text})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(resp.content)
        
        except OutputParserException:
            raise OutputParserException('Content too big')
        
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
            Remember you are Mohan, BDE at AtliQ. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )

        chain_email = prompt_email | self.llm

        resp = chain_email.invoke({'job_description':job,
                                  'link_list':links })
        return resp.content

if __name__ == "__main__":
    print('Chain')


