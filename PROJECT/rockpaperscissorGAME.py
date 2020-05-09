import random

print("Rock Paper Scissors")
print("Best of:")
rounds = int(input())

# SCORE
player_score = 0
computer_score = 0

picks = ['Rock', 'Paper', 'Scissors']


def score():
    print('Score')
    print('Player:' + str(player_score))
    print('Computer:' + str(computer_score))


for roundCount in range(0, rounds):
    computer = picks[random.randint(0, 2)]
    print('\nRound: ' + str(roundCount+1))
    print('Rock Paper Scissors')
    player = input()
    player_valid_pick = False
    while not player_valid_pick:
        if player not in picks:
            print("That's not a valid pick. Check your spelling!")
            player = input()
        else:
            player_valid_pick = True

    if player == computer:
        print('Tie')
        score()
    elif player == 'Rock':
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
        score()
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
        score()
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
        score()


print('\nFinal Score')
print('Player:' + str(player_score))
print('Computer:' + str(computer_score))
print()
if player_score > computer_score:
    print('You win!')
elif player_score == computer_score:
    print('Draw!')
else:
    print('You lose!')
