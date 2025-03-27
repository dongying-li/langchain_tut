import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


model = init_chat_model("gpt-4o-mini", model_provider="openai")
output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")

chain = prompt | model | output_parser

result = chain.invoke({"topic": "minions"})
print(result)
