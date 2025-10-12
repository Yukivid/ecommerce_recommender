from database import SessionLocal
from models import Product
from sentence_transformers import SentenceTransformer, util

class SimpleRecommender:
    def __init__(self):
        self.db = SessionLocal()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.products = self.db.query(Product).all()
        self.embeddings = self.model.encode([p.name for p in self.products], convert_to_tensor=True)

    def recommend(self, query, top_k=1):
        query = query.strip().lower()

        # Try exact match first
        for p in self.products:
            if query in p.name.lower():
                return [{
                    "name": p.name,
                    "category": p.category,
                    "price": p.price,
                    "description": p.description
                }]

        # Otherwise, fall back to semantic top 1
        query_emb = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_emb, self.embeddings)[0]
        best_idx = int(scores.argmax())
        p = self.products[best_idx]
        return [{
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "description": p.description
        }]
