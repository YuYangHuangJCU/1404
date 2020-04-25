print('C - convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit')
choice = input('>>>').upper()
while choice != 'Q':
    if choice == 'C':
        celsius = float(input('Celsius: '))
        fahrenheit = celsius*9.0/5+32
        print('Result: {:.2f} Fahrenheit'.format(fahrenheit))
    elif choice == 'F':
        fahrenheit = float(input('Fahrenheit: '))
        celsius = 5/9*(fahrenheit-32)
        print('Result: {:.2f} Celsius'.format(celsius))
    else:
        print('Invalid!')
        print(
            'C - convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit')
        choice = input('>>>').upper
print('Program terminated!Thank you!')
