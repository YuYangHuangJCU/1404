"""Structures for a single guitar"""




class Guitar:
    # variables
    name = ""
    year = 0
    cost = 0

    def __init__(self, name, year, cost):  # parameters
        """constructor that takes three parameters and registers the result"""
        self.name = name  # self method inside a class function
        self.year = year
        self.cost = cost

    def __str__(self):
        """string format for representation of a guitar object"""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """method to get age of guitar"""
        return (2018 - self.year)

    def is_vintage(self):
        """method to determine if a guitar is vintage"""
        age = self.get_age()
        if age >= 50:
            return True
        return False


def unit_test():
    """unit tests after creation of the guitar object"""

    # create test instances
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 14035.40)
    another_guitar = Guitar("Another Guitar", 2012, 200.0)
    fifty_guitar = Guitar("50-year old guitar", 1968, 10000.34)

    # test get_age()
    print("{} get_age() - Expected 96. Actual value got:  {}".format(
        gibson_guitar, gibson_guitar.get_age()))
    print("{} get_age() - Expected 6. Actual value got:  {}".format(
        another_guitar, another_guitar.get_age()))

    # test is_vintage()
    print("{} is_vintage() - Expected True. Actual value got:  {}".format(
        gibson_guitar, gibson_guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Actual value got:  {}".format(
        another_guitar, another_guitar.is_vintage()))
    print("{} is_vintage() - Expected True. Actual value got:  {}".format(
        fifty_guitar, fifty_guitar.is_vintage()))


if __name__ == "__main__":
    unit_test()
