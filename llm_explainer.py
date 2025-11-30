import os
import google.generativeai as genai
from database import SessionLocal
from models import Explanation
from datetime import datetime

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain(product, query, db):
    # Check cache
    cached = (
        db.query(Explanation)
        .filter_by(product_id=product.id, query=query)
        .order_by(Explanation.created_at.desc())
        .first()
    )
    if cached:
        return cached.explanation

    prompt = f"""
    Explain in simple words why the product '{product.name}' is recommended 
    for the search query '{query}'.
    Product description: {product.description}
    Category: {product.category}
    """

    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
        explanation_text = response.text
    except Exception:
        explanation_text = "This product matches your search based on category and description."

    record = Explanation(
        product_id=product.id,
        query=query,
        explanation=explanation_text
    )
    db.add(record)
    db.commit()

    return explanation_text
