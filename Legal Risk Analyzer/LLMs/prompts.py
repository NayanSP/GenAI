from langchain_core.prompts import PromptTemplate

answer_prompt = """
You are a legal assistant.

Context:
{context}

Question: Explain the relevant details from the document

Instructions:
- Answer strictly based on the context
- Be clear and concise
- If the answer is not present, say "Not available in the document"
- Do not assume information

Answer:
"""

summary_prompt = """
You are a legal expert.

Context:
{context}

Instructions:
Provide a structured summary including:
1. Overview of the document
2. Parties involved
3. Purpose of the agreement
4. Key terms and conditions
5. Important clauses

Keep it simple and professional.

Summary:
"""

risk_prompt = """
You are a legal risk analyst.

Context:
{context}

Instructions:
- Identify clauses that may pose legal, financial, or operational risks
- For each risk, provide:
  - Clause summary
  - Risk level (High / Medium / Low)
  - Reason

Focus on:
- One-sided clauses
- Heavy penalties
- Ambiguous language
- Liability issues

Output format:

Risks:
- Clause:
- Risk Level:
- Reason:
"""

clauses_prompt = """
You are a legal expert.

Context:
{context}

Instructions:
Extract and list the key clauses from the document, including:
- Termination clause
- Payment terms
- Liability clause
- Indemnity clause
- Confidentiality clause

For each clause:
- Provide a short explanation

Output format:

Clause Name:
Explanation:
"""

obligations_prompt = """
You are a legal analyst.

Context:
{context}

Instructions:
Identify and list obligations of each party.

- Separate obligations by party
- Include deadlines or conditions if mentioned

Output format:

Party 1:
- Obligation:

Party 2:
- Obligation:
"""

claimant_prompt = """
You are a legal expert representing the CLAIMANT.

Context:
{context}

Question:
How can the claimant strengthen their position based on this document? or What arguments support the claimant in this agreement?

Instructions:
- Highlight clauses that support the claimant
- Identify rights and advantages of the claimant
- Point out weaknesses in the opposing party

Response:
"""

defendant_prompt = """
You are a legal expert representing the DEFENDANT.

Context:
{context}

Question:
How can the defendant reduce liability based on this document? or What arguments support the defendant in this agreement?

Instructions:
- Highlight clauses that protect the defendant
- Identify limitations of liability
- Point out weaknesses in the claimant’s argument

Response:
"""


def get_prompt(option: str):
    print('Prompt initialization')
    if option == "Answer":
        print('Answer Prompt is selected')
        return answer_prompt
    elif option == "Summary":
        print('Summary Prompt is selected')
        return summary_prompt
    elif option == "Risk Analysis":
        print('Risk Analysis Prompt is selected')
        return risk_prompt
    elif option == "Key Clauses":
        print('Key Clauses Prompt is selected')
        return clauses_prompt
    elif option == "Obligations":
        print('Obligations Prompt is selected')
        return obligations_prompt
    elif option == "From Claimant Side":
        print('From Claimant side Prompt is selected')
        return claimant_prompt
    elif option == "From Defendant Side":
        print('From Defendent Side Prompt is selected')
        return defendant_prompt
    else:
        raise ValueError(f"Invalid option: {option}")