"""Build a local SQLite database from CSVs in data/raw.
Run: python src/build_sqlite.py
"""
import os
import pandas as pd
import sqlalchemy as sa

BASE = os.path.dirname(os.path.dirname(__file__))
RAW = os.path.join(BASE, "data", "raw")
DB  = os.path.join(BASE, "data", "processed", "sales.db")

engine = sa.create_engine(f"sqlite:///{DB}")

files = {
    "transactions": "transactions.csv",
    "products": "products.csv",
    "regions": "regions.csv",
}

for table, fname in files.items():
    path = os.path.join(RAW, fname)
    if not os.path.exists(path):
        print(f"[skip] {path} not found")
        continue
    df = pd.read_csv(path)
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"[ok] wrote table {table} -> {DB}")

print("Done. If all tables were present, you can now query data with sql/ scripts.")
