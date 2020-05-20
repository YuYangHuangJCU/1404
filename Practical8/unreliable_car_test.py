from CP1404.prac_08.unreliable_car import UnreliableCar


def test():
    NEW_CAR = UnreliableCar("Parker",150, 70)
    print(NEW_CAR.drive(100))
    print(NEW_CAR.drive(50))

test()
