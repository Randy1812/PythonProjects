from art import logo

print(logo)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    should_continue = True
    num1 = float(input("What's the first number? : "))
    print("+\n-\n*\n/\n")
    while should_continue:
        opr = input("Pick an operation : ")
        num2 = float(input("What's the next number?: "))
        calc_func = operations[opr]
        result = calc_func(num1, num2)
        print(f"{num1} {opr} {num2} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            should_continue = False
            calculator()


calculator()
