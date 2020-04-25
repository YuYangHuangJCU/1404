# 1
name = input('Enter your name:')
f = open('name.txt', 'w')
f.write(name)
f.close()
# 2
f = open('name.txt', 'r')
print('Your name is '+f.read())
f.close()
# 3
f = open('numbers.txt', 'r')
one = (f.readline())
two = (f.readline())
print(one)
print(two)
print(int(one)+int(two))
f.close()
# 4
f = open('numbers.txt', 'r')
for x in f:
    print(x)
