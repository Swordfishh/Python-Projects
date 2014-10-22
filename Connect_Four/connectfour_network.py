#Richard Lin

import collections
import socket


connectfour_connection = collections.namedtuple(
    'connectfour_connection',
    ['socket', 'socket_input', 'socket_output'])


def send_and_read(connection: connectfour_connection, message: str) -> str:
    '''sends messages to and reads messages from server'''
    write_line(connection, message)
    print(read_line(connection))
    

def server_messages(connection: connectfour_connection, username: str) -> str:
    '''
    Server returns messages based on user input
    '''
    write_line(connection, 'I32CFSP_HELLO ' + username)
    print('I32CFSP_HELLO ' + username)
    print(read_line(connection))
    print()


def connect_to_server() -> connectfour_connection:
    '''creates socket to connect based on user input host and port number'''
    try:
        print()
        HOST = input('Enter a host server name: ')
        PORT = int(input('Enter a host port number: ' ))
        print()
        connectfour_socket = socket.socket()
        connectfour_socket.connect((HOST, PORT))
        print('Successfully connected to server!')
        connectfour_socket_input = connectfour_socket.makefile('r')
        connectfour_socket_output = connectfour_socket.makefile('w')

    except ConnectionRefusedError:
        print('Connection refused. Check VPN and try again.')
        return connect_to_server()
        
    except:
        print('Invalid host name or port number Try again.')
        return connect_to_server()
        
    else:
        
        return connectfour_connection(
            socket = connectfour_socket,
            socket_input = connectfour_socket_input,
            socket_output = connectfour_socket_output)


def close(connection: connectfour_connection) -> None:
    'closes the connection to the connectfour server'
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()


def read_line(connection: connectfour_connection) -> str:
    '''reads a line of text sent from the server and returns it without
    a newline on the end of it'''

    return connection.socket_input.readline()[:-1]


def write_line(connection: connectfour_connection, line: str) -> None:
    '''writes a line of text to the server, including the appropriate
    newline sequence'''
    connection.socket_output.write(line + '\r\n')
    connection.socket_output.flush()


