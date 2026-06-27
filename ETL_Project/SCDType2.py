from sqlalchemy import create_engine, text
from datetime import date

engine = create_engine("mysql+pymysql://root:root@localhost/testdb")

today = date.today()

with engine.begin() as conn:
    # Expire old record
    conn.execute(text("""
        UPDATE dim_customer_type2
        SET end_date = :today,
            is_current = 0
        WHERE customer_id = 1
        AND is_current = 1;
    """), {"today": today})

    # Insert new record
    conn.execute(text("""
        INSERT INTO dim_customer_type2
        (customer_id, name, city, start_date, end_date, is_current)
        VALUES (1, 'Amit', 'Dubai', :today, NULL, 1);
    """), {"today": today})

print("SCD Type 2 Update Done")