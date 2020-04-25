def main():
    print('C - convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit')
    choice = input('>>>').upper()

    def celcius(celsius):
        fahrenheit = celsius*9.0/5+32
        print('Result: {:.2f} Fahrenheit'.format(fahrenheit))

    def f(f):
        celsius = 5/9*(fahrenheit-32)
        print('Result: {:.2f} Celsius'.format(celsius))

    if choice == 'C':
        user = float(input('Celcisus: '))
        celcius(user)

    elif choice == 'F':
        fahrenheit = float(input('Fahrenheit: '))
        f(fahrenheit)

    else:
        print('Invalid!')

    print('Program terminated!Thank you!')


main()
