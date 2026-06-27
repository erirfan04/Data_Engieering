import pandas as pd
from sqlalchemy import create_engine, text

# Step 1: Create MySQL connection
engine = create_engine(
    "mysql+pymysql://root:root@localhost/testdb"
)

# Step 2: Load CSV
df = pd.read_csv("sales.csv")

# Step 3: LOAD (ELT - Load first)
df.to_sql("sales_raw", con=engine,
          if_exists="replace", index=False)

print("Raw data loaded")

# Step 4: TRANSFORM inside MySQL
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE sales_elt AS
        SELECT 
            order_id,
            customer,
            amount,
            amount * 1.10 AS amount_with_tax,
            city
        FROM sales_raw
        WHERE city = 'Delhi';
    """))

print("ELT Transformation Done")