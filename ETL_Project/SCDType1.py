from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:root@localhost/testdb")

with engine.begin() as conn:
    conn.execute(text("""
        UPDATE dim_customer_type1
        SET city = 'Mumbai'
        WHERE customer_id = 1;
    """))

print("SCD Type 1 Update Done")