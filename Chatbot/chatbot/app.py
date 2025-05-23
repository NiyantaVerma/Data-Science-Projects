import os
import uuid

# FastApi Dependencies
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from utils.dependency import get_dependencies

# Data Input Output to API check
from schemas.schemas import ChatbotResponse, UserRequest

# Functions needed
from services.chatbot_service import generate_response
from services.sessionId_track import generate_sessionId

# Starting API app
app = FastAPI()

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify allowed origins like ["http://localhost"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

##################################
# FrontEnd for Testing of Chatbot
from fastapi.templating import Jinja2Templates 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

template = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return template.TemplateResponse("index.html", {"request":request})
##################################

# # Import and include routers
# from app.routes.chatbot import chatbot_router
# app.include_router(chatbot_router, prefix="/chatbot", dependencies=[Depends(get_dependencies)])

# /chatbot
@app.post("/chatbot/response", response_model=ChatbotResponse)
def chatbot_response(request: UserRequest, dependencies: dict = Depends(get_dependencies)):
    response_text = generate_response(request.query, dependencies, request.lang)
    # sessionId = generate_sessionId(request.customer_id, request.session_id, request.query, response_text)
    return ChatbotResponse(response=response_text, sessionId=request.sessionId)