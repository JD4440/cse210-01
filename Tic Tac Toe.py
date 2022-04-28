'''Tic Tac Toe'''
'''Author: Shawn Jensen'''

def main():
    player = next_player("")
    gameboard = create_gameboard()
    while not (the_winner(gameboard) or tied_game(gameboard)):
        show_gameboard(gameboard)
        make_move(player, gameboard)
        player = next_player(player)
    show_gameboard(gameboard)

def create_gameboard():
    gameboard = []
    for i in range(9):
        gameboard.append(i + 1)
    return gameboard

def show_gameboard(gameboard):
    print()
    print(f"{gameboard[0]}|{gameboard[1]}|{gameboard[2]}")
    print('-+-+-')
    print(f"{gameboard[3]}|{gameboard[4]}|{gameboard[5]}")
    print('-+-+-')
    print(f"{gameboard[6]}|{gameboard[7]}|{gameboard[8]}")
    print()

def tied_game(gameboard):
    for i in range(9):
        if gameboard[i] != "x" and gameboard[i] != "o":
            return False
    return True 

def the_winner(gameboard):
    return (gameboard[0] == gameboard[1] == gameboard[2] or
            gameboard[3] == gameboard[4] == gameboard[5] or
            gameboard[6] == gameboard[7] == gameboard[8] or
            gameboard[0] == gameboard[3] == gameboard[6] or
            gameboard[1] == gameboard[4] == gameboard[7] or
            gameboard[2] == gameboard[5] == gameboard[8] or
            gameboard[0] == gameboard[4] == gameboard[8] or
            gameboard[2] == gameboard[4] == gameboard[6])

def make_move(player, gameboard):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    gameboard[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()
