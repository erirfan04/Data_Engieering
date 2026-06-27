from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:root@localhost/testdb")

with engine.begin() as conn:
    conn.execute(text("""
        UPDATE dim_customer_type3
        SET previous_city = city,
            city = 'Mumbai'
        WHERE customer_id = 1;
    """))

print("SCD Type 3 Update Done")