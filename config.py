import os

if os.environ["OPENAI_API_KEY"]:
    from langchain_openai import ChatOpenAI
    default_langchain_model = ChatOpenAI(model="gpt-4o", temperature=0)