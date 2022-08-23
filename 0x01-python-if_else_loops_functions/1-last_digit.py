#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number % 10
print(f"Last digit of {number} is {ldigit} and is", end=" ")
if ldigit > 5:
    print("greater than 5")
elif ldigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
