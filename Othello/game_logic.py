# Richard Lin

BLACK = 'B'
WHITE = 'W'

direction = [[0, -1], [0, 1], [-1, 0], [1, 0],
             [-1, -1], [-1, 1], [1, -1], [1, 1]]

class SpaceFilledError(Exception):
    pass

class InvalidMoveError(Exception):
    pass

class othello():
    ''' othello game logic '''   
    def __init__(self, row: int, column: int, first_player: str, top_left: str, winner: str) -> None:
        ''' initializes parameters '''
        self._board = []
        self._row = row
        self._column = column
        self._turn = first_player
        self._top_left = top_left
        self._winner = winner

# --------------- INITIALIZES GAME ---------------  
    def new_game_state(self) -> [[str]]:
        ''' creates new othello board game '''
        for row in range(self._row):
            self._board.append([])
            for column in range(self._column):
                self._board[-1].append('.')

    def top_left(self) -> [[str]]:
        ''' initializes first four colors on board '''
        r1, r2 = self._row // 2 - 1, self._row//2
        c1, c2 = self._column // 2 - 1, self._column // 2
        self._board[r1][c1] = self._board[r2][c2] = self._top_left
        self._board[r1][c2] = self._board[r2][c1] = self.get_opposite(self._top_left)

    def game(self, rc: [int]):
        ''' flip pieces and change turns '''
        self.flip_pieces(self.all_to_flip(rc[0], rc[1], direction))
        self.turn(rc[0], rc[1])
        self._turn = self.get_opposite(self._turn)
        
# --------------- GAME LOGIC ---------------    
    def valid_moves(self, turn: str) -> list:
        ''' goes through each item in game board and returns a list of valid
        moves '''
        valid_moves = []
        for row in range(self._row):
            for col in range(self._column):
                if self._board[row][col] == '.':
                    for dt in direction:
                        r = dt[0]
                        c = dt[1]
                        try:
                            if row + r >= 0 and col + c >= 0 and self._board[row+r][col+c] == self.get_opposite(turn):
                                while True:                                
                                    r += dt[0]
                                    c += dt[1]
                                    if row + r >= 0 and col + c >= 0:
                                        try:
                                            if self._board[row+r][col+c] == self.get_opposite(turn):
                                                pass
                                            elif self._board[row+r][col+c] == turn:
                                                valid_moves.append([row,col])
                                                break
                                            elif self._board[row+r][col+c] == '.':
                                                break      
                                        except:
                                            break                                   
                                    else:
                                        break
                        except:
                            pass
        return valid_moves
    
    def list_to_flip(self, row: int, column: int, direction: [[int]]) -> [[int]]:
        ''' takes a list of integers and returns a list of indexes to flip '''
        result = []
        r = 0
        c = 0
        while True:
            r += direction[0]
            c += direction[1]
            if row + r >= 0 and column + c >= 0:
                try:
                    if self._board[row+r][column+c] == self.get_opposite(self._turn):
                        result.append([row+r, column+c])
                    elif self._board[row+r][column+c] == self._turn:
                        return result
                    elif self._board[row+r][column+c] == '.':
                        return []
                except IndexError:
                    return []
            else:
                return []
                

    def all_to_flip(self, row: int, column: int, direction: [[int]]) -> [[int]]:
        ''' goes through each direction and returns a list of all pieces to
        flip '''
        list_to_flip = []
        for num in range(8):
            list_to_flip.extend(self.list_to_flip(row, column, direction[num]))
        return list_to_flip

    def flip_pieces(self, lst: [[int]]):
        ''' takes a list of indexes and flips all the pieces to the player's
        colors '''
        if len(lst) > 0:
            for item in lst: 
                self._board[item[0]][item[1]] = self._turn

    def turn(self, row: int, column: int) -> [[str]]:
        ''' changes a tile to the player's color '''
        self._board[row][column] = self._turn

    def determine_winner(self) -> str:
        ''' prints the winner of the game based on winner options '''
        if self._winner == 'L':
            if self.score(BLACK) > self.score(WHITE):
                return 'White wins!!!'                
            elif self.score(WHITE) > self.score(BLACK):
                return 'Black wins!!!'
            elif self.score(BLACK) == self.score(WHITE):
                return 'Tie game!'
        elif self._winner == 'M':
            if self.score(BLACK) < self.score(WHITE):
                return 'White wins!!!'       
            elif self.score(BLACK) > self.score(WHITE):
                return 'Black wins!!!'              
            elif self.score(BLACK) == self.score(WHITE):
                return 'Tie game!'
    
# --------------- CHECK TURNS AND SCORES ---------------
    def previous(self):
        self._noob = self._board
        self._board = self._noob
        return self._noob
    def change_turn(self) -> str:
        ''' changes turn '''
        if self._turn == BLACK:
            self._turn = WHITE
        else:
            self._turn = BLACK

    def get_opposite(self, turn: str) -> str:
        ''' takes a string and returns the opposite color of the string '''
        if turn == WHITE:
            return BLACK
        else:
            return WHITE

    def winner(self) -> str:
        ''' returns the winner option '''
        return self._winner
    
    def tl(self) -> str:
        ''' returns top left disc '''
        return self._top_left
    
    def player(self) -> str:
        ''' returns the player's turn '''
        return self._turn

    def game_board(self) -> [[str]]:
        ''' returns the game board '''
        return self._board

    def score(self, player: str) -> int:
        ''' takes a player and returns that player's score '''
        result = 0
        for row in self._board:
            result += row.count(player)
        return result
    
    def print_score(self) -> str:
        ''' prints the current score of the game '''
        print()
        print('---------- Scores ----------')
        print('White: ' +  str(self.score(WHITE)) + '     Black: ' + str(self.score(BLACK)))
        print('----------------------------')
