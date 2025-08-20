-- Example schema for SQLite if you prefer to create tables manually
CREATE TABLE IF NOT EXISTS transactions (
  order_id TEXT,
  order_date TEXT,
  sku TEXT,
  region TEXT,
  qty INTEGER,
  unit_price REAL,
  discount REAL,
  channel TEXT
);

CREATE TABLE IF NOT EXISTS products (
  sku TEXT PRIMARY KEY,
  product_name TEXT,
  category TEXT,
  sub_category TEXT
);

CREATE TABLE IF NOT EXISTS regions (
  region TEXT PRIMARY KEY,
  manager TEXT,
  currency TEXT
);
