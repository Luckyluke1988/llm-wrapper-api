from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

nlp_pipeline = pipeline(
    "zero-shot-classification",
    model="MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33"
)

@app.get("/version")
async def root():
    return {"0.1.0"}


@app.get("/zero-shot-classification")
async def say_hello(text: str, labels: str):
    candidate_labels = [label.strip() for label in labels.split(",")]
    result = nlp_pipeline(text, candidate_labels=candidate_labels)
    return {"result": result}