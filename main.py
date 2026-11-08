# Project: Business Sales Intelligence Report

import pandas as pd
import numpy as np

import os
os.makedirs("output", exist_ok=True)

# 1. Load Dataset

data = {
    "OrderID": [
        101, 102, 103, 104, 105, 106,
        107, 108, 109, 110, 111, 112,
        113, 114, 115, 116, 117, 118,
        119, 120, 121, 122, 123, 124,
        125, 126, 127, 128, 129, 129
    ],
    "OrderDate": [
        "2026-10-01", "2026-10-02", "2026/10/05", "2026-10-06", "2026-10-06", "2026-10-10",
        "2026/10/12", "2026-10-14", "invalid_date", "2026-10-15", "2026-10-18", "2026-10-20",
        "2026/10/22", "2026-10-25", "2026-10-28", "2026-11-01", "2026-11-03", "2026-11-05",
        "2026-11-07", "2026-11-09", "2026-11-12", "2026-11-14", "2026-11-16", "2026-11-18",
        "2026-11-20", "2026-11-22", "2026-11-24", "2026-11-26", "2026-11-28", "2026-11-30"
    ],
    "Product": [
        "Laptop ", "Phone", "Laptop", "PHONE", "Tablet", "Headphones",
        "Smartwatch", "Monitor", "Keyboard", "Mouse", "Printer", "Router",
        "Speaker", "Phone", "Tablet", "Laptop", "Phone", "Headphones",
        "Monitor", "Keyboard", "Mouse", "Smartwatch", "Printer", "Router",
        "Speaker", "Laptop", "Tablet", "Phone", "Monitor", "Keyboard"
    ],
    "Category": [
        "Electronics", "Mobile", "Electronics", "Mobile", "Electronics", "Accessories",
        "Accessories", "Electronics", "Accessories", "Accessories", "Office Supply", "Networking",
        "Accessories", "Mobile", "Electronics", "Electronics", "Mobile", "Accessories",
        "Electronics", "Accessories", "Accessories", "Accessories", "Office Supply", "Networking",
        "Accessories", "Electronics", "Electronics", "Mobile", "Electronics", "Accessories"
    ],
    "City": [
        "Kasur", "Lahore", "KASUR", "Lahore", None, "Karachi",
        "lahore", "Islamabad", "Kasur", "Karachi", "Lahore", "Faisalabad",
        "Multan", "Karachi", "Lahore", "Kasur", "LAHORE", "Karachi",
        "Islamabad", "Kasur", "Multan", "Lahore", "Faisalabad", "Karachi",
        "Kasur", "Lahore", "Islamabad", "Karachi", "Multan", "Lahore"
    ],
    "Quantity": [
        1, 2, 1, -1, 3, 5,
        2, 1, 10, 2, 1, 1,
        4, 3, 5, 2, 1, 4,
        2, 10, 3, 2, 1, 2,
        5, 1, 3, 2, 1, 4
    ],
    "UnitPrice": [
        120000, 45000, 120000, 45000, 25000, 6000,
        15000, 35000, 4000, 2500, 18000, 8500,
        12000, 45000, None, 125000, 48000, 6500,
        36000, 4200, 2700, 16000, 19000, 9000,
        13000, 118000, 26000, 46000, 37000, 4500
    ],
    "Discount": [
        10, None, 0.15, 0, 5, 0.20,
        None, 12, -5, 0, 8, 0.10,
        0, 25, 0.15, 5, 0.10, 0.15,
        8, 0, 5, 0.10, 12, 0.05,
        0, 10, 0.15, 5, 0.10, 0.20
    ]
}

df = pd.DataFrame(data)

# 2. Inspect Dataset

print("Dataset Shape:", df.shape)

print("\nDataset Information:")
df.info()

print("\nDataset Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Records:", df.duplicated().sum())
print("Duplicate OrderIDs:", df["OrderID"].duplicated().sum())

# Store Initial Dataset Information

initial_rows = len(df)
missing_before = int(df.isna().sum().sum())
duplicate_records = int(df.duplicated().sum())
duplicate_order_ids = int(df["OrderID"].duplicated().sum())

# 3. Remove Duplicate Records

df = df.drop_duplicates().copy()
df = df.drop_duplicates(subset=["OrderID"], keep="first").copy()

# 4. Standardize Text Columns

df["Product"] = df["Product"].astype("string").str.strip().str.title()
df["Category"] = df["Category"].astype("string").str.strip().str.title()
df["City"] = df["City"].astype("string").str.strip().str.title()

df["Product"] = df["Product"].fillna("Unknown Product")
df["Category"] = df["Category"].fillna("Unknown Category")
df["City"] = df["City"].fillna("Unknown")

# 5. Clean Quantity

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

invalid_quantity = df["Quantity"].isna() | (df["Quantity"] <= 0)
invalid_quantity_count = int(invalid_quantity.sum())

print("\nInvalid Quantity Records:")
print(df[invalid_quantity])

# Remove Zero and Negative Quantities

df = df[df["Quantity"] > 0].copy()

# Fill Missing Quantity

quantity_median = df.loc[df["Quantity"] > 0, "Quantity"].median()
df["Quantity"] = df["Quantity"].fillna(quantity_median)

# Remove Zero and Negative Quantities
df = df[df["Quantity"] > 0].copy()

# 6. Clean UnitPrice

df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

invalid_price = df["UnitPrice"].isna() | (df["UnitPrice"] <= 0)
invalid_price_count = int(invalid_price.sum())

df.loc[df["UnitPrice"] <= 0, "UnitPrice"] = np.nan

# Calculate Product-wise Median

product_median = df.groupby("Product")["UnitPrice"].transform("median")

# Calculate Global Median

global_unit_price_median = df["UnitPrice"].median()

# Fill Missing Prices

df["UnitPrice"] = df["UnitPrice"].fillna(product_median)
df["UnitPrice"] = df["UnitPrice"].fillna(global_unit_price_median)

# 7. Clean Discount

df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")

# Convert Percentage Values into Decimal Values

df["Discount"] = np.where(df["Discount"] > 1, df["Discount"] / 100, df["Discount"])

invalid_discount = ~df["Discount"].between(0, 1)
invalid_discount_count = int(invalid_discount.sum())

print("\nInvalid Discount Records:")
print(df[invalid_discount])

df.loc[invalid_discount, "Discount"] = np.nan

# Fill Missing Discounts

df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df["Discount"] = df["Discount"].fillna(0)

# 8. Clean OrderDate

df["OrderDate"] = df["OrderDate"].astype("string").str.replace("/", "-", regex=False)
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")

invalid_dates = int(df["OrderDate"].isna().sum())

print("\nInvalid or Missing Dates:", invalid_dates)

# 9. Create Revenue Columns

df["GrossRevenue"] = df["Quantity"] * df["UnitPrice"]
df["NetRevenue"] = df["GrossRevenue"] * (1 - df["Discount"])

# 10. Validate Cleaned Dataset

print("\n========== Data Validation ==========")

assert (df["Quantity"] > 0).all(), "Invalid Quantity Found"
assert (df["UnitPrice"] > 0).all(), "Invalid UnitPrice Found"
assert df["Discount"].between(0, 1).all(), "Invalid Discount Found"
assert df["Product"].notna().all(), "Missing Product Found"
assert df["City"].notna().all(), "Missing City Found"
assert not df["OrderID"].duplicated().any(), "Duplicate OrderID Found"

print("Data Validation Status: PASSED")

# 11. Create Data Quality Report

final_rows = len(df)
missing_after = int(df.isna().sum().sum())

