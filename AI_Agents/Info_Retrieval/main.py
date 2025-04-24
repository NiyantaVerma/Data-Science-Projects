from fastapi import FastAPI
from pydantic import BaseModel
from agent import get_agent_response
from logger import log_interaction
app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/ask")
def ask_agent(input: QueryInput):
    result = get_agent_response(input.query)
    log_interaction(input.query, result)
    return {"result": result}