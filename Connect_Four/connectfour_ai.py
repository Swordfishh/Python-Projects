#Richard Lin

import connectfour_network
import connectfour_functions
import connectfour

def client():
    ''' main program'''
    try:
        _welcome()
        name = str(_ask_for_username())
        
        # connect to server
        connection = connectfour_network.connect_to_server() 
        connectfour_network.server_messages(connection, name)

        # ai_game
        game_type(connection, name)

    except:
        print('An error occurred.')
        
    finally:
        print('Attempting to disconnect...')
        connectfour_network.close(connection)
        print('Disconnected!')


def game_type(connection: connectfour_network.connectfour_connection, name: str) -> None:
    ''' connect four game vs. AI if user inputs AI_GAME'''
    game = input('Enter [AI_GAME] to play vs. Artificial Intelligence:\n> ').upper()

    if game == 'AI_GAME':
        connectfour_network.send_and_read(connection, game)
        connectfour_functions.print_game_board(connectfour_functions.new_game())
        return user_interface(connection, name, connectfour_functions.new_game())
        
    else:
        print('Invalid game type. Please try again.')
        print()
        return game_type(connection, name)
    

def user_interface(connection: connectfour_network.connectfour_connection, username: str, game_state: connectfour.ConnectFourGameState) -> None:
    '''connect four artificial intelligence game'''        
    print('Enter DROP or POP followed by a column number.')
    user_input = input(username + '\'s turn (R): ')
    try:
        if user_input.split()[0].upper() == 'DROP':
            # user drops to game state 
            drop = connectfour_functions.drop_game_state(user_input, game_state)

            # prints game board
            connectfour_functions.print_game_board(drop)

            # sends message to server
            connectfour_network.write_line(connection, user_input)
            
            server_reply = connectfour_network.read_line(connection)
            print(server_reply)

            if _check_winner(server_reply):
                return None
            else:
                server_actions(connection, drop, username)

        elif user_input.split()[0].upper() == 'POP':
            # user pops to game state
            pop = connectfour_functions.pop_game_state(user_input, game_state)

            # prints game board
            connectfour_functions.print_game_board(pop)
            
            # sends message to server
            connectfour_network.write_line(connection, user_input)

            server_reply = connectfour_network.read_line(connection)
            print(server_reply)

            if  _check_winner(server_reply):
                return None
            else:
                server_actions(connection, pop, username)

        else:
            print('------------------------------')
            print('Invalid move, try again.')
            return user_interface(connection, username, game_state)

    except:
        print()
        print('Invalid move, try again.')
        return user_interface(connection, username, game_state)


        
def server_actions(connection: connectfour_network.connectfour_connection, game_state: connectfour.ConnectFourGameState, username: str):
    '''drops or pops to column number based on server message'''
    
    # reads message from server
    message = connectfour_network.read_line(connection)
    print(message)

    if message.split()[0] == 'DROP':
        # server drops to game state
        server_drop = connectfour_functions.drop_game_state(message, game_state)
        connectfour_functions.print_game_board(server_drop)
    
        server_reply = connectfour_network.read_line(connection)
        print(server_reply)

        if _check_winner(server_reply):
            return None
        else:
            return user_interface(connection, username, server_drop)


    elif message.split()[0] == 'POP':
        # server pops to game state
        server_pop = connectfour_functions.pop_game_state(message, game_state)
        connectfour_functions.print_game_board(server_pop)

        server_reply = connectfour_network.read_line(connection)
        print(server_reply)

        if _check_winner(server_reply):
            return None
        else:
            return user_interface(connection, username, server_pop)

def _check_winner(message: str) -> bool:
    ''' takes action based on server message'''
    if message == 'WINNER_RED' or message == 'WINNER_YELLOW':
        print('Goodbye!')
        return True
    else:
        return False 

def _welcome():
    ''' prints welcome statements'''
    print('----------------------------')
    print('Welcome to Connectfour game.')
    print('----------------------------')


def _ask_for_username() -> str:
    ''' asks user for username without tab and space'''
    print('Username cannot include whitespaces or tabs.')
    username = input('Enter username: ')

    if ' ' in username or '\t' in username:
        print()
        print('Please try again.')
        print()
        return _ask_for_username()
    return username

if __name__ == '__main__':
    client()
