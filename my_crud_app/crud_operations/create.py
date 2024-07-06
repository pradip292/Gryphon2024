# crud_operations/create.py
import psycopg2
from db_config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def create_employee(name, age, department):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO employees (name, age, department)
            VALUES (%s, %s, %s)
        """, (name, age, department))
        conn.commit()  # Commit the transaction
        print("Employee added successfully")
    except Exception as e:
        print(f"Error creating employee: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Database connection closed")
