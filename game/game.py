import random

while True:
    try:
        range = int(input("Level: "))
        if range < 1:
            raise ValueError()
        break
    except ValueError:
        pass
the_number = random.randrange(1, range + 1)
print(the_number)

while True:
    while True:
        try:
            guess = int(input("Guess: "))
            break
        except ValueError:
            pass

    if guess < the_number:
        print("Too small!")
    elif guess > the_number:
        print("Too large!")
    else:
        print("Just right!")
        break