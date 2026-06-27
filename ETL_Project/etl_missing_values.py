import pandas as pd
from sqlalchemy import create_engine

# Step 1: Extract
df = pd.read_csv("sales_missing.csv")

print("Original Data:")
print(df)

# Step 2: Transform (Handle Missing Values)

# 1️⃣ Replace missing amount with average amount
avg_amount = df["amount"].mean()
df["amount"].fillna(avg_amount, inplace=True)

# 2️⃣ Replace missing customer with 'Unknown'
df["customer"].fillna("Unknown", inplace=True)

# 3️⃣ Replace missing city with 'Not Available'
df["city"].fillna("Not Available", inplace=True)

# 4️⃣ Add new column with tax
df["amount_with_tax"] = df["amount"] * 1.10

print("\nCleaned Data:")
print(df)

# Step 3: Load into MySQL
engine = create_engine(
    "mysql+pymysql://root:root@localhost/testdb"
)

df.to_sql("sales_cleaned", con=engine,
          if_exists="replace", index=False)

print("\nETL Process Completed Successfully!")