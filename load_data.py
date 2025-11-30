import csv
from sqlalchemy.orm import Session
from database import engine
from models import Base, Product

Base.metadata.create_all(bind=engine)

CSV_PATH = "data/products.csv"

def import_products():
    with open(CSV_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    session = Session(bind=engine)

    for r in rows:
        product = Product(
            sku=r.get("sku"),
            name=r.get("name"),
            category=r.get("category"),
            price=float(r.get("price")) if r.get("price") else None,
            description=r.get("description"),
            image_url=r.get("image_url")  # <-- filename only
        )
        session.add(product)

    session.commit()
    session.close()
    print(f"Imported {len(rows)} products successfully!")

if __name__ == "__main__":
    import_products()
