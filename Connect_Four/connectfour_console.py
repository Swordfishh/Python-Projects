#Richard Lin

import connectfour
import connectfour_functions

# -------------------- MAIN PROGRAM --------------------
def user_interface() -> None:
    '''connect four game console'''
    connectfour_functions.print_game_board(connectfour_functions.new_game())
    game_board(connectfour_functions.new_game())
    

def game_board(game_state: connectfour.ConnectFourGameState) -> connectfour.ConnectFourGameState:
    '''returns game board of each move until a player wins'''
    if connectfour.winning_player(game_state) not in [connectfour.YELLOW, connectfour.RED]:
        
        if game_state.turn == 'R':
            user_input = input('\tRed Player\'s turn: ')
            _moves(game_state, user_input)

        elif game_state.turn == 'Y':
            user_input = input('\tYellow Player\'s turn: ')
            _moves(game_state, user_input)
            
        return None

    
def _moves(game_state: connectfour.ConnectFourGameState, user_input) -> connectfour.ConnectFourGameState:
    '''performs actions based on pop or drop'''
    try:
        if user_input.split()[0] == 'DROP':
            connectfour_functions.game_board_check_winner(connectfour_functions.drop_game_state(user_input, game_state))
            return game_board(connectfour_functions.drop_game_state(user_input, game_state))

        elif user_input.split()[0] == 'POP':
            connectfour_functions.game_board_check_winner(connectfour_functions.pop_game_state(user_input, game_state))
            return game_board(connectfour_functions.pop_game_state(user_input, game_state))

        else:
            print()
            print('\tInvalid move, please enter DROP # or POP #. Ex: DROP 3')
            return game_board(game_state)

    except:
        print()
        print('\tInvalid move, please enter DROP # or POP #. Ex: DROP 3')
        return game_board(game_state)
 

if __name__ == '__main__':
    user_interface()
