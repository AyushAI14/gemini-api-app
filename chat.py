from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

# API KEY IS LOADED ---------------
load_dotenv()
GEMINI_API=os.getenv('GEMINI_API')
genai.configure(api_key=GEMINI_API)

# defining models 
model_name = 'gemini-2.5-pro'
model = genai.GenerativeModel(model_name)
chat = model.start_chat(history=[])

def userInput(question):
    response = model.generate_content(question)
    return response

# initialing streamlit app 
st.set_page_config(page_title='Gemini Tut Project')
st.header(f'Me Chatting with {model_name}')

input = st.text_input('Input : ',key='input')
submit = st.button('Ask Anything')

if input and submit:
    response = userInput(input)
    st.header('Gemini Reponse : ')
    for txt in response:
        st.write(txt.text)

    #appending the history of the chat
    with open('history.txt' , 'a') as f:
        f.write(f'Me: {input} \n\nGemini: {response.text} \n\ntotal_token_count: {response._result.usage_metadata.total_token_count} \n\nmodel_version: {response._result.model_version}\n\n-----------------------------------------------------------------\n\n')

