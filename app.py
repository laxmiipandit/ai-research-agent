import streamlit as st
from agent.llm import research_answer

st.set_page_config(page_title="AI Research Agent", page_icon="🔍", layout="centered")

# Custom styling — baby pink & white theme
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFFFF;
    }
h1, h1 span, .stApp h1 {
    color: #D63384 !important;
    font-weight: 800 !important;
}
h3 {
    color: #D63384 !important;
}
    .stTextInput > div > div > input {
        background-color: #FFF0F5;
        border: 1.5px solid #F8BBD0;
        border-radius: 8px;
        color: #333333;
    }
    .stButton > button {
        background-color: #F8BBD0;
        color: #7A1F4C;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5em 1.5em;
    }
    .stButton > button:hover {
        background-color: #F48FB1;
        color: white;
    }
    div[data-testid="stMarkdownContainer"] p {
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("AI Research Agent")
st.write("Ask any question — I'll search the web, reason across sources, and answer with citations.")

question = st.text_input("Your question:")

if st.button("Research") and question:
    with st.spinner("Searching and reasoning..."):
        answer = research_answer(question)
    st.markdown("### Answer")
    st.write(answer)