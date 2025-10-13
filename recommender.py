from database import SessionLocal
from models import Product
from sentence_transformers import SentenceTransformer, util

class SimpleRecommender:
    def __init__(self):
        self.db = SessionLocal()
        self.products = self.db.query(Product).all()
        self.model = None
        self.embeddings = None

    def _ensure_model_loaded(self):
        """Load the model only once (lazy loading to save memory)."""
        if self.model is None:
            # Use smaller, memory-efficient model for Render/local
            self.model = SentenceTransformer("paraphrase-MiniLM-L3-v2")
            self.embeddings = self.model.encode(
                [p.name for p in self.products],
                convert_to_tensor=True
            )

    def recommend(self, query: str, top_k: int = 4):
        self._ensure_model_loaded()
        query = query.strip().lower()

        # Try exact or category match first
        filtered = [
            p for p in self.products
            if query in p.name.lower() or query in p.category.lower()
        ]
        if filtered:
            return [
                {
                    "name": p.name,
                    "category": p.category,
                    "price": p.price,
                    "description": p.description
                }
                for p in filtered[:4]
            ]

        # Otherwise use semantic similarity
        query_emb = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_emb, self.embeddings)[0]
        top_results = scores.topk(min(top_k, len(self.products))).indices

        return [
            {
                "name": self.products[i].name,
                "category": self.products[i].category,
                "price": self.products[i].price,
                "description": self.products[i].description
            }
            for i in top_results
        ]
