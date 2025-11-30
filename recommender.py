from sentence_transformers import SentenceTransformer, util
from models import Product
import numpy as np

class SimpleRecommender:

    def __init__(self, db):
        self.db = db
        self.model = SentenceTransformer("paraphrase-MiniLM-L3-v2")
        self.products = self.db.query(Product).all()

        corpus = [
            (p.name or "") + " " + (p.description or "")
            for p in self.products
        ]

        self.embeddings = self.model.encode(corpus, convert_to_tensor=True)

    def recommend(self, query, top_k=5):
        query_emb = self.model.encode(query, convert_to_tensor=True)
        hits = util.semantic_search(query_emb, self.embeddings, top_k=top_k)[0]

        results = []
        for h in hits:
            p = self.products[h["corpus_id"]]
            results.append({
                "product": p,
                "score": float(h["score"])
            })
        return results
