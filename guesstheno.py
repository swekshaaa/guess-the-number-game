import random
for i in range(10):
    b=random.randint(1,10)
    guess=int(input("guess a number-"))
    print(b)
    if guess==b:
        print("congratulations you won!")
    else:
        print("better luck next time!")
        