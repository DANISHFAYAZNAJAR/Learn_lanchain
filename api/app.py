from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langserve import add_routes
import uvicorn 
import os 


from langchain_community.llms.ollama import Ollama 

from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


app = FastAPI(
    title='LANGCAHIN SERVER',
    version='1.0',
    description='A simple api server'
)


add_routes(
    app,
    ChatOpenAI(),
    path='/openai'
)


model  = ChatOpenAI() 

llm = Ollama(model='llama2')

prompt1 = ChatPromptTemplate.from_messages(
    [
        ('system','You are assistant, write me an assay given by user'),
        ('user','Topic : {topic}')
    ]
)

prompt2 = ChatPromptTemplate.from_messages(
    [
        ('system','You are assistant, write me an poem given by user'),
        ('user','Topic : {topic}')
    ]
)



add_routes(
    app,
    prompt1| model,
    path='/essay'
)

add_routes(
    app,
    prompt2|llm, 
    path='/poem'
)


if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8000)
    
    