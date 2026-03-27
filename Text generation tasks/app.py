import streamlit as st
from langchain.prompts import PromptTemplate
from utils.llm import load_llm

# Load model
llm = load_llm()

# UI
st.set_page_config(page_title="Text Generator", layout="centered")
st.title("🧠 AI Text Generator (No API Key)")

user_input = st.text_area("Enter your prompt:")

# Prompt Template
template = """
You are a helpful AI assistant.
Generate a detailed response for:

{input_text}
"""

prompt = PromptTemplate(
    input_variables=["input_text"],
    template=template
)

if st.button("Generate"):
    if user_input:
        final_prompt = prompt.format(input_text=user_input)
        response = llm(final_prompt)
        st.write(response)
    else:
        st.warning("Please enter text")