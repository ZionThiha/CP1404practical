import random

def evaluate_score(score):
    """Evaluate the score and return the result as a string."""
    if score < 0 or score > 100:  # Checks for invalid scores
        return "Invalid score"
    elif score >= 90:  # Score is 90 or more
        return "Excellent"
    elif score >= 50:  # Score is 50 or more but less than 90
        return "Passable"
    else:  # Score is less than 50
        return "Bad"

def main():
    # Ask the user for their score
    user_score = float(input("Enter score: "))
    # Use the evaluate_score function to get the result and print it
    print(evaluate_score(user_score))

    # Generate a random score and print the result using the same function
    random_score = random.randint(0, 100)  # Generate a random score between 0 and 100
    print(f"Random score: {random_score}")
    print(evaluate_score(random_score))

if __name__ == "__main__":
    main()