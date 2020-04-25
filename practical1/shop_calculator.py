def main():
    number()
    price()


def number():
    items = int(input('Number of items: '))
    while items <= 0:
        print('Invalid , please enter again:')
        items = int('Number of items: ')


def price():
    item1 = float(input('Price of item:'))
    item2 = float(input('Price of item:'))
    item3 = float(input('Price of item:'))
    while item1 <= 0 or item2 <= 0 or item3 <= 0:
        print('Invalid input in one of the prices, please enter again:')
        item1 = float(input('Price of item:'))
        item2 = float(input('Price of item:'))
        item3 = float(input('Price of item:'))

    if item1 >= 100:
        item1 = item1*0.9
    elif item2 >= 100:
        item2 = item2*0.9
    elif item3 >= 100:
        item3 = item3*0.9
    else:
        pass
    print('Price of item:{:.2f}'.format(item1))
    print('Price of item:{:.2f}'.format(item2))
    print('Price of item:{:.2f}'.format(item3))
    total = item1+item2+item3
    print("Total price for 3 items is ${:.2f}".format(total))


main()
