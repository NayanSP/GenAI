import streamlit as st
from utils import generate_script
from dotenv import load_dotenv
load_dotenv()

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#FFFFFF;
    }
</style>""", unsafe_allow_html=True)

st.title("Youtube Script Writing tool")
st.sidebar.title(":Youtube:")

prompt = st.text_input("Please provide the topic of the video",key='prompt')
video_length = st.text_input("Expected video lenght in Minutes", key="video_length")
creativity = st.slider("Word limit - Low to Hight(0 to 1)",0.0,1.0,0.1, step = 0.1)

submit = st.button("Generate")

if submit:
    search_result,title,script = generate_script(prompt, video_length, creativity)
    st.success('Hope you like it')
    st.subheader("title:")
    st.write(title)

    st.subheader("Your video script:")
    st.write(script)

    st.subheader('Check out:')
    with st.expander('show me:'):
        st.info(search_result)
else:
    st.error("Opss! Please try once again")