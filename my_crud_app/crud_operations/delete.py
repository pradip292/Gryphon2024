# crud_operations/delete.py
import psycopg2
from db_config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def delete_employee(employee_id):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
        conn.commit()  # Commit the transaction
        print("Employee deleted successfully")
    except Exception as e:
        print(f"Error deleting employee: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Database connection closed")
