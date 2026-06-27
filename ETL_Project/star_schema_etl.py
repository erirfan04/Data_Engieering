import pandas as pd
from sqlalchemy import create_engine

# MySQL connection
engine = create_engine("mysql+pymysql://root:root@localhost/testdb")

# Step 1: Load CSV
df = pd.read_csv("sales_data.csv")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# ----------------------------
# 1️⃣ Create Customer Dimension
# ----------------------------
dim_customer = df[["customer_name", "city"]].drop_duplicates().reset_index(drop=True)
dim_customer["customer_id"] = dim_customer.index + 1

# ----------------------------
# 2️⃣ Create Product Dimension
# ----------------------------
dim_product = df[["product_name", "category"]].drop_duplicates().reset_index(drop=True)
dim_product["product_id"] = dim_product.index + 1

# ----------------------------
# 3️⃣ Create Date Dimension
# ----------------------------
dim_date = df[["order_date"]].drop_duplicates().reset_index(drop=True)
dim_date["date_id"] = dim_date.index + 1
dim_date["year"] = dim_date["order_date"].dt.year
dim_date["month"] = dim_date["order_date"].dt.month
dim_date["day"] = dim_date["order_date"].dt.day

# ----------------------------
# 4️⃣ Create Fact Table
# ----------------------------

# Merge to get foreign keys
fact_sales = df.merge(dim_customer, on=["customer_name", "city"])
fact_sales = fact_sales.merge(dim_product, on=["product_name", "category"])
fact_sales = fact_sales.merge(dim_date, on="order_date")

fact_sales = fact_sales[[
    "order_id",
    "customer_id",
    "product_id",
    "date_id",
    "amount"
]]

# ----------------------------
# 5️⃣ Load into MySQL
# ----------------------------

dim_customer.to_sql("dim_customer", con=engine, if_exists="replace", index=False)
dim_product.to_sql("dim_product", con=engine, if_exists="replace", index=False)
dim_date.to_sql("dim_date", con=engine, if_exists="replace", index=False)
fact_sales.to_sql("fact_sales", con=engine, if_exists="replace", index=False)

print("Star Schema Created Successfully!")