import sqlite3
from sqlite3 import Error
 
class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
 
    def connect(self):
        """Create a database connection to a SQLite database"""
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"Connected to SQLite database: {self.db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
 
    def create_table(self):
        """Create a table in the SQLite database"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                             (id INTEGER PRIMARY KEY,
                              name TEXT NOT NULL,
                              position TEXT NOT NULL,
                              salary REAL)''')
            print("Table 'employees' created successfully")
        except Error as e:
            print(f"Error creating table: {e}")
 
    def insert_employee(self, name, position, salary):
        """Insert a new employee into the employees table"""
        sql = ''' INSERT INTO employees(name,position,salary)
                  VALUES(?,?,?) '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (name, position, salary))
            self.conn.commit()
            print(f"Employee {name} inserted successfully")
        except Error as e:
            print(f"Error inserting employee: {e}")
 
    def read_employees(self):
        """Query all rows in the employees table"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error reading employees: {e}")
 
    def update_employee(self, id, name, position, salary):
        """Update an employee's details"""
        sql = ''' UPDATE employees
                  SET name = ?,
                      position = ?,
                      salary = ?
                  WHERE id = ? '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (name, position, salary, id))
            self.conn.commit()
            print(f"Employee with id {id} updated successfully")
        except Error as e:
            print(f"Error updating employee: {e}")
 
    def delete_employee(self, id):
        """Delete an employee by id"""
        sql = 'DELETE FROM employees WHERE id=?'
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (id,))
            self.conn.commit()
            print(f"Employee with id {id} deleted successfully")
        except Error as e:
            print(f"Error deleting employee: {e}")
 
    def transaction_example(self):
        """Example of transaction management with COMMIT and ROLLBACK"""
        try:
            self.conn.execute("BEGIN TRANSACTION")
            self.insert_employee("John Doe", "Manager", 75000)
            self.insert_employee("Jane Smith", "Developer", 65000)
            # Simulating an error
            if False:  # Change to True to simulate an error and see ROLLBACK in action
                raise Exception("Simulated error")
            self.conn.commit()
            print("Transaction committed successfully")
        except Exception as e:
            self.conn.rollback()
            print(f"Transaction rolled back due to error: {e}")
 
    def close_connection(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            print("Database connection closed")
 
def main():
    db_manager = DatabaseManager("employees.db")
 
    # Connect to the database
    db_manager.connect()
 
    # Create table
    db_manager.create_table()
 
    # Insert employees
    db_manager.insert_employee("Alice Johnson", "HR Manager", 60000)
    db_manager.insert_employee("Bob Williams", "Software Engineer", 70000)
 
    # Read all employees
    print("\nAll employees:")
    db_manager.read_employees()
 
    # Update an employee
    db_manager.update_employee(1, "Alice Johnson", "Senior HR Manager", 65000)
 
    # Delete an employee
    db_manager.delete_employee(2)
 
    # Read all employees after modifications
    print("\nEmployees after modifications:")
    db_manager.read_employees()
 
    # Transaction example
    db_manager.transaction_example()
 
    # Close the connection
    db_manager.close_connection()
 
if __name__ == "__main__":
    main()