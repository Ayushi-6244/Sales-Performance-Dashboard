# Sales Performance Dashboard

## Business Problem
Sales leaders need clear visibility into revenue performance, discounting behavior, and product-level profitability across regions.  
This project analyzes sales transaction data to identify revenue leakage, underperforming SKUs, and seasonal trends to support better pricing, promotion, and inventory decisions.

---

## Dataset
- ~10,000 simulated sales transactions
- Dimensions: Region, Product, Category, Date
- Measures: Revenue, Quantity Sold, Discount %, Profit

---

## Key Business Questions
- Which regions and products drive revenue but hurt profitability?
- Where is excessive discounting reducing margins?
- How does seasonality impact sales performance?
- Which SKUs should be optimized, promoted, or reviewed?

---

## Approach
1. Cleaned and validated transactional sales data
2. Created core KPIs: Revenue, Profit, Margin %, Discount %
3. Analyzed trends by region, category, product, and time
4. Designed an interactive dashboard for quick business decision-making

---

## Key Insights
- Identified high-revenue SKUs with low margins caused by aggressive discounting
- Found consistent underperformance in specific regions requiring pricing review
- Surfaced seasonal demand patterns useful for inventory and promotion planning

---

## Business Impact
- Supports pricing and discount optimization decisions
- Helps leadership identify revenue leakage areas
- Provides a single, easy-to-use view of sales performance

---

## Dashboard Preview
Screenshots of key dashboard views are available in the `/screenshots` folder:
- Overall Sales Performance
- Region-wise Revenue & Margin
- Product / SKU Performance Analysis

---

## Tools & Technologies
Python | SQL | Tableau / Power BI | Data Visualization

---

## How to Use This Dashboard
- Filter by region to compare revenue and margin performance
- Drill down by product or SKU to identify discount-heavy items
- Use time filters to analyze seasonal sales trends

---

## Assumptions & Limitations
- Dataset is simulated for learning purposes
- Profit calculations assume a static cost structure
- Insights should be validated with real business data before implementation
