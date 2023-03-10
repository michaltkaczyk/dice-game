import random

N_ROUNDS = 10

def main():
    playerOneName = input("Player One - Please enter your name: ")
    print("Hello, {}\n".format(playerOneName))
    playerTwoName = input("Player Two - Please enter your name: ")
    print("Hello, {}\n".format(playerTwoName))

    playerOneScore = 0
    playerOneWins = 0
    playerTwoScore = 0
    playerTwoWins = 0

    round_counter = 1

    while round_counter <= N_ROUNDS:
        print("Round " + str(round_counter))
        round_counter = round_counter + 1

        playerOneScore = roll_dice()
        print("{} rolls {}".format(playerOneName, playerOneScore))
        playerTwoScore = roll_dice()
        print("{} rolls {}".format(playerTwoName, playerTwoScore))

        if playerOneScore > playerTwoScore:
            playerOneWins = playerOneWins + 1
            print("{} wins!\n".format(playerOneName))
        elif playerTwoScore > playerOneScore:
            playerTwoWins = playerTwoWins + 1
            print("{} wins!\n".format(playerTwoName))
        else:
            print("Draw!\n")

    if playerOneWins > playerTwoWins:
        print("{} wins! Rounds won: {}".format(playerOneName, playerOneWins))
    elif playerTwoWins > playerOneWins:
        print("{} wins! Rounds won: {}".format(playerTwoName, playerTwoWins))
    else:
        print("Draw!")    

def roll_dice():
    dice = random.randint(1, 6)
    return dice

if __name__ == '__main__':
    main()
