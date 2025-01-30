print("Welcome to the tip calculator project.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15 "))
split_bill = int(input("How many people the bill will be split between?"))
bill_wid_tip = tip/100 *bill + bill
print(bill_wid_tip)
individual_bill = bill_wid_tip / split_bill
print(f"Each person should pay : ${individual_bill}")