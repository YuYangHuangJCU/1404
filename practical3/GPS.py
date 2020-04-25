import random


def main():
    print('Welcome to the Gopher Population Simulator!')
    start = 1000
    for i in range(10):
        bornRate = random.randint(10, 20)
        bornRate = bornRate/100
        deathRate = random.randint(5, 25)
        deathRate = deathRate/100
        print('Year {}\n'.format(i+1))
        print('{} gophers were born {} died.'.format(
            round((start*bornRate), 0), round((start*deathRate), 0)))
        start = start+start*bornRate-start*deathRate
        print('Population: '+str(round(start, 0)))


main()
