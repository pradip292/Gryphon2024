# main.py
from crud_operations.create import create_employee
from crud_operations.read import read_employees
from crud_operations.update import update_employee
from crud_operations.delete import delete_employee

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Create an employee")
        print("2. Read all employees")
        print("3. Update an employee")
        print("4. Delete an employee")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            department = input("Enter department: ")
            create_employee(name, age, department)
        elif choice == '2':
            read_employees()
        elif choice == '3':
            employee_id = input("Enter employee ID: ")
            name = input("Enter new name (or press Enter to skip): ")
            age = input("Enter new age (or press Enter to skip): ")
            department = input("Enter new department (or press Enter to skip): ")
            update_employee(employee_id, name if name else None, age if age else None, department if department else None)
        elif choice == '4':
            employee_id = input("Enter employee ID: ")
            delete_employee(employee_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
