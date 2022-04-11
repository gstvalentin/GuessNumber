import random

def guess(x):
    random_number = 50 #random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number betwenn 1 and {x}: '))
        if (guess > random_number and guess < random_number + 10) or (guess < random_number and guess > random_number - 10):
            print('Almost there, try again. You nearly won!')
        elif guess > random_number + 11:
            print('Sorry, guess again. Too high')
        elif guess > random_number - 11:
            print('Sorry, guess again. Too low')
        

guess(100)