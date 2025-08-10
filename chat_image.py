from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
from PIL import Image

# API KEY IS LOADED ---------------
load_dotenv()
GEMINI_API=os.getenv('GEMINI_API')
genai.configure(api_key=GEMINI_API)

# defining models 
model_name = 'gemini-2.0-flash-lite'
model = genai.GenerativeModel(model_name)
chat = model.start_chat(history=[])

def userInput(question,image):
    if question != '':
        content = [question]+image
        response = model.generate_content(content)
    else:
        response = model.generate_content(image)
    return response

# initialing streamlit app 
st.set_page_config(page_title='Gemini Project')
st.header(f'Me Chatting with {model_name}')


st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"],accept_multiple_files=True)
image = []
if uploaded_file is not None:
    for img in uploaded_file:
        imag = Image.open(img)
        image.append(imag)
        # st.image(imag, caption="Uploaded Image.", width=200)

submit=st.button('Ask Anything')
if submit:
    response = userInput(input,image)
    st.subheader('Gemini Response')
    st.write(response.text)

    

