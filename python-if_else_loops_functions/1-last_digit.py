#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#menfi ededin son reqeminin menfi olmasi
if number < 0:
    last_digit = -(-number % 10)
else:
    last_digit = number % 10
if number % 10 > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")