quality_report = {
    "Rows Before Cleaning": initial_rows,
    "Rows After Cleaning": final_rows,
    "Rows Removed": initial_rows - final_rows,
    "Duplicate Records Found": duplicate_records,
    "Duplicate OrderIDs Found": duplicate_order_ids,
    "Invalid Quantities Found": invalid_quantity_count,
    "Invalid Prices Found": invalid_price_count,
    "Invalid Discounts Found": invalid_discount_count,
    "Invalid or Missing Dates": invalid_dates,
    "Missing Values Before Cleaning": missing_before,
    "Missing Values After Cleaning": missing_after,
    "Data Validation": "PASSED"
}

quality_report_df = pd.DataFrame(list(quality_report.items()), columns=["Metric", "Value"])

print("\n========== Data Quality Report ==========")
print(quality_report_df)

# 12. Calculate Revenue Statistics

total_revenue = df["NetRevenue"].sum()
total_orders = df["OrderID"].nunique()
average_revenue = total_revenue / total_orders

print("\nTotal Revenue:", total_revenue)
print("Total Orders:", total_orders)
print(f"Average Revenue per Order: {average_revenue:.2f}")

print("\nRevenue Statistics:")
print(df["NetRevenue"].describe())

# 13. Find Total Revenue by Product

product_revenue = df.groupby("Product")["NetRevenue"].sum().sort_values(ascending=False)

print("\nTotal Revenue by Product:")
print(product_revenue)

# 14. Find Total Revenue by City

city_revenue = df.groupby("City")["NetRevenue"].sum().sort_values(ascending=False)

print("\nTotal Revenue by City:")
print(city_revenue)

# 15. Find Average Order Revenue by Category

category_revenue = df.groupby("Category")["NetRevenue"].mean().sort_values(ascending=False)

print("\nAverage Order Revenue by Category:")
print(category_revenue)

# 16. Create Product-by-City Pivot Table

pivot_revenue = pd.pivot_table(df, values="NetRevenue", index="Product", columns="City", aggfunc="sum", fill_value=0)

print("\nProduct-by-City Pivot Table:")
print(pivot_revenue)

# 17. Analyze Monthly Revenue

monthly_df = df[df["OrderDate"].notna()].copy()
monthly_df["Month"] = monthly_df["OrderDate"].dt.to_period("M").astype("string")
monthly_revenue = monthly_df.groupby("Month")["NetRevenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)

# 18. Calculate Correlations

correlation_matrix = df[["Quantity", "UnitPrice", "Discount", "NetRevenue"]].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# 19. Detect Revenue Outliers using IQR Method

Q1 = df["NetRevenue"].quantile(0.25)
Q3 = df["NetRevenue"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df["NetRevenue"] < lower_limit) | (df["NetRevenue"] > upper_limit)]

print("\nNetRevenue Outliers:")
print(outliers)

# 20. Final Business Sales Summary

print("\n========== Final Business Sales Summary ==========")

print("\nTotal Orders:", total_orders)
print("Total Net Revenue:", round(total_revenue, 2))
print("Average Revenue per Order:", round(average_revenue, 2))
print("Highest Revenue Product:", product_revenue.idxmax())
print("Highest Revenue City:", city_revenue.idxmax())
print("Highest Revenue Category:", df.groupby("Category")["NetRevenue"].sum().idxmax())
print("Highest Revenue Month:", monthly_revenue.idxmax() if len(monthly_revenue) > 0 else "No valid dates")
print("Records with Invalid Dates:", invalid_dates)
print("Potential Revenue Outliers:", len(outliers))

# 21. Export Cleaned Dataset and Reports

df.to_csv("output/clean_sales_data.csv", index=False)
quality_report_df.to_csv("output/data_quality_report.csv", index=False)
product_revenue.to_csv("output/product_revenue_report.csv")
city_revenue.to_csv("output/city_revenue_report.csv")
monthly_revenue.to_csv("output/monthly_revenue_report.csv")
pivot_revenue.to_csv("output/product_city_revenue_report.csv")

print("\n========== Project Execution Complete ==========")
print("Cleaned dataset exported successfully.")
print("Data quality report exported successfully.")
print("Business analysis reports exported successfully.")
