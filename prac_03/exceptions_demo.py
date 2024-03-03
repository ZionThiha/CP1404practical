#1. When will a ValueError occur?
#A ValueError will occur if either the numerator or the denominator input by the user cannot be converted to an integer by the int() function. This typically happens if the user inputs something that is not a number, such as letters or symbols.
#2. When will a ZeroDivisionError occur?
#A ZeroDivisionError will occur if the user enters 0 as the denominator. In mathematics, division by zero is undefined, and Python represents this rule by raising a ZeroDivisionError when an attempt is made to divide by zero.
#3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#Yes, the code can be modified to avoid a ZeroDivisionError by checking if the denominator is zero before attempting the division.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero denominator.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")