import random

times = int(input('Enter a number of scores: '))


def main(score):

    if score > 100 or score < 0:
        return ('Invalid score entered!')
    elif score >= 90:
        return ('Excellent')
    elif score >= 50:
        return ('Passable')
    else:
        return ('Fail')


for i in range(times):
    score = random.randint(0, 100)
    reuslt = main(score)
    print('{} is {}'.format(score, reuslt))
    f = open('results.txt', 'a')
    f.write('{} is {}\n'.format(score, reuslt))
    f.close()
