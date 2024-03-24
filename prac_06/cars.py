def main():
    """Create a new Car object called "limo" with 100 units of fuel.
    Add 20 more units of fuel to this new car object using the add method.
    Attempt to drive the car 115 km using the drive method."""
    limo = Car(100, "Limo")

    limo.add_fuel(20)
    print(f"The limo has {limo.fuel} units of fuel.")

    distance_driven = limo.drive(115)
    print(f"The limo drove {distance_driven}km.")

    print(limo)
class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0, name='Car'):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        name: str, the name of the car
        """
        self.fuel = fuel
        self.name = name
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of a Car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"


main()