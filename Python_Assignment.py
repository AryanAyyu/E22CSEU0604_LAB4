def sort_employee_data(employee_data, sorting_parameter):
    if sorting_parameter == 1:
        sorted_data = sorted(employee_data, key=lambda x: x[2])  # Sort by Age
    elif sorting_parameter == 2:
        sorted_data = sorted(employee_data, key=lambda x: x[1])  # Sort by Name
    elif sorting_parameter == 3:
        sorted_data = sorted(employee_data, key=lambda x: x[3])  # Sort by Salary
    else:
        print("Invalid sorting parameter")
        return
    
    return sorted_data

def main():
    
    print()
    print("Aryan Srivastava")
    print("E22CSEU0604")
    print()
    employee_data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000)
    ]

    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    sorting_parameter = int(input("Enter sorting parameter (1/2/3): "))
    sorted_employee_data = sort_employee_data(employee_data, sorting_parameter)

    if sorted_employee_data:
        print("\nSorted Employee Data:")
        for emp in sorted_employee_data:
            print(f"Employee ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Salary: {emp[3]}")

if __name__ == "__main__":
    main()