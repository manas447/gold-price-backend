# Gold Price Prediction API

This is a backend API built with FastAPI that predicts gold prices based on financial indicators.

## Endpoints

- `GET /` – Test the server
- `POST /predict` – Get gold price prediction

### Example input:
```json
{
  "SPX": 2781.0,
  "USO": 12.0,
  "SLV": 15.0,
  "EUR_USD": 1.12
}
```

### Output:
```json
{
  "predicted_price": 1275.23
}
```
