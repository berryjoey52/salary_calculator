# Salary Calculator on hourly Wage
weeks_in_year = 52.1429

def salary():
    hours = float(input("How many hours will you be working a week? (ex. 40) "))
    rate = float(input("What is your hour rate in $ (ex. 17.75)"))
    salary = ((hours * rate) * weeks_in_year)
    
    print(f"Salary: ${salary:.2f}")
    print(f"Weekly Hours:{hours}")
    print(f"Rate: ${rate:.2f}/hr")
    menu()

def hours():
    rate = float(input("What is your hour rate in $? (ex. 17.75)"))
    salary = float(input("What is your targeted salary? (ex. 60000)"))
    hours = (((salary / weeks_in_year) / rate))
    
    print(f"Salary: ${salary:.2f}")
    print(f"Weekly Hours:{hours}")
    print(f"Rate: ${rate:.2f}/hr")
    menu()

def rate():
    salary = float(input("What is your targeted salary? (ex. 60000)"))
    hours = float(input("How many hours will you be working a week? (ex. 40) "))
    rate = ((salary / hours) / weeks_in_year) 
   
    print(f"Salary: ${salary:.2f}")
    print(f"Weekly Hours:{hours}")
    print(f"Rate: ${rate:2f}/hr")
    menu()
   
def help():
    print("Selection 1 will let you calcuate the yearly salary if you already have the hourly wage and numbers of hours worked. \nSelection 2 will give you the hours needed to work per week if you have the salary and rate per hour. \nSelection 3 Will give you the hourly rate if you have the Salary and the hours worked each week. \nSelection 0 will have you exit the program.")

def menu():
    selection = input("Press 1 if you would like to calculate salary. \nPress 2 if you would like to calculate hours worked per week. \nPress 3 if you would like to caculate the hourly rate. \nPress 0 if you would like to end the program. \nPress 'h' for help.\n")
    if selection == "1":
        salary()
    elif selection == "2":
        hours()
    elif selection == "3":
        rate()
    elif selection == "0":
        print("Thank you for using wage calculator, bye!")
        exit()
    elif selection == "h":
        help()
        menu()
    else:
        print("Invalid selction please try again")
        menu()
menu()