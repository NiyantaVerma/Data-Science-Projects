import os
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from dotenv import load_dotenv

load_dotenv()

search = DuckDuckGoSearchAPIWrapper()
llm = ChatOpenAI(model="gpt-4o-mini",openai_api_key=os.getenv("OPEN_AI_API_KEY"))

tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Search the web for relevant information"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

def get_agent_response(query):
    return agent.run(query)
