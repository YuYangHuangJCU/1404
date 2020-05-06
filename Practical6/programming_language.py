
class ProgrammingLanguage:#Main calss
    def __init__(self, name, typing, reflection, year):#Taking in parameters
        """Constructor that takes in parameters and create object"""
        self.n = name#Assigning variables
        self.t = typing
        self.r = reflection
        self.y = year

    def __str__(self):
        """return the detail of the language"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.n, self.t, self.r, self.y)

    def is_dynamic(self):
        """Judge if language is dynamic."""
        return self.t == "Dynamic"


def test():#Test functions
    """To check with python"""
    python = ProgrammingLanguage("Java", "Dynamic", True, 1987)
    print(python)


if __name__ == "__main__":
    test()
