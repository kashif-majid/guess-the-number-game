import random

highest = 10
answer = random.randint(1, highest)

print("PLEASE GUESS THE NUMBER BETWEEN 1 AND {}".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("GAME OVER ,THANKS FOR PLAYING")
        break
    if guess < answer:
        print("GUESS HIGHER")
        break
    elif guess > answer:
        print("GUESS LOWER")
        break
    else:
        print("YOU GUESSED CORRECTLY")



