#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    p_number = -number % 10
else:
    p_number = number % 10
if p_number > 5:
    print(f"Last digit of {number} is {p_number} and is greater than 5")
elif p_number == 0:
    print(f"Last digit of {number} is {p_number} and is 0")
else:
    print(f"Last digit of {number} is {p_number}\
 and is less than 6 and not 0")
