# crud_operations/read.py
import psycopg2
from db_config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def read_employees():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error reading employees: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
