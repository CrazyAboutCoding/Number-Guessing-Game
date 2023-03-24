import random
def number_guessing():
    num=random.randint(1,10)
    print("Hey there! I'm thinking of a number from 1 to 10")
    guess=int(input("Guess what number I'm thinking?"))
    while num!=0:
        if num<guess:
            print("Your guess is high.")
            guess=int(input("Guess again:"))
        elif num>guess:
            print("Your guess is low")
            guess=int(input("Guess again:"))
        else:
            print("You guessed it right! The number was", num)
            break
number_guessing()
