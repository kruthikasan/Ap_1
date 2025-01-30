#Nested If statements

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
age = int(input("Enter your age."))
if height >= 122:
    print("You can go on roller coater ride.")
    if age >= 18:
        print("pay $20")
    else:
        print("Pay $10")
else:
    print("You can not ride as your height doesn't meet the requirement.")