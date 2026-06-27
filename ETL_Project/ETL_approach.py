import pandas as pd
from sqlalchemy import create_engine

# Step 1: Extract
df = pd.read_csv("sales.csv")

# Step 2: Transform (Before Loading)
# Example: Create total amount with 10% tax
df["amount_with_tax"] = df["amount"] * 1.10

# Filter only Delhi data
df_delhi = df[df["city"] == "Delhi"]

# Step 3: Load into MySQL
engine = create_engine("mysql+pymysql://root:root@localhost/testdb")

df_delhi.to_sql("sales_etl", con=engine, if_exists="replace", index=False)

print("ETL Process Completed")