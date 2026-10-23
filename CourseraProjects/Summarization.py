
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationSummaryMemory
from streamlit_chat import message

load_dotenv()

st.set_page_config(
    page_title="ChatGPT Clone",
    page_icon="💬"
)

if "conversation" not in st.session_state:
    st.session_state.conversation = None

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown(
    "<h1 style='text-align: center;'>How can I assist you?</h1>",
    unsafe_allow_html=True
)

st.sidebar.title("Chat Options")


def get_response(user_input):
    if st.session_state.conversation is None:
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.0
        )

        memory = ConversationSummaryMemory(llm=llm)

        st.session_state.conversation = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=True
        )

    return st.session_state.conversation.predict(input=user_input)


if st.sidebar.button("Summarize conversation"):
    conversation = st.session_state.conversation

    if conversation is None:
        st.sidebar.info("Start a conversation first.")
    else:
        summary = conversation.memory.buffer
        st.sidebar.write("### Conversation Summary")
        st.sidebar.write(summary or "No summary available yet.")


with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_area("Your question goes here:")
    submit = st.form_submit_button("Send")

if submit:
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        try:
            with st.spinner("Generating response..."):
                response = get_response(user_input)

            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

        except Exception as e:
            st.error(f"Error generating response: {e}")

# Render the full conversation after every rerun
for chat in st.session_state.messages:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])
