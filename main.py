import random

def main():
    playerOneName = input("Player One - Please enter your name: ")
    print("Hello, " + playerOneName + "\n")
    playerTwoName = input("Player Two - Please enter your name: ")
    print("Hello, " + playerTwoName + "\n")

    playerOneScore = 0
    playerOneWins = 0
    playerTwoScore = 0
    playerTwoWins = 0

    rounds = 1

    while rounds != 4:
        print("Round " + str(rounds))
        playerOneScore = roll_dice()
        playerTwoScore = roll_dice()
        print(playerOneName + " Roll: " + str(playerOneScore))
        print(playerTwoName + " Roll: " + str(playerTwoScore))

        if playerOneScore > playerTwoScore:
            playerOneWins = playerOneWins + 1
            print(playerOneName + " wins!\n")
        elif playerTwoScore > playerOneScore:
            playerTwoWins = playerTwoWins + 1
            print(playerTwoName + " wins!\n")
        else:
            print("Draw!\n")

        rounds = rounds + 1

    if playerOneWins > playerTwoWins:
        print(playerOneName + " wins! Rounds won: " + str(playerOneWins))
    elif playerTwoWins > playerOneWins:
        print(playerTwoWins + " wins! Rounds won: " + str(playerTwoWins))
    else:
        print("Draw!")    

def roll_dice():
    dice = random.randint(1, 6)
    return dice

main()
