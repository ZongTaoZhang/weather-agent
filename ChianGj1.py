import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from AllTools import getWeather
from langchain_ollama import ChatOllama

load_dotenv()
llm=ChatOllama(
    model="qwen3.5:2b",
    base_url="http://localhost:11434"
)
agent = create_agent(
    model=llm,
    tools=[getWeather]
)
print("调用")
response = agent.invoke({
    "messages" :[
    {"role":"user","content":"今天成都天气怎么样?"}
]}
)
content = response["messages"][-1].content
print(content)