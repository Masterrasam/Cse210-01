""" Assisgnment: Tic-Tac-Toe
    Author: Samuel Olanrewaju Okoosi """

def main():
    print("Welcome to the Tic-Tac-Toe game. This game is designed for two individuals. X and O respectively. X is the first player to play. Play wisely.")
    
    player = next_player("")
    board = create_game_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_game_board(board)
        make_a_move(player, board)
        player = next_player(player)
    display_game_board(board)
    print("Great game! Thanks for playing!") 

#creates the game board to be used throughout the program
def create_game_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

#display the game board to the users for selection
def display_game_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
#ensures that each of the user's input is within X and O. Any input returns an invalid input.
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
#contains different combinations to win the game depending on the users input
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

#displays to the user what player's turn is it to play
def make_a_move(player, board):
    square = int(input(f" it's {player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()

"""I used a version control system to develop my program. The version control system i employed was GitHub. 
I created a repository on Github called cse210-01 and copied the repository's url to clone it on VS code. This way, i was
able to a save a copy of it in my local file. I Proceded to create a file called tic-tac-toe.py and saved it under the
respository file. After writing the codes of the game, i committed it and then pushed it to my GitHub repository. This
way, my work is saved on both sides. Whatever changes i made can also be staged and pushed to my GitHub repository. """
