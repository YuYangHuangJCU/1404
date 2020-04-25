for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
a = 20

for i in range(20):
    print(a, end=' ')
    a -= 1
print()
userINput = int(input('Enter a number: '))
for i in range((userINput+1)):
    print('*'*i)

sales = float(input("Enter sales: $"))
while sales >= 0:
    bonus = 0
    if sales < 1000:
        bonus = sales*0.1
        print('Bonus is {}'.format(bonus))
    elif sales >= 1000:
        bonus = sales*0.15
        print('Bonus is {}'.format(bonus))
    else:
        print('Number entered is invalid.')
    sales = float(input("Enter sales: $"))
