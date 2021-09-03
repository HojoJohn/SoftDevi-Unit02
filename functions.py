


def user_input():

    c_year = input("Enter the current year: ")

    c_month = input("Enter the current month: ")

    birth_year = input("Enter your birth year: ")

    birth_month = input("Enter your birth month: ")

    print("Current year: ", c_year)

    print("Current month: ", c_month)

    print("Birth year: ", birth_year)

    print("Birth month: ", birth_month)

    month = (int(c_year) - int(birth_year)) * 12 + int(c_month) - 1

    print("Your age in months: ", month)

def ap_day():

    month = input("Enter the month: ")

    day = input("Enter the day of the month: ")

    total = int(month) * 30.4 + int(day) - 30.4

    print("The approximate day of the year is:", total)


def main(): 

    user_input()
    ap_day()

main() 

