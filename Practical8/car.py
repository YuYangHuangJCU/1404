
class Car:
    # car Obj
    def __init__(self, name="", fuel=0):
        # Initialise a Car instance.
        # name: string, reference name for car
        # fuel: float, one unit of fuel drives one kilometre
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        #Return a string representation of a Car object.#
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def add_fuel(self, amount):
        #Add amount to the car's fuel.#
        self.fuel += amount

    def drive(self, Road_distance):
        # Drive the car a given Road_distance.
       # Drive given Road_distance if car has enough fuel
        # or drive until fuel runs out return the Road_distance actually driven.
        #
        if Road_distance > self.fuel:
            Road_distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= Road_distance
        self.odometer += Road_distance
        return Road_distance
