from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Article(BaseModel):
    content : str
    comments : List[str] = []

@app.post('/article/')
def recognize_entities(article:Article, big_model: bool = False):
    return {"message": f"Reading {article.content}", "big_model": big_model}

