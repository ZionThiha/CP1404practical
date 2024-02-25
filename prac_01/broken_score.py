score = float(input("Enter score: "))

if score < 0 or score > 100:  # Checks for invalid scores
    print("Invalid score")
elif score >= 90:  # Score is 90 or more
    print("Excellent")
elif score >= 50:  # Score is 50 or more but less than 90
    print("Passable")
else:  # Score is less than 50
    print("Bad")
