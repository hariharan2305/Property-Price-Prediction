import uvicorn
from fastapi import FastAPI
from PropertyVariables import ProperyPricePred
import numpy as np 
import pickle 
import pandas as pd 
import joblib 

# 1.  Creating the App object
PropertyPricePredApp = FastAPI()

# 2.  Load the model from disk
fileName = 'model/property_price_prediction_voting.sav'
loaded_model = joblib.load(fileName)

# pickle_in = open("model/regressor.pkl","rb")
# loaded_model = pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
@PropertyPricePredApp.get('/')
def index():
    return {'message': 'Hello, World!'}

# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted price with the confidence
@PropertyPricePredApp.post('/predict')
def predict_price(data: ProperyPricePred):
    data = data.dict()
    print(data)
    data = pd.DataFrame([data])
    print(data.head())

    prediction = loaded_model.predict(data)
    print(str(prediction))
    return str(prediction)
