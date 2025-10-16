from fastapi import FastAPI, HTTPException
from schemas import GoldInput
from model import predict_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Gold Price Prediction API"}

@app.post("/predict")
def predict(data: GoldInput):
    try:
        features = [data.SPX, data.USO, data.SLV, data.EUR_USD]
        result = predict_price(features)
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed")
    return {"predicted_price": result}
