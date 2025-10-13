# 🛍️ AI-Powered E-commerce Product Recommender

The **AI-Powered E-commerce Product Recommender** is an intelligent system built using **FastAPI** and **Google Gemini LLM**.  
It analyzes user queries and recommends relevant products along with human-like explanations — just like a smart shopping assistant 🧠✨.

---

## 🎥 Demo Video

🎬 **Watch the full demo here:**  
👉 [Click to Watch on Google Drive](https://drive.google.com/file/d/1N-N-iivWSEEthxyNUYz6_RwtRK-_YRCu/view?usp=sharing)

Or view the embedded demo below 👇

https://github.com/Yukivid/ecommerce_recommender/assets/demo_video.mp4


---


## 🌟 Features

- 🤖 **AI-Generated Explanations**  
  Uses **Google Gemini 2.5 Flash** to explain *why* each product is recommended.

- 🔍 **Smart Product Matching**  
  Employs semantic similarity using **sentence-transformers (all-MiniLM-L6-v2)**.

- 🗃️ **Database Integration**  
  Stores product data (name, category, price, description) in **SQLite** using SQLAlchemy ORM.

- 💻 **Modern Responsive Frontend**  
  Built with **HTML + CSS + JS**, featuring a glassmorphic, animated design.

- 🖼️ **Fallback Image System**  
  Displays a default image automatically when a product image is unavailable.

- ☁️ **Render Cloud Ready**  
  Fully optimized for **Render Cloud** deployment with environment variable support.

---

## 🧠 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | FastAPI (Python 3.10+) |
| **AI Model** | Google Gemini 2.5 Flash |
| **Embeddings** | sentence-transformers (all-MiniLM-L6-v2) |
| **Database** | SQLite + SQLAlchemy ORM |
| **Hosting** | Render Cloud |

---

## 📁 Project Structure

| File / Folder | Description |
|----------------|--------------|
| `main.py` | FastAPI application entry point |
| `recommender.py` | Core logic for product similarity and retrieval |
| `llm_explainer.py` | Handles Gemini AI API for generating explanations |
| `models.py` | Defines SQLAlchemy ORM product model |
| `database.py` | Initializes SQLite database session |
| `templates/index.html` | Frontend interface |
| `static/images/` | Product and default images |
| `data/products.csv` | Contains 250+ product entries |

---

## 🔍 Methodology

### 🧠 Step 1 — Query Understanding  
The user’s search query (e.g., “laptop”, “mobile”, “headphones”) is embedded using **sentence-transformers** to capture semantic meaning.

### 🔎 Step 2 — Product Matching  
The recommender computes similarity scores between the query and product embeddings, retrieving the top matches.

### 💬 Step 3 — Explanation Generation  
Each recommendation is passed to **Gemini AI**, which generates a natural language explanation describing why it’s a good fit.

### 🎨 Step 4 — Frontend Display  
All results are displayed in a clean, card-based layout with product images, price, category, and explanations.

---

## 📊 Example Output

| Product | Category | Price | AI Explanation |
|----------|-----------|--------|----------------|
| Apple iPhone 15 | Mobile | ₹79,999 | “A flagship phone with A16 Bionic chip, ideal for performance and camera quality.” |
| Samsung Galaxy S24 | Mobile | ₹74,999 | “A premium Android with AMOLED 120Hz display and advanced AI camera features.” |
| HP Pavilion Laptop | Laptop | ₹59,999 | “A reliable choice for work and entertainment with strong performance.” |

---

## ⚙️ Getting Started

### 🧩 Prerequisites

- Python 3.10 or higher  
- Google Gemini API Key  
- Internet connection

---

### 🧰 Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Yukivid/ecommerce_recommender.git
cd ecommerce_recommender

# 2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Set your Gemini API key
set GOOGLE_API_KEY=your_gemini_api_key_here  # Windows
# export GOOGLE_API_KEY=your_gemini_api_key_here  # Mac/Linux

# 5️⃣ Run the application
uvicorn main:app --reload

## 🚀 Future Enhancements

🧩 Add category tabs (Mobiles, Laptops, Cameras, etc.)
🔍 Integrate vector databases like ChromaDB or Pinecone
💬 Implement personalized recommendations using user profiles
🌗 Add dark mode toggle
📱 Mobile UI optimization

## ✨ Developed by Deepesh Raj A.Y

If you found this helpful, leave a ⭐ on GitHub!
