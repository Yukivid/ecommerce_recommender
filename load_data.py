import csv
from database import SessionLocal, engine
from models import Base, Product

Base.metadata.create_all(bind=engine)
db = SessionLocal()

with open("data/products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        db.add(Product(
            name=row["name"],
            category=row["category"],
            price=float(row["price"]),
            description=row["description"]
        ))
db.commit()
db.close()

print("✅ Imported all 250+ products successfully!")
