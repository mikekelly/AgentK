import os
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

default_model_temperature = int(os.getenv("DEFAULT_MODEL_TEMPERATURE", "0"))
default_model_provider = os.getenv("DEFAULT_MODEL_PROVIDER", "OPENAI").upper()
default_model_name = os.getenv("DEFAULT_MODEL_NAME", "gpt-4o")

match default_model_provider:
    case "OPENAI":
        default_langchain_model = ChatOpenAI(model_name=default_model_name, temperature=default_model_temperature)
    case "ANTHROPIC":
        default_langchain_model = ChatAnthropic(model_name=default_model_name, temperature=default_model_temperature)