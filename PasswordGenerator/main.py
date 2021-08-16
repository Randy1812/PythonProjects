import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for i in range(nr_letters):
#     password += random.choice(letters)
# for i in range(nr_symbols):
#     password += random.choice(symbols)
# for i in range(nr_numbers):
#     password += random.choice(numbers)
#
# print(f"Here is your password: {password}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""
nl = nn = ns = 0
while nl+nn+ns <= nr_letters + nr_symbols + nr_numbers:
    ch = random.randint(1,3)
    if ch == 1:
        if nl <= nr_letters:
            password += random.choice(letters)
            nl += 1
    elif ch == 2:
        if ns <= nr_symbols:
            password += random.choice(symbols)
            ns += 1
    elif ch == 3:
        if nn <= nr_numbers:
            password += random.choice(numbers)
            nn += 1

print(f"Here is your password: {password}")