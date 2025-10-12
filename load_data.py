import csv
from database import SessionLocal, engine, Base
from models import Product

Base.metadata.create_all(bind=engine)
db = SessionLocal()

with open("data/products.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = Product(
            name=row["name"],
            category=row["category"],
            price=float(row["price"]),
            description=row.get("description", "")
        )
        db.add(product)

db.commit()
db.close()
print("✅ Products loaded into database!")
