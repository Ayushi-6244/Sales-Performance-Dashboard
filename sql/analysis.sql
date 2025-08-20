-- Starter analysis queries
-- Revenue by month
SELECT strftime('%Y-%m', order_date) AS ym,
       SUM(qty * unit_price * (1.0 - COALESCE(discount,0))) AS revenue
FROM transactions
GROUP BY ym
ORDER BY ym;

-- Top 10 SKUs by revenue
SELECT t.sku,
       p.product_name,
       SUM(qty * unit_price * (1.0 - COALESCE(discount,0))) AS revenue
FROM transactions t
LEFT JOIN products p USING(sku)
GROUP BY t.sku, p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- Revenue leakage candidates (high discount)
SELECT t.sku,
       p.product_name,
       AVG(discount) AS avg_discount,
       SUM(qty) AS units
FROM transactions t
LEFT JOIN products p USING(sku)
GROUP BY t.sku, p.product_name
HAVING avg_discount > 0.25 AND units > 100
ORDER BY avg_discount DESC;
