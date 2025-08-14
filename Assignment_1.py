#Step 1 - Plan the Data Storage

employees = {
    101 : {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102 : {'name' : 'Ram', 'age': 30, 'department' : 'finance', 'salary' : 70000}
}

#Step 2 - Define the Menu System
def main_menu():
    while True:
        print("\n----- Employee Management System -----")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            print("Thank you for using Employee Management System (EMS) exit")
            break
        else:
            print("Invalid choice. Please try again.")


#Step 3 – Add Employee Functionality

def add_employee():
    while True:
        try: 
            emp_id = int(input("Enter Employee ID : "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a new one")
            else:
                break
        except ValueError:
            print("Invalid input. Employee ID mustbe a number")
    
    name = input("Enter Employee Name: ")
    while True:
        try:
            age = int(input("Enter Employee Age: "))
            break
        except ValueError:
            print("Invalid input. Age must be a number.")
        
    department = input("Enter Employee Department: ")

    while True:
        try:
            salary = float(input('Enter Employee Salary: '))
            break
        except ValueError:
            print("Invalid input. Salary must be a number.")
    
    employees[emp_id] = {
        'name' : name,
        'age' : age,
        'department' : department,
        'salary' : salary
    }

    print(f"Employee {name} added successfully")


#Step 4 - View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
        return
    print("\n{:<10} {:<15} {:<5} {:<15} {:10}".format('Emp_ID','Name','Age','Department','Salary'))
    print("-"*55)

    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(
            emp_id, details['name'], details['age'], details['department'], details['salary']))

  
#Step 5 - Search for an Employee by ID

def search_employee():
    try:
        emp_id = int(input("Enter Employee Id to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\nEmployee Found: \nName: {emp['name']}\nAge: {emp['age']}\nDepartment: {emp['department']}\nSalary: {emp['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input.Employee Id must be a number")

#Step 6 - Exit the Program
#Already handled in main_menu() with option 4.

main_menu()








