from fastapi import FastAPI, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from models import Product
from recommender import SimpleRecommender
from llm_explainer import explain_recommendation
import os

# Initialize FastAPI app
app = FastAPI(title="AI E-commerce Recommender")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (images, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Initialize recommender
recommender = SimpleRecommender()

# 🏠 Homepage route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 🧠 Recommendation API — returns products matching the query
@app.get("/recommendations")
def get_recommendations(query: str = Query(..., description="Search for a product or category")):
    """
    Return product recommendations based on similarity or category.
    Example: /recommendations?query=mobile
    """
    try:
        db = SessionLocal()
        query_lower = query.lower()

        # Step 1️⃣: Get recommendations from recommender
        recs = recommender.recommend(query, top_k=10)

        # Step 2️⃣: Fallback — direct DB match if recommender returns few results
        if not recs or len(recs) < 5:
            db_results = db.query(Product).filter(
                Product.category.ilike(f"%{query_lower}%") |
                Product.name.ilike(f"%{query_lower}%") |
                Product.description.ilike(f"%{query_lower}%")
            ).limit(20).all()

            recs = [
                {
                    "name": p.name,
                    "category": p.category,
                    "price": p.price,
                    "description": p.description,
                    "explanation": ""
                }
                for p in db_results
            ]

        # Step 3️⃣: Generate explanations for each unique product (avoid duplicates)
        unique_names = set()
        final_recs = []

        for r in recs:
            if r["name"] not in unique_names:
                unique_names.add(r["name"])
                if not r.get("explanation"):
                    try:
                        r["explanation"] = explain_recommendation(r["name"], query)
                    except Exception:
                        r["explanation"] = "This product matches your search preference!"
                final_recs.append(r)

        db.close()
        return {"query": query, "results": final_recs}

    except Exception as e:
        return {"error": str(e)}


# 🧾 View all products in DB
@app.get("/products")
def list_products():
    """
    Returns all products stored in the database.
    Example: /products
    """
    db = SessionLocal()
    items = db.query(Product).all()
    db.close()
    return [
        {
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "description": p.description
        }
        for p in items
    ]


# 🌐 Startup log
@app.on_event("startup")
def startup_message():
    print("🚀 AI E-commerce Recommender API running successfully!")


# Run this app using: uvicorn main:app --reload
