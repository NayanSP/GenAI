from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser


# =========================
# 1. ANSWER
# =========================
class AnswerOutput(BaseModel):
    answer: str = Field(description="Final answer to the user's question")


answer_parser = PydanticOutputParser(pydantic_object=AnswerOutput)


# =========================
# 2. SUMMARY
# =========================
class SummaryOutput(BaseModel):
    overview: str
    parties: List[str]
    purpose: str
    key_points: List[str]


summary_parser = PydanticOutputParser(pydantic_object=SummaryOutput)


# =========================
# 3. RISK ANALYSIS
# =========================
class RiskItem(BaseModel):
    clause: str
    risk_level: str  # High / Medium / Low
    reason: str


class RiskOutput(BaseModel):
    risks: List[RiskItem]


risk_parser = PydanticOutputParser(pydantic_object=RiskOutput)


# =========================
# 4. KEY CLAUSES
# =========================
class ClauseItem(BaseModel):
    clause_name: str
    explanation: str


class ClauseOutput(BaseModel):
    clauses: List[ClauseItem]


clause_parser = PydanticOutputParser(pydantic_object=ClauseOutput)


# =========================
# 5. OBLIGATIONS
# =========================
class ObligationOutput(BaseModel):
    party_1: List[str]
    party_2: List[str]


obligation_parser = PydanticOutputParser(pydantic_object=ObligationOutput)


# =========================
# 6. CLAIMANT SIDE
# =========================
class ClaimantOutput(BaseModel):
    arguments: List[str]
    advantages: List[str]
    weaknesses_in_defendant: List[str]


claimant_parser = PydanticOutputParser(pydantic_object=ClaimantOutput)


# =========================
# 7. DEFENDANT SIDE
# =========================
class DefendantOutput(BaseModel):
    arguments: List[str]
    protections: List[str]
    weaknesses_in_claimant: List[str]


defendant_parser = PydanticOutputParser(pydantic_object=DefendantOutput)


# =========================
# PARSER SELECTOR
# =========================
def get_parser(option: str):
    print('Ouput Parser Initialization')
    if option == "Answer":
        return answer_parser
    elif option == "Summary":
        return summary_parser
    elif option == "Risk Analysis":
        return risk_parser
    elif option == "Key Clauses":
        return clause_parser
    elif option == "Obligations":
        return obligation_parser
    elif option == "From Claimant Side":
        return claimant_parser
    elif option == "From Defendant Side":
        return defendant_parser
    else:
        raise ValueError(f"Invalid option: {option}")