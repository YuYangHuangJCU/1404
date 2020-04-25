numbers = []
for i in range(5):
    numbers.append(int(input('Number : ')))
print('The first number is {}'.format(numbers[0]))
print('The last number is {}'.format(numbers[-1]))
print('The smallest number is {}'.format(min(numbers)))
print('The latgest number is {}'.format(max(numbers)))
total = 0
for i in numbers:
    total += i
print('The average number is {}'.format(total/len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user = input('Please enter your name:')
if(user in usernames):
    print('Access Granted')
else:
    print('Access Denied')
