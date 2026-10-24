age = int(input("Enter your age: "))

if age > 18:
    print("You are eligible to vote.")
elif age == 18:
    print("You are 18 and eligible to vote.")
else:
    print("You are not eligible to vote.")


if age == 0:
    print("Age is zero.")
elif age % 2 == 0:
    print("Age is even.")
else:
    print("Age is odd.")