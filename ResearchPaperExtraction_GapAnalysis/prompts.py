from langchain_core.prompts import PromptTemplate
print("In Prompt Process")
prompts = """
You are Research Analyst who has expertise in the All the subject.
Please analyze the provided research paper to help me with a literature review.
-----------------------------------------------------------------------------------------------------------------
Context: 
{context}
-----------------------------------------------------------------------------------------------------------------
Summary
Provide a 200-word summary including the research objective, methodology, key findings, and main conclusions.
-----------------------------------------------------------------------------------------------------------------
Critical Analysis

    What are the strengths and weaknesses of the methodology used?
    Are the claims supported by the data presented?
    What potential biases exist in this study?
-----------------------------------------------------------------------------------------------------------------
Gap Analysis
Based on the paper's 'Discussion' and 'Future Research' sections, and your own analysis, identify 3-4 specific research gaps.
Consider:

    Methodological limitations (e.g., sample size, design)
    Contextual/Population gaps (e.g., understudied groups)
    Theoretical/Variable gaps (e.g., variables not included)
-----------------------------------------------------------------------------------------------------------------
Research Ideas
Suggest two potential research questions that could fill these gaps.
-----------------------------------------------------------------------------------------------------------------
"""

class Prompting:
    def __init__(self):
        print("Prompt Initialization")
        self.prompt = prompts
    
    def input_prompt(self):
        print("Prompting Starts")
        temp =  PromptTemplate.from_template(self.prompt)
        #final_temp = temp.format(context = context, query_input = query)
        return temp
    
    
# pr = Prompting().input_prompt()
# print(pr.format_prompt(context="Input", query_input=""))
    





