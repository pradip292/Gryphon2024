# crud_operations/update.py
import psycopg2
from db_config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def update_employee(employee_id, name=None, age=None, department=None):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        
        if name:
            cur.execute("""
                UPDATE employees
                SET name = %s
                WHERE id = %s
            """, (name, employee_id))
        
        if age:
            cur.execute("""
                UPDATE employees
                SET age = %s
                WHERE id = %s
            """, (age, employee_id))
        
        if department:
            cur.execute("""
                UPDATE employees
                SET department = %s
                WHERE id = %s
            """, (department, employee_id))
        
        conn.commit()  # Commit the transaction
        print("Employee updated successfully")
    except Exception as e:
        print(f"Error updating employee: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Database connection closed")
