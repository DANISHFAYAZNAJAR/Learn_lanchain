from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.llms.ollama import Ollama 
import streamlit as st 
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


## prompt 

prompt = ChatPromptTemplate.from_messages(
    [
        ("System","You are helpful assistant, response to user question"),
        ("User","question:{question}")
    ]
)


st.title("Langchain Demo with OPENAI API")
input_text = st.text_input("Search the topic you want")

llm = Ollama(model='llama2')

output_parser = StrOutputParser()

chain = prompt | llm | output_parser 

if input_text: 
    st.write(chain.invoke({'question':input_text}))
    
    
    



