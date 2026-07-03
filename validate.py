def get_salary():
    print("Enter Base Salary (EGP)",end=": ")
    while True:
        salary = input()
        try:
            salary = float(salary)
        except:
            print("Please.. enter a valid value",end=": ")
            continue
        if salary >= 0: return salary
        else: print("Please.. enter a positive valid value",end=": ")

def get_rating():
    print("Enter Performance Rating (1-5)",end=": ")
    while True:
        rating = input()
        try:
            rating = int(rating)
        except:
            print("Please.. enter a valid value",end=": ")
            continue
        if 1 <= rating <= 5: return rating
        else: print("Please.. enter a valid value (1 -> 5)",end=": ")

        