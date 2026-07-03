import calculate, validate
class Employee:
    def __init__(self, name, department, base_salary, rating):
        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.rating = rating

def new_emp():
    emp_name = input("Enter Employee Name: ")
    emp_department = input("Enter Employee Department: ")
    emp_base_salary = validate.get_salary()
    emp_rating = validate.get_rating()
    return Employee(emp_name, emp_department, emp_base_salary, emp_rating)

def display(emp, bonus, tax, net_salary):
    print
    print("Basic  Information".center(50,'-'))
    print(" Employee Name: ",emp.name)
    print(" Department: ",emp.department)
    print("#" * 50)
    print("\n")
    print("Component".ljust(24)+"Amount")
    print("-" * 50)
    print("Base Salary".ljust(24)+f"[${emp.base_salary:,}]")
    print("Performance Rating".ljust(24)+f"{emp.rating}")
    print("Bonus".ljust(24)+f"+[${bonus}]")
    print("Tax Deductions".ljust(24)+f"-[${tax}]\n")
    print(f"Net Payable Salary: $[{net_salary}]\n\n")
    print("Notes & Approvals")
    print("Status: Processed")
    print("HR Remarks: ",end="")
    if emp.rating == 5: print("(Excellent performance)")
    elif emp.rating in [3,4]: print("(Good performance)")
    else: print("(Needs improvement)")



def main_hr_app():
    emp = new_emp() # initial data

    # Calculations to get bonus amount and tax
    bonus = calculate.calculate_bonus(emp.base_salary, emp.rating)
    tax = calculate.calculate_tax(bonus + emp.base_salary)
    net_salary = emp.base_salary + bonus - tax


    # Display
    display(emp,bonus,tax,net_salary)

    
main_hr_app()

