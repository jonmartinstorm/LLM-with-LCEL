from dotenv import dotenv_values
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

config = dotenv_values()

model = ChatOllama(
    model="llama3.1",
    temperature=0,
)

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

parser = StrOutputParser()

if __name__ == "__main__":
    chain = model | parser
    print(chain.invoke(messages))