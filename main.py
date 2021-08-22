from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import spacy

nlp_en = spacy.load("en_core_web_sm")

app = FastAPI()

class Article(BaseModel):
    content : str
    comments : List[str] = []

@app.post('/article/')
def recognize_entities(article:Article, big_model: bool = False):
    doc_en = nlp_en(article.content)
    ents = []
    for ent in doc_en.ents:
        ents.append({"text": ent.text, "label": ent.label_})
    return {"message": article.content, "ents": ents, "big_model": big_model}
