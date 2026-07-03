def calculate_bonus(base_salary, performance_rating):
    if performance_rating == 5: bonus_percentage = 0.2
    elif performance_rating in [3, 4]: bonus_percentage = 0.1
    else: bonus_percentage = 0
    return base_salary * bonus_percentage

def calculate_tax(gross_salary):
    if gross_salary > 7000: tax_percentage = 0.15
    elif 3000 <= gross_salary <= 7000: tax_percentage = 0.1
    else: tax_percentage = 0
    return gross_salary * tax_percentage
