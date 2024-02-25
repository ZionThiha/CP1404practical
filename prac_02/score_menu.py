import random


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive."""
    score = float(input("Enter a score between 0 and 100: "))
    while score < 0 or score > 100:
        print("Invalid score. The score must be between 0 and 100.")
        score = float(input("Enter a score between 0 and 100: "))
    return score


def evaluate_score(score):
    """Evaluate the score and return the result."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score):
    """Print the result based on the score."""
    result = evaluate_score(score)
    print(f"Result: {result}")


def show_stars(score):
    """Print stars equal to the score."""
    print("*" * int(score))


def main():
    score = -1  # Initialize score with an invalid value to enter the loop
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score >= 0 and score <= 100:
                print_result(score)
            else:
                print("Please get a valid score first.")
        elif choice == "S":
            if score >= 0 and score <= 100:
                show_stars(score)
            else:
                print("Please get a valid score first.")
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").upper()

    print("Farewell!")


if __name__ == "__main__":
    main()