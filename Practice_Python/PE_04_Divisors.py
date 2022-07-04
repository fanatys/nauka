# Create a program that asks the user for a number and then prints out 
# a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

divisor = []
number = int(input("Type a number: "))
list = range(1, number)

for a in list:
    if (number % a) == 0:
       divisor.append(a)

divisor.append(number)

print("Divisors of this number are: ")
print(divisor)

