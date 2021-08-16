print("Welcome to the Tip Calculator.")
amt = float(input("What was the total bill? "))
pct = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
num = float(input("How many people to split the bill? "))
amt += amt*pct/100
amt /= num
print(f"Each person must pay: ${round(amt,2)}")
