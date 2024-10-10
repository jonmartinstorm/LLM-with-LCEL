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

if __name__ == "__main__":
    chain = prompt_template | model | parser
    print(chain.invoke({"language": "norwegian", "text": "Hi, how are you?"}))