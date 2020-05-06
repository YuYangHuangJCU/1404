"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):  # parameters
        """Initialise a Car instance.
        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.n = name#assigning variables
        self.f = fuel
        self.o = 0

    def __str__(self):#Taking in self variables
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.n, self.f,
                                                 self.o)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.f += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.f:
            distance = self.f
            self.f = 0
        else:
            self.f -= distance
        self.o += distance
        return distance


if __name__ == "__main__":
    drive()
