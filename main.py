from dotenv import dotenv_values
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

config = dotenv_values()

model = ChatOllama(
    model="llama3.2:3b-instruct-fp16", 
    temperature=0,
)

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

if __name__ == "__main__":
    print(model.invoke(messages))