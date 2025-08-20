"""
analysis_eda.py
----------------
This script performs a basic exploratory data analysis on the 10k sales records
dataset included in this repository. It reads the CSV file from the
`data/raw` folder, computes summary metrics by region and item type, and
produces simple bar charts for revenue by region and the top item types by
revenue.  All charts use matplotlib and do not specify any custom colours or
styles to comply with project guidelines.

To run this script, execute:

```
python src/analysis_eda.py
```

The output charts will be saved in the `reports` directory, and a markdown
summary of the results will be written to `reports/analysis_summary.md`.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data(filepath: str) -> pd.DataFrame:
    """Load the CSV file into a pandas DataFrame."""
    df = pd.read_csv(filepath)
    return df


def compute_metrics(df: pd.DataFrame):
    """Compute revenue and profit by region and revenue by item type."""
    revenue_by_region = (
        df.groupby('Region')['Total Revenue']
        .sum()
        .sort_values(ascending=False)
    )

    profit_by_region = (
        df.groupby('Region')['Total Profit']
        .sum()
        .sort_values(ascending=False)
    )

    # Average profit margin per region (profit divided by revenue)
    margin_by_region = profit_by_region / revenue_by_region

    revenue_by_item = (
        df.groupby('Item Type')['Total Revenue']
        .sum()
        .sort_values(ascending=False)
    )

    return revenue_by_region, profit_by_region, margin_by_region, revenue_by_item


def save_charts(revenue_by_region, revenue_by_item, output_dir: str):
    """Generate and save bar charts for revenue by region and top item types."""
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Chart: Revenue by Region
    plt.figure()
    revenue_by_region.plot(kind='bar')
    plt.title('Total Revenue by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    revenue_region_path = os.path.join(output_dir, 'revenue_by_region.png')
    plt.savefig(revenue_region_path)
    plt.close()

    # Chart: Top 10 Item Types by Revenue
    top_items = revenue_by_item.head(10)
    plt.figure()
    top_items.plot(kind='bar')
    plt.title('Top 10 Item Types by Total Revenue')
    plt.xlabel('Item Type')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    items_path = os.path.join(output_dir, 'top_item_types_by_revenue.png')
    plt.savefig(items_path)
    plt.close()

    return revenue_region_path, items_path


def save_summary(revenue_by_region, profit_by_region, margin_by_region, revenue_by_item, summary_path: str):
    """Write a markdown summary of the key metrics to a file."""
    lines = []
    lines.append("# Analysis Summary\n")
    lines.append("## Revenue by Region\n")
    for region, value in revenue_by_region.items():
        lines.append(f"- **{region}**: ${value:,.2f}")
    lines.append("\n## Profit by Region\n")
    for region, value in profit_by_region.items():
        lines.append(f"- **{region}**: ${value:,.2f}")
    lines.append("\n## Average Profit Margin by Region\n")
    for region, value in margin_by_region.items():
        lines.append(f"- **{region}**: {value:.2%}")
    lines.append("\n## Top 10 Item Types by Revenue\n")
    for item, value in revenue_by_item.head(10).items():
        lines.append(f"- **{item}**: ${value:,.2f}")
    with open(summary_path, 'w') as f:
        f.write('\n'.join(lines))


def main():
    data_file = os.path.join('data', 'raw', '10000_sales_records.csv')
    df = load_data(data_file)
    revenue_by_region, profit_by_region, margin_by_region, revenue_by_item = compute_metrics(df)
    # Save charts
    charts_dir = os.path.join('reports')
    save_charts(revenue_by_region, revenue_by_item, charts_dir)
    # Save summary markdown
    summary_path = os.path.join(charts_dir, 'analysis_summary.md')
    save_summary(revenue_by_region, profit_by_region, margin_by_region, revenue_by_item, summary_path)


if __name__ == '__main__':
    main()