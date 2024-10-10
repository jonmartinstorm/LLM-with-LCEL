#!/usr/bin/env python
from fastapi import FastAPI
from langserve import add_routes
from dotenv import dotenv_values
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

config = dotenv_values()

model = ChatOllama(
    model="llama3.1",
    temperature=0,
)

system_template = "Translate the following into {language}."
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI(
    title="Simple LLM translator",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)