# Installing Libraries
import uvicorn               # For ASGI Server Type
from fastapi import FastAPI

# Creating a FastAPI Instance
app = FastAPI()


# Index Route Path
@app.get('/')
def index():
    return {'message': 'Hello! This is my First FastAPI Implementation!!!'}


# Route Path with Parameter
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to my Welcome Page': f'{name}'}


# Run the API with `uvicorn`
if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 5000)    # CLI: uvicorn Tutorial:app --reload --port 5000
