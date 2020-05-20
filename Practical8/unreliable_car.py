import random
from CP1404.prac_08.car import Car


class UnreliableCar(Car):
    def __init__(self, Name, Fuel, Reliability):
        super().__init__(Name, Fuel)
        self.Reliability = Reliability

    def drive(self, distance):
        r = random.randint(1, 100)
        if r >= self.Reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven