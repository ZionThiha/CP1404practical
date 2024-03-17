# Dictionary of color names and their hexadecimal codes.
colour_codes = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

print("Enter a color name to get its hexadecimal code. Enter a blank to stop.")

while True:
    user_input = input("Enter color name: ").strip()
    if user_input == "":
        break
    user_input_formatted = user_input[0].upper() + user_input[1:].lower()
    hex_code = colour_codes.get(user_input_formatted)
    if hex_code:
        print(f"The hexadecimal code for {user_input_formatted} is {hex_code}.")
    else:
        print("Invalid color name. Please try again.")

print("Program ended.")