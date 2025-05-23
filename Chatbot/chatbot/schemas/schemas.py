from pydantic import BaseModel

class UserRequest(BaseModel):
    query: str
    sessionId: str
    customerId: str
    lang: str

class ChatbotResponse(BaseModel):
    response: str
    sessionId: str
