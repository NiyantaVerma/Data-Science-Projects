from database import crud


def create_sessionId():
    return "123456789"


def generate_sessionId(customerId: str, session_id: str, query: str, response_text: str) -> str:


    if crud.read(customerId)!=None:
        if crud.read(sessionId)==None:
            sessionId = crud.read(customerId).sessionId
            crud.create(sessionId, customerId)
    elif crud.read(customerId)==None:
        if crud.read(sessionId)==None:
            sessionId = create_sessionId()
            crud.create(sessionId, customerId)

    crud.update(sessionId, response_text, query)
    return session_id