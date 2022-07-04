# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.

# Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.

number = int(input("Type a number: "))

if (number % 4) == 0:
    print("Your number is a multiple of 4")
elif (number % 2) == 0:
    print("Your number is even")
else:
    print("Your number is odd")

num = int(input("Type number to check: "))
check = int(input("Type number to divide: "))

if (num % check) == 0:
    print("check divides evenly into num")
else:
    print("check does not divides evenly into num")



