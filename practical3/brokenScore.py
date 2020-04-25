import random
score = float(input('Enter score: '))


def main(score):

    if score > 100 or score < 0:
        return ('Invalid score entered!')
    elif score >= 90:
        return ('Excellent')
    elif score >= 50:
        return ('Passable')
    else:
        return ('Fail')


print(main(score))
print(main(score=random.randint(0, 100)))
