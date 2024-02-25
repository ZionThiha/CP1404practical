def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)

# Display the menu
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

# Loop until the user chooses to quit
while choice != "Q":
    if choice == "C":
        # Get Celsius input from the user
        celsius = float(input("Celsius: "))
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        # Print the result
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # Get Fahrenheit input from the user
        fahrenheit = float(input("Fahrenheit: "))
        # Convert Fahrenheit to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)
        # Print the result
        print(f"Result: {celsius:.2f} C")
    else:
        # Handle invalid option
        print("Invalid option")
    # Display the menu again
    print(MENU)
    # Prompt for the next choice
    choice = input(">>> ").upper()

# Print a goodbye message when quitting
print("Thank you.")
