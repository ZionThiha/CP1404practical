import csv
from guitar import Guitar
def read_guitars_from_csv(filename):

    guitars = []
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def main():
    print("My guitars!")
    # Read guitar data from the 'guitars.csv' file
    guitars = read_guitars_from_csv('guitars.csv')

    guitars.sort()


    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f}{vintage_string}")



main()