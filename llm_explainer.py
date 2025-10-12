import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_recommendation(product_name: str, user_query: str):
    """
    Generate a short explanation using Gemini 2.5 Flash.
    """
    prompt = f"""
    The user searched for "{user_query}".
    In 1–2 short, natural sentences, explain why "{product_name}" is a great recommendation.
    Be helpful, friendly, and specific.
    """

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)
        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "No explanation generated."
    except Exception as e:
        return f"(Explanation unavailable: {e})"
