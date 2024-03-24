from guitar import Guitar
import datetime

def main():
    """Assuming the current year is 2022 for this example
    Create instances of Guitars"""
    current_year = datetime.date.today().year


    vintage_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    new_guitar = Guitar("Another Guitar", 2013, 2499.95)

    print(f"{vintage_guitar.name} get_age() - Expected {current_year - 1922}. Got {vintage_guitar.get_age()}")
    print(f"{new_guitar.name} get_age() - Expected {current_year - 2013}. Got {new_guitar.get_age()}")
    print(f"{vintage_guitar.name} is_vintage() - Expected True. Got {vintage_guitar.is_vintage()}")
    print(f"{new_guitar.name} is_vintage() - Expected False. Got {new_guitar.is_vintage()}")

main()