finished = False
result = 0
while not finished:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)

    except:
        print("Please enter a valid integer.")
        finished = True
print("Valid result is:", result)
