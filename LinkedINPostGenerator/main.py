import streamlit as st
from few_shots import Few_Shot_Posts
from post_generate import generate_post

def main():
    st.title("LinkedIN Post Generator")
    col1, col2 = st.columns(2)
    fs = Few_Shot_Posts()
    with col1:
        select_tag = st.selectbox("Title", options=fs.get_tags())
    
    with col2:
        select_length = st.selectbox("Length", options=['Short','Medium', 'Long'])
    
    if st.button('Generate'):
        post = generate_post(select_length, select_tag)
        st.write(f"Generated post for Length: {select_length} and Tags: {select_tag}")
        st.write(post)

if __name__ == "__main__":
    main()