#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: November. 1, 2023
# Program that determines weather its a leap year or not

# Get year as string from user
year_as_string = input("Enter a year: ")

# Try catch to make sure they enter a valid imput and if not it doesn't crash
try:
    year_as_int = int(year_as_string)

    if year_as_int % 400 == 0:
        print("This is a leap year")
    else:
        if year_as_int % 4 == 0:
            if year_as_int % 100 != 0:
                print("This is a leap year")
            else:
                print("This is not a leap year")
        else:
            print("This is not a leap year")

except ValueError:
    print("Please enter a valid year")
