from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import PyPDF2

# API 
load_dotenv()
GEMINI_API = os.getenv('GEMINI_API')
genai.configure(api_key=GEMINI_API)

# Model setup
model_name = 'gemini-2.0-flash-lite'
model = genai.GenerativeModel(model_name)

# Initialize session state for history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  

def userInput(question, pdf):
    if question != '':
        content = [question] + pdf
        response = model.generate_content(content)
    else:
        response = model.generate_content(pdf)
    return response

# Streamlit UI
st.set_page_config(page_title='Gemini Project')
st.header(f"Gemini Chat With Pdf on {model_name}")

input_question = st.text_input("Input Prompt: ", key="input")
uploaded_files = st.file_uploader("Choose PDF(s)...", type=["pdf"], accept_multiple_files=True)

pdf_content = []
if uploaded_files:
    for pdf in uploaded_files:
        content = PyPDF2.PdfReader(pdf)
        text = ''
        for page in content.pages:
            text += page.extract_text() or ""
        pdf_content.append(text)

if st.button('Ask Anything'):
    response = userInput(input_question, pdf_content)
    st.session_state.chat_history.append((input_question, response.text))

# chat history 
st.subheader("Conversation")
for i, (q, a) in enumerate(st.session_state.chat_history, start=1):
    st.markdown(f"<span style='font-size:25px; font-weight:bold;'>Me :</span> {q}", unsafe_allow_html=True)
    st.markdown(f"<span style='font-size:25px; font-weight:bold;'>Gemini :</span> {a}", unsafe_allow_html=True)

