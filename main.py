from fastapi import FastAPI
from app.schemas import GoldInput
from app.model import predict_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Gold Price Prediction API"}

@app.post("/predict")
def predict(data: GoldInput):
    features = [data.SPX, data.USO, data.SLV, data.EUR_USD]
    result = predict_price(features)
    return {"predicted_price": result}
