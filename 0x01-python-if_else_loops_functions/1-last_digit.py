#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number_str = str(number)
last_digit = int(number_str[-1])
last_digit_negative = '-' + number_str[-1]
if number >= 0:
    print("Last digit of", number, "is", last_digit, end=" ")
else:
    print("Last digit of", number, "is", last_digit_negative, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
