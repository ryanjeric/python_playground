import random

play = True
print('Hello,what is your name?')
player = input()
while play:
    secretNumber = random.randint(1, 20)
    print('Well ' + player + ', I am thinking of a number between 1-20')

    # ask the player to guess 6 times:
    for guessesTaken in range(1, 7):
        print('Take a guess')
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break # this condition is the correct guess!
    if guess == secretNumber:
        print('Good job ' + player + "! You guess my number in " + str(guessesTaken) + ' guesses')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

    print('Do you want to play again? (Y/N)')
    play = bool(input() == 'Y')
