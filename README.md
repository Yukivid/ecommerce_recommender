# 🛒 AI-Powered E-commerce Product Recommender

An intelligent **E-commerce Product Recommendation System** built with **FastAPI** and **Google Gemini LLM**, capable of recommending products based on user queries and explaining *why* each product is suggested — just like a smart shopping assistant 🧠✨.

---

## 🚀 Features

✅ **FastAPI Backend** – Lightweight & fast API server  
✅ **LLM-Powered Explanations** – Gemini 2.5 Flash generates natural, helpful reasoning  
✅ **Semantic Product Matching** – `sentence-transformers` for meaning-based similarity  
✅ **SQLite Database Integration** – Product data stored locally via SQLAlchemy  
✅ **Modern Frontend UI** – Animated, responsive glass-style design  
✅ **Render Cloud Deployment Ready**  

---

## 🧠 Tech Stack

| Layer | Tools |
|-------|-------|
| **Backend** | FastAPI |
| **AI Model** | Google Gemini 2.5 Flash |
| **Database** | SQLite + SQLAlchemy |
| **Embeddings** | all-MiniLM-L6-v2 |
| **Frontend** | HTML + CSS + JS |
| **Hosting** | Render Cloud |

---

## ⚙️ Setup & Run Locally

```bash
# 1️⃣ Clone the repo
git clone https://github.com/Yukivid/ecommerce_recommender.git
cd ecommerce_recommender

# 2️⃣ Create & activate virtual env
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add your Gemini API key
echo GOOGLE_API_KEY=your_gemini_key_here > .env

# 5️⃣ Load product data
python load_data.py

# 6️⃣ Run server
uvicorn main:app --reload
