# Simple calculator by Aymane Berhoua - @berhocode 

def power():
    number = safe_input("Number > ")
    pow_number = safe_input("Power > ")
    print(f"{number} ^ {pow_number} = {number ** pow_number}")

def addition():
    number_1 = safe_input("1st number > ")
    number_2 = safe_input("2nd number > ")
    print(f"{number_1} + {number_2} = {number_1 + number_2}")

def subtraction():  # Fixed spelling
    number_1 = safe_input("1st number > ")
    number_2 = safe_input("2nd number > ")
    print(f"{number_1} - {number_2} = {number_1 - number_2}")

def multiplication():
    number_1 = safe_input("1st number > ")
    number_2 = safe_input("2nd number > ")
    print(f"{number_1} * {number_2} = {number_1 * number_2}")

def division():
    number_1 = safe_input("1st number > ")
    number_2 = safe_input("2nd number > ")
    if number_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{number_1} / {number_2} = {number_1 / number_2}")

def floor_division():
    number_1 = safe_input("1st number > ")
    number_2 = safe_input("2nd number > ")
    if number_2 == 0:
        print("Error: Floor division by zero is not allowed.")
    else:
        print(f"{number_1} // {number_2} = {number_1 // number_2}")

def modulus():
    number_1 = safe_input("1st number > ")
    number_2 = safe_input("2nd number > ")
    if number_2 == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        print(f"{number_1} % {number_2} = {number_1 % number_2}")

def safe_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    exit_key = "exit"
    operator = input("Choose an operator (+, -, *, /, //, %, ^) or type 'exit' to quit > ")

    if operator.lower() == exit_key:
        print("Exiting program...")
        break

    if operator == "+":
        addition()
    elif operator == "-":
        subtraction()
    elif operator == "*":
        multiplication()
    elif operator == "/":
        division()
    elif operator == "//":
        floor_division()
    elif operator == "%":
        modulus()
    elif operator == "^":
        power()
    else:
        print(f"'{operator}' is not a valid operator.")