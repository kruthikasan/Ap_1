print("Welcome to the roller coaster ride!")
height = int(input("What is your height?"))
age = int(input("How old are you to go on a ride?"))
if height >= 122 :
    print("Can ride")
    if age >= 18:
        print("pay $20")
    elif age >= 12:
        print("Pay $15")
    elif age <18:
        print("Pay $10")
else:
    print("can not ride "
          "as your height doesn't meet our requirement")