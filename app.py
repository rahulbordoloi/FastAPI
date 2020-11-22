# Installing Libraries
import uvicorn
from fastapi import FastAPI
from Schema import BankNote
import pickle
import os

# Creating a FastAPI Instance
app = FastAPI()

# Reading in the Pickle File
model = pickle.load(open('classifier.pkl', 'rb'))


# Index Route
@app.get('/')
async def index():
    return {'message': 'My First FastAPI ML Deployment Implementation!!'}


# Route Path with Parameter
@app.get('/{name}')
async def hello(name: str):
    return {'message': f'Hello, {name}!'}


# Predict Route Path with Parameter

"""
Will make a prediction from the passed JSON data and return the prediction with the confidence.
"""

@app.post('/predict')
async def predict(data: BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    predictedValue = model.predict_proba([[variance, skewness, curtosis, entropy]])[:, 1][0]
    if predictedValue < 0.5:
        prediction = "Fake Note"
    else:
        prediction = "Authentic Bank Note"
    return {
        'prediction': prediction
    }


# Run the API with `uvicorn`
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, debug = True, host = '0.0.0.0', port = port)

