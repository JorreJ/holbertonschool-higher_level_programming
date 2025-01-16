#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    p_number = -number
else:
    p_number = number
if p_number % 10 > 5:
    print(f"Last digit of {number} is {p_number % 10} and is greater than 5")
elif p_number % 10 == 0:
    print(f"Last digit of {number} is {p_number % 10} and is 0")
else:
    print(f"Last digit of {number} is {p_number % 10}\
 and is less than 6 and not 0")
