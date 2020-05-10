import time
import random

print("Snake and ladder w/o Board - v1.0")


class Player:
    def __init__(self, player_id):
        self.score = 0
        self.player_id = player_id

    def addScore(self, dice):
        """ If the player rolls a higher number than needed to land exactly on 100,
        their piece does not move and remains there until their next turn, when they can roll again."""
        tempScore = self.score + dice
        if tempScore > 100:
            print('Score not added needs to be exactly 100, current score ' + str(self.score))
            return 'void'
        else:
            self.score = self.score + dice
            return self.score

    def displayPlayer(self):
        return 'Player ' + str(self.player_id)

    def hasLadderOrSnake(self):
        # 8 ladders && 7 snakes dictionary
        ladders = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}
        snakes = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 85: 56, 97: 78}
        if self.score in ladders:
            self.score = ladders[self.score]
            print(self.displayPlayer() + ' lands on a ladder, climbs to square ' + str(self.score))
        elif self.score in snakes:
            self.score = snakes[self.score]
            print(self.displayPlayer() + ' was bitten by a snake, will go down to square ' + str(self.score))
        else:
            print(self.displayPlayer() + ' proceed to square ' + str(self.score))


print("Max Players:")
max_player = int(input())
players = []


def rollDice():
    for i in range(0, 3):
        print(".", end=' ')
        time.sleep(1.5)
    return random.randint(1, 6)


for player_count in range(0, max_player):
    players.append(Player(player_count + 1))

# GAME START
player_win = False
while not player_win:
    for player in range(len(players)):
        print("\n" + players[player].displayPlayer() + ' will now roll the dice')
        diceScore = rollDice()
        print(players[player].displayPlayer() + " rolled " + str(diceScore), end=' ')

        if players[player].addScore(diceScore) != 'void':
            players[player].hasLadderOrSnake()  # CHECK HAS LADDER OR SNAKE

        if players[player].score == 100:
            player_win = True
            print('\n\n' + players[player].displayPlayer() + ' WIN!')
            break

        print('\n Next player ready!<Press Enter>')
        input()




