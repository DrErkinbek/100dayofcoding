print("Welcome to the tip calculator!")
bill = float(input(print("What was total bill? $")))
tip = int(input(print("How much tip would you like to give? 10, 12, or 15?")))
people = int(input(print("How many people to split the bill? ")))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
print(f"Total bill: ${bill_with_tip}")
print(f"Each person should pay: ${bill_per_person}")