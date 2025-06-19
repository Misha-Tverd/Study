from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pathlib import Path
from fastapi.responses import HTMLResponse, FileResponse
import joblib
import json

app = FastAPI()

# Load model and vectorizer once
model = joblib.load("output/model.joblib")
vectorizer = joblib.load("output/vectorizer.joblib")

# Load news.json
with open("output/news.json", encoding="utf-8") as f:
    news_data = json.load(f)

@app.get("/", response_class=HTMLResponse)
def serve_html():
    return FileResponse("static/index.html")

@app.get("/news")
def get_news():
    return news_data

@app.post("/predict")
async def predict_category(request: Request):
    data = await request.json()
    title = data.get("title")

    if not title:
        return JSONResponse(content={"error": "No title provided"}, status_code=400)

    vec = vectorizer.transform([title])
    pred = model.predict(vec)[0]
