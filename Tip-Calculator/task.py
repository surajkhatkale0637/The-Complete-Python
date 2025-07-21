
print("welcome to the trip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip you would like to give? 10, 12 or 15?"))
tip = tip / 100
bill_with_tip = (bill * tip) + bill
people = int(input("How many people to split the bill?"))
bill_with_tip/= people
print(f"Each person should pay: ${round(bill_with_tip, 2)}")
