import pandas as pd
from sqlalchemy import create_engine

# Step 1: Extract
df = pd.read_csv("sales.csv")

engine = create_engine("mysql+pymysql://root:password@localhost/testdb")

# Step 2: Load Raw Data First
df.to_sql("sales_raw", con=engine, if_exists="replace", index=False)

print("Raw Data Loaded")