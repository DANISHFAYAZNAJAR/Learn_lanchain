import requests
import streamlit as st 

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json = {"input":{'topic':input_text}})
    
    return response.json()['output']['content']
def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
    json = {"input":{'topic':input_text}})
    
    return response.json()['output']


st.title('langchain dmeo with api')
input_text = st.text_input("write an essay on  anything")
input_text2 = st.text_input("write an poem on  anything")


if input_text:
    st.write(get_openai_response(input_text))
    
if input_text:
    st.write(get_ollama_response(input_text2))