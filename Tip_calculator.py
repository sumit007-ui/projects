print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
Tip = float(input("How much tip would you like to give in percent ? 10 , 12 , 15 ?"))
person = int(input("Each person should pay:  "))

total_bill = ((bill*Tip/100)+bill)/person
print(total_bill)

