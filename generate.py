from random import randint

print("Randomly Generate 69420")
print("(c) Baran Önen 2020")
print("This program will generate random 5-digit numbers until it generates 69420")


def run_random():
    trialnumber = 0
    number = 0

    while number != 69420:
        number = randint(10000, 99999)
        print(number, end="\r")
        trialnumber += 1

    return f"\nDone in {trialnumber} tries."


if input("\nStart? [Y/N]: ").lower() == "y":
    print(run_random())
    while input("\nTry again? [Y/N]: ").lower() == 'y':
        print(run_random())
