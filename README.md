# Corporate Talent & Payroll Management System

A structural, modular Python program that simulates a corporate HR and payroll backend system. This project demonstrates clean code practices, strict input validation, and modular architecture.

## Project Structure
The project is strictly split into modular components to ensure high maintainability and clean code architecture:
- `main.py`: The core runtime application and controller that orchestrates the workflow.
- `calculate.py`: Contains the logic for calculating bonuses and progressive tax deductions.
- `validate.py`: Handles continuous user input validation via robust exception handling.

## Installation & Setup

1. Make sure you have **Python 3.13** installed on your system.
2. Clone this repository or download the source code files.
3. Place all the files (`main.py`, `calculate.py`, `validate.py`) into the same directory.
4. Open your terminal or command prompt, navigate to the project directory, and execute the following command:
```bash
python main.py
```

## Example Run
Here is a full demonstration of how the system safely intercepts invalid entries, requests corrections, and outputs a highly formatted financial report:
```text
Enter Employee Name: Mahmoud Hassani
Enter Employee Department: AI Engineering
Enter Base Salary (EGP): -5000
Please.. enter a positive valid value: abc
Please.. enter a valid value: 12000
Enter Performance Rating (1-5): 6
Please.. enter a valid value (1 -> 5): 5

----------------Basic  Information----------------
 Employee Name:  Mahmoud Hassani
 Department:  AI Engineering
##################################################


Component               Amount
--------------------------------------------------
Base Salary             [$12,000.0]
Performance Rating      5
Bonus                   +[$2,400.0]
Tax Deductions          -[$2,160.0]

Net Payable Salary: $[12,240.0]


Notes & Approvals
Status: Processed
HR Remarks: (Excellent performance)
```
## Best Practices Followed
- `Single Responsibility Principle (SRP)`: Each file and function has one dedicated job (e.g., handling math, validating, or displaying text).
- `Snake Case Naming Convention`: All variables and functions use descriptive lowercase names with underscores (snake_case) for maximum readability.
- `Data Encapsulation`: Used Python classes (Employee) to neatly bundle employee attributes together rather than handling loose variables across functions.
