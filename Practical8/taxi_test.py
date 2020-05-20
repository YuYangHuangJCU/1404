from CP1404.prac_08.taxi import Taxi

def test():
    new_taxis = Taxi("Prius 1", 100)
    new_taxis.drive(40)
    print(new_taxis)
    print("Fare:${:.2f}".format(new_taxis.get_fare()))

    new_taxis.start_fare()

    new_taxis.drive(100)
    print(new_taxis)
    print("Fare:${:.2f}".format(new_taxis.get_fare()))


test()
