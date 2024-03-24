# car.py module content
def main():
    """Demo test code to show how to use car class.
    Create a new Car object called "limo" with 100 units of fuel.
    Add 20 more units of fuel to this new car object using the add_fuel method.
    """
    limo = Car(100, 'Limo')

    limo.add_fuel(20)
    print(f"The limo has {limo.fuel} units of fuel.")
    distance_driven = limo.drive(115)
    print(f"The limo drove {distance_driven}km.")
    print(limo)

    # Other car interactions
    my_car = Car(180, 'My Car')
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0, name='Car'):
        """Initialise a Car instance with a name and initial fuel quantity."""
        self.fuel = fuel
        self.name = name
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self.odometer += distance_driven
        return distance_driven

    def __str__(self):
        """Return a string representation of a Car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"


main()