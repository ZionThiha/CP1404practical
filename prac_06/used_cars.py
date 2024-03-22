class Car:
    def __init__(self, fuel=0, name="Car"):
        self.fuel = fuel
        self._odometer = 0
        self.name = name

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"


limo = Car(100, name="Limo")

limo.add_fuel(20)

print(limo.fuel)

distance_driven = limo.drive(115)

print(limo)