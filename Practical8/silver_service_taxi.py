from CP1404.prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, Name, Fuel, Fanciness):

        super().__init__(Name, Fuel)
        self.Fanciness = Fanciness
        self.price_per_km *= Fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                    self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()