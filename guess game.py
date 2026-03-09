import random
number=random.randint(1,20)
while True:
    guess=int(input("enter the number between 1 and 20:"))

    if guess==number:
        print("Correct! you guess the correct number")
        break
    else:
        print("Try again!")