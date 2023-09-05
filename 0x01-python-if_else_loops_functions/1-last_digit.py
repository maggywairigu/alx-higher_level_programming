#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is", number % 10, end=" ")

number_str = str(number)
last_digit = number_str[-1]

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
