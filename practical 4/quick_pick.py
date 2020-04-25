import random
quicks = int(input('How many quicks do u wan to generate? :'))
al = []
for i in range(quicks):
    empty = []
    for i in range(6):
        randm = random.randint(1, 45)
        while randm in empty:
            randm = random.randint(1, 45)
        empty.append(randm)
        empty.sort()
        # for i in range (len(empty)):
        #     if empty[i]==empty[i+1]:
        #         empty[i]=randm.randint(1,45)
        #         while empty[i] in empty:
        # 6390413
    al.append(empty)
total = ''

for a in range(len(al)):
    row = ''
    for i in range(6):
        row += str(al[a][i])+' '
    total += row+'\n'
print(total)
