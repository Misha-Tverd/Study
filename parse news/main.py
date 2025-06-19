from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import joblib
import json

app = FastAPI()

# Статичні файли
app.mount("/static", StaticFiles(directory="static"), name="static")

# Модель
model = joblib.load("output/model.joblib")
vectorizer = joblib.load("output/vectorizer.joblib")

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
    return {"title": title, "predicted_category": pred}
