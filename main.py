import random
from tokenize import Number

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number betwenn 1 and {x}: '))
        except:
            print('\n')
            print(f'Please, inpunt a integer between 1 and {x}')
            print('\n')
            guess = int(input(f'Guess a number betwenn 1 and {x}: '))
        
        if (guess > random_number and guess <= round(random_number * 1.2)) or (guess < random_number and guess >= round(random_number * 0.8)):
            print('Almost there, try again. You nearly won!')
        elif guess > round(random_number * 1.2):
            print('Sorry, guess again. Too high')
        elif guess < round(random_number * 0.8):
            print('Sorry, guess again. Too low')
    print('\n')
    print(f'Congratulations!! YOU WON!!!!')
    print(f'The number was {guess}!')
    
guess(random.randint(10, 100))