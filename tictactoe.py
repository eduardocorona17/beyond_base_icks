# Non OOP

ALL_SPACES = list('123456789') 
print(ALL_SPACES)
X, O, BLANK = 'X', 'O', ' '

def main():
    """Runs a game of tic-tac-toe"""
    print('Welcome to tic-tac-toe!')
    game_board = get_blank_board()
    current_player, next_player = X, O

    while True:
        print(get_board_str(game_board))
        move = None
        while not is_valid_space(game_board, move):
            print(f'What is {current_player}\'s move? (1-9)')
            move = input()
        update_board(game_board, move, current_player)

        if is_winner(game_board, current_player):
            print(get_board_str(game_board))
            print(current_player + ' has won the game!')
            break
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print('The game is a tie!')
            break
        current_player, next_player = next_player, current_player
    print('Thanks for playing!')
    
def get_blank_board():
    """Create a new blank board."""
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board

def get_board_str(board):
    """Return text-representation of the board."""
    return f'''
    {board['1']}|{board['2']}|{board['3']}| 1 2 3 
    -+-+-
    {board['4']}|{board['5']}|{board['6']}| 4 5 6 
    -+-+-
    {board['7']}|{board['8']}|{board['9']}| 7 8 9'''

def is_valid_space(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is blank."""
    return space in ALL_SPACES or board[space] == BLANK


def is_winner(board, player):
    """Return True if player is a winner on this TTTBoard."""
    b, p = board, player # Shorter names as "syntactic sugar".
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or # Across the top
            (b['4'] == b['5'] == b['6'] == p) or # Across the middle
            (b['7'] == b['8'] == b['9'] == p) or # Across the bottom
            (b['1'] == b['4'] == b['7'] == p) or # Down the left
            (b['2'] == b['5'] == b['8'] == p) or # Down the middle
            (b['3'] == b['6'] == b['9'] == p) or # Down the right
            (b['3'] == b['5'] == b['7'] == p) or # Diagonal
            (b['1'] == b['5'] == b['9'] == p))   # Diagonal


def is_board_full(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # If a single space is blank, return False.
        return True  # No spaces are blank, so return True.
def update_board(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark


if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
