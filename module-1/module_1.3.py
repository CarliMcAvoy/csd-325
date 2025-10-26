"""
Carli McAvoy
October 26, 2025
Module 1.3
"""


def main():

    try:

        bottle = int(input("How many bottle(s) of beer do you have? "))

        if bottle <= 0 or bottle >100:

            print("Number must be an integer greater than 0 and less than 101.")
            return main()

        repeat(bottle)

        print("Time to buy more bottles of beer.")

    except ValueError:

        print("ERROR: Enter a valid number.\n")
        return main()


def repeat(n):

    if n > 1:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        print(f"Take one down and pass it around, {n-1} bottle(s) of beer on the wall.\n")
        repeat(n - 1)
        return
    else:
        print(f"{n} bottle of beer on the wall, {n} bottle of beer. Take one down and pass it around, 0 bottle(s) of "
              f"beer on the wall.\n")


main()
