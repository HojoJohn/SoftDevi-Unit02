def variable_practice():
    age = 19

    year = 365    

    name_pet = "lucky"

    pi = 3.14159

    print(age, year, name_pet, pi)


 
def expressions_practice():

    literal = 35
    addition = 5 + 5
    exponent = 5 ** 5
    floor_division = 5 // 5
    mod = 5 % 7
    parantheses = 5 ** (5 + 5 - 6)

    print(literal, addition, exponent, floor_division, mod, parantheses)



def prompt_and_print():

    first_number = input("Enter your first numeric value: ")

    second_number = input("Enter your second numeric value: ")

   

    print(int(first_number) * int(second_number))



def main():
    prompt_and_print()
    expressions_practice()
    variable_practice()

main()