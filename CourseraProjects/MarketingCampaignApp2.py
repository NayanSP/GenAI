
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    PromptTemplate,
    FewShotPromptTemplate
)
from langchain_core.example_selectors import (
    LengthBasedExampleSelector
)

load_dotenv()


examples = [
    {
        "query": "What is a mobile?",
        "answer": "A mobile is a magical device that fits in your pocket!"
    },
    {
        "query": "What are your dreams?",
        "answer": "I dream of colorful adventures, ice cream parties, and having a pet dragon!"
    },
    {
        "query": "What are your ambitions?",
        "answer": "I want to spread laughter, bake cookies, and build amazing blanket forts!"
    },
    {
        "query": "What happens when you get sick?",
        "answer": "I feel tired and need rest, care, and lots of cuddles."
    },
    {
        "query": "How much do you love your dad?",
        "answer": "I love my dad to the moon and back!"
    },
    {
        "query": "Tell me about your friend?",
        "answer": "A friend makes life happier by sharing, listening, and playing together."
    },
    {
        "query": "What does math mean to you?",
        "answer": "Math is a fun puzzle that helps me count, measure, and solve problems!"
    },
    {
        "query": "What is your fear?",
        "answer": "Sometimes I fear thunderstorms, but I feel safer with comfort and support."
    }
]


def get_llm_response(query, age_option, tasktype_option, word_limit):

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7
    )

    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template="Question: {query}\nResponse: {answer}"
    )

    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200
    )

    prefix = """
    You are a marketing assistant writing for the following audience:
    {template_ageoption}.

    Your task is to {template_tasktype_option}.
    Use the examples as guidance for tone and style.
    Adapt your response to the user's input.
    """

    suffix = """
    User input: {template_userInput}

    Write a response within approximately {word_limit} words.
    Response:
    """

    prompt_template = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=[
            "template_userInput",
            "template_ageoption",
            "template_tasktype_option",
            "word_limit"
        ],
        example_separator="\n\n"
    )

    prompt = prompt_template.format(
        template_userInput=query,
        template_ageoption=age_option,
        template_tasktype_option=tasktype_option,
        word_limit=word_limit
    )

    with st.expander("View formatted prompt"):
        st.text(prompt)

    response = llm.invoke(prompt)

    return response.content


# Streamlit UI

st.set_page_config(
    page_title="Marketing Tool",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Hey, how can I help you?")

form_input = st.text_area("Enter text", height=200)

tasktype_option = st.selectbox(
    "Please select the action to be performed?",
    (
        "Write a sales copy",
        "Create a tweet",
        "Write a product description"
    )
)

age_option = st.selectbox(
    "For which age group?",
    ("Kid", "Adult", "Senior Citizen")
)

number_of_words = st.slider(
    "Word limit",
    1, 200, 25
)

if st.button("Generate"):
    if not form_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Generating response..."):
            try:
                result = get_llm_response(
                    form_input,
                    age_option,
                    tasktype_option,
                    number_of_words
                )
                st.subheader("Generated content")
                st.write(result)

            except Exception as e:
                st.error(f"Failed to generate content: {e}")
