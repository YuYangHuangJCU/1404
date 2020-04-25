STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}
short = input("Enter short state: ").upper()
while short != "":
    if short in STATE_NAMES:
        print("{} is {}" .format(short, STATE_NAMES[short]))
    else:
        print("Invalid short state")
    short = input("Enter short state: ").upper()
