from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from database import get_db
from recommender import SimpleRecommender
from llm_explainer import explain
from models import Product
from sqlalchemy.orm import Session

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/products")
def products(db: Session = Depends(get_db)):
    all_products = db.query(Product).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "image_url": p.image_url,
        }
        for p in all_products
    ]

@app.get("/recommendations")
def recommendations(query: str, db: Session = Depends(get_db)):
    recommender = SimpleRecommender(db)
    results = recommender.recommend(query)

    output = []
    for r in results:
        p = r["product"]
        explanation = explain(p, query, db)
        output.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "category": p.category,
            "image_url": p.image_url,
            "score": r["score"],
            "explanation": explanation,
        })

    return JSONResponse(output)
