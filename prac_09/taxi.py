from prac_09.car import Car

class Taxi(Car):

    price_per_km = 1.23

    def __init__(self, name, fuel):

        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):

        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):

        return self.price_per_km * self.current_fare_distance

    def start_fare(self):

        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


my_taxi = Taxi("Prius 1", 100)


my_taxi.drive(40)


print(f"Details: {my_taxi}")
print(f"Current Fare: ${my_taxi.get_fare():.2f}")


my_taxi.start_fare()
my_taxi.drive(100)


print(f"Details after new trip: {my_taxi}")
print(f"Current Fare after new trip: ${my_taxi.get_fare():.2f}")