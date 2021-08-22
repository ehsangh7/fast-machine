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
def recognize_entities(articles : List[Article]):
    ents = []
    response_body = []
    for article in articles:
        for comment in article.comments:
            comment.l
            doc_en = nlp_en(comment)
            for ent in doc_en.ents:
                ents.append({"text": ent.text, "label": ent.label_})
            response_body.append({"message": comment, "ents": ents})
    return response_body
