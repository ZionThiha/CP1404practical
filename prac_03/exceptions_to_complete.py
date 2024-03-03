is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # This line will be reached only if the input is a valid integer, thus breaking the loop
    except ValueError:  # Catching the ValueError specifically to handle non-integer inputs
        print("Please enter a valid integer.")
print("Valid result is:", result)
