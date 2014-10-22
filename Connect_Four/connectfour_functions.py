#Richard Lin

import connectfour
    
def new_game() -> connectfour.ConnectFourGameState:
    '''creates a new connect four game state'''
    return connectfour.new_game_state()

def drop_game_state(command: str, game_state: connectfour.ConnectFourGameState) -> connectfour.ConnectFourGameState:
    '''prints out game board based on drop command'''
    column_number = int(command.split()[-1]) - 1
    return connectfour.drop_piece(game_state, column_number)    

def pop_game_state(command: str, game_state: connectfour.ConnectFourGameState) -> connectfour.ConnectFourGameState:
    '''prints out game board based on pop command'''
    column_number = int(command.split()[-1]) - 1
    return connectfour.pop_piece(game_state, column_number)    

def print_winner(game_state: connectfour.ConnectFourGameState) -> str:
    '''prints the winner of the game'''
    if connectfour.winning_player(game_state) == connectfour.YELLOW:
        print('WINNER_YELLOW')
        print('Goodbye!') 
    elif connectfour.winning_player(game_state) == connectfour.RED:
        print('WINNER_RED')
        print('Goodbye!')

def game_board_check_winner(function: 'drop or pop function'):
    '''prints game board and checks winner on drop or pop game state'''
    print_game_board(function)
    return print_winner(function)

# -------------------- CONVERTS GAME STATE TO BOARD --------------------
def print_game_board(game_state: connectfour.ConnectFourGameState) -> None:
    '''prints out current game board'''
    print('\t1  2  3  4  5  6  7')
    board = _change_space_to_dot(game_state).board
    board_list = []
    for row_number in range(connectfour.BOARD_ROWS):
        row_list = []
        for column_number in range(connectfour.BOARD_COLUMNS):
            row_list.extend(board[column_number][row_number])
        board_list.append(row_list)
    
    for row in board_list:
        print('\t', end = '')
        for column in range(connectfour.BOARD_COLUMNS):
            if column < connectfour.BOARD_COLUMNS - 1:
                print(row[column] , end = '  ')
            else:
                print(row[column])

def _change_space_to_dot(game_state:connectfour.ConnectFourGameState) -> connectfour.ConnectFourGameState:
    '''changes all the spaces on the board into dots'''
    board = game_state.board
    new_board = []
    for column in board:
        new_column = []
        for row in column:
            if row == ' ':
                new_column.extend('.')
            else:
                new_column.extend(row)
        new_board.append(new_column)
    return connectfour.ConnectFourGameState(board = new_board, turn = game_state.turn)
