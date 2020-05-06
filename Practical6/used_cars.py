"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from CP1404.prac_06.car import Car

# main function

"""Demo test code to show how to use car class."""
my_car = Car(180)  # Using class imported from another file
my_car.drive(30)  # Using the variables from another file imported
print("fuel =", my_car.fuel)
print("odo =", my_car.odometer)
print(my_car)

print("Car {}, {}".format(my_car.fuel, my_car.odometer))
print("Car {self.fuel}, {self.odometer}".format(self=my_car))
"""to add the limo add"""
limo = Car("Limo", 100)
limo.add_fuel(20)
print(limo.fuel)
limo.drive(115)
print(limo.odometer)


()
