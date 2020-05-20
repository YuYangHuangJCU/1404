from CP1404.prac_08.silver_service_taxi import SilverServiceTaxi

def test():
    taxi = SilverServiceTaxi("Parker", 200, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

test()