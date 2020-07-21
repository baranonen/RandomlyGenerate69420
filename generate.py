from random import *
import sys

print("Randomly Generate 69420")
print("(c) Baran Önen 2020")
print("This program will generate random 5-digit numbers until it generates 69420")
print("To start, type y")

answer = input()

if answer != "y":
    sys.exit()

trialnumber = 0
number = 0

while number != 69420:
    number = randint(9999, 100000)
    print(number)
    trialnumber = trialnumber + 1

print("Done in " + str(trialnumber) + " tries")