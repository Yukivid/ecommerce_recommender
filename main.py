from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from database import SessionLocal
from models import Product
from recommender import SimpleRecommender
from llm_explainer import explain_recommendation
import os

# Initialize FastAPI app
app = FastAPI(title="AI E-commerce Recommender")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Initialize recommender
recommender = SimpleRecommender()


# 🏠 Root endpoint - loads the HTML UI
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 🧠 Recommendation endpoint
@app.get("/recommendations")
def get_recommendations(query: str = Query(..., description="User search query")):
    """
    Returns product recommendation and LLM explanation.
    Example: /recommendations?query=iphone
    """
    try:
        recs = recommender.recommend(query, top_k=1)
        for r in recs:
            r["explanation"] = explain_recommendation(r["name"], query)
        return {"query": query, "results": recs}
    except Exception as e:
        return {"error": str(e)}


# 🧾 All Products endpoint
@app.get("/products")
def list_products():
    """
    Returns all products stored in the database.
    Example: /products
    """
    db = SessionLocal()
    items = db.query(Product).all()
    return [
        {
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "description": p.description,
        }
        for p in items
    ]


# 🌐 Startup message
@app.on_event("startup")
def startup_message():
    print("🚀 E-commerce Recommender API started successfully!")


# Run manually using: uvicorn main:app --reload
