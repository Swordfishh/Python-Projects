# Richard Lin

import game_logic
import tkinter

def othello_GUI():
    ''' runs othello main game '''
    gui = GUI()
    gui.start()
    OthelloApplication(gui.info()[0], gui.info()[1], gui.info()[2],
                       gui.info()[3], gui.info()[4]).start()

class GUI:
    def __init__(self) -> None:
        ''' initializes graphics user input '''
        self._even_list = ['4', '6', '8', '10', '12', '14', '16']        
        self._window = tkinter.Tk()
        
        # welcome label and entry
        welcome_label = tkinter.Label(self._window,
                                      text = 'Welcome to Othello',
                                      font = ('Helvetica', 20), width = 40)
        welcome_label.grid(row = 0, column = 0, columnspan = 3)
        
        # row label and entry      
        row_label = tkinter.Label(self._window, font = ('Helvetica', 12),
                                  text = 'Enter even row number (4-16)')
        row_label.grid(row=1, column=0)
        self._rowEnt = tkinter.Entry(self._window)
        self._rowEnt.grid(row = 1, column = 1)
        
        # column label and entry
        column_label = tkinter.Label(self._window, font = ('Helvetica', 12),
                                     text = 'Enter even column number (4-16)')
        column_label.grid(row=2, column=0)
        self._columnEnt = tkinter.Entry(self._window)
        self._columnEnt.grid(row = 2, column = 1)

        # first player label and entry
        fp_label = tkinter.Label(self._window, font = ('Helvetica', 12),
                                 text = 'Enter first player [B]lack or [W]hite')
        fp_label.grid(row = 3, column = 0)       
        self._fpEnt = tkinter.Entry(self._window)
        self._fpEnt.grid(row = 3, column = 1)

        # top left and entry
        top_left_label = tkinter.Label(self._window, font = ('Helvetica', 12),
                                       text = 'Enter top left color [B]lack or [W]hite')
        top_left_label.grid(row = 4, column = 0)
        self._top_leftEnt = tkinter.Entry(self._window)
        self._top_leftEnt.grid(row = 4, column = 1)

        # winner option label and entry
        winner_label = tkinter.Label(self._window, font = ('Helvetica', 12),
                                     text = '[M]ost discs wins or [L]east discs wins')
        winner_label.grid(row = 5, column = 0)
        self._winnerEnt = tkinter.Entry(self._window)
        self._winnerEnt.grid(row = 5, column = 1)

        # play button     
        play_button = tkinter.Button(self._window, text = 'Play',font = ('Helvetica', 12),
                                     command = self._play_game)
        play_button.grid(row = 6, column = 0, columnspan = 3)
        
        # Enter button
        self._window.bind('<Return>', self._on_enter_pressed)
    
    def _on_enter_pressed(self, event: tkinter.Event) -> None:
        ''' play command: destroys window only with valid input '''
        if self._rowEnt.get() in self._even_list\
           and self._columnEnt.get() in self._even_list\
           and self._fpEnt.get() in ['B', 'W', 'b', 'w']\
           and self._top_leftEnt.get() in ['B', 'W', 'b', 'w']\
           and self._winnerEnt.get() in ['L', 'M', 'l', 'm']:
            self._row = self._rowEnt.get()
            self._col = self._columnEnt.get()
            self._fp = self._fpEnt.get().upper()
            self._tl = self._top_leftEnt.get().upper()
            self._w = self._winnerEnt.get().upper()
            self._window.destroy()
        else:
            # if invalid input new window pops up specifying error
            self._error_window = tkinter.Toplevel()
            error_label = tkinter.Label(self._error_window,
                                        text = self._error_text(), font = ('Helvetica', 14), width = 40)
            error_label.grid(row = 0, column = 0)
            okay_button = tkinter.Button(self._error_window, text = 'Okay',
                                         command = self.error_window_command, font = ('Helvetica', 12))
            okay_button.grid(row = 1, column = 0, columnspan = 2)
            self._error_window.grab_set()
            self._error_window.wait_window()
            self._error_window.mainloop()

    def _play_game(self) -> None:
        ''' play command: destroys window only with valid input '''
        if self._rowEnt.get() in self._even_list\
           and self._columnEnt.get() in self._even_list\
           and self._fpEnt.get() in ['B', 'W', 'b', 'w']\
           and self._top_leftEnt.get() in ['B', 'W', 'b', 'w']\
           and self._winnerEnt.get() in ['L', 'M', 'l', 'm']:
            self._row = self._rowEnt.get()
            self._col = self._columnEnt.get()
            self._fp = self._fpEnt.get().upper()
            self._tl = self._top_leftEnt.get().upper()
            self._w = self._winnerEnt.get().upper()
            self._window.destroy()
        else:
            # if invalid input new window pops up specifying error
            self._error_window = tkinter.Toplevel()
            error_label = tkinter.Label(self._error_window,
                                        text = self._error_text(), font = ('Helvetica', 14), width = 40)
            error_label.grid(row = 0, column = 0)
            okay_button = tkinter.Button(self._error_window, text = 'Okay',
                                         command = self.error_window_command, font = ('Helvetica', 12))
            okay_button.grid(row = 1, column = 0, columnspan = 2)
            self._error_window.grab_set()
            self._error_window.wait_window()
            self._error_window.mainloop()

    def _error_text(self) -> str:
        ''' specifies error message '''
        if self._rowEnt.get() not in self._even_list:
            return 'Invalid row number.'
        if self._columnEnt.get() not in self._even_list:
            return 'Invalid column number.'
        if self._fpEnt.get() not in ['B', 'W']:
            return "Invalid first player.\nEnter 'B' for black and 'W' for white."
        if self._top_leftEnt.get() not in ['B', 'W']:
            return "Invalid top left color.\nEnter 'B' for black and 'W' for white."
        if self._winnerEnt.get() not in ['L', 'M']:
            return "Invalid winner option.\nEnter 'L' for least and 'M' for most."
    
    def error_window_command(self) -> None:
        ''' destroys error window '''
        self._error_window.destroy()
    
    def info(self) -> [[int and str]]:
        ''' returns a list of info '''
        return [int(self._row), int(self._col), self._fp, self._tl, self._w]    

    def start(self) -> None:
        ''' starts window '''
        self._window.mainloop()

class OthelloApplication:
    def __init__(self, row: int, column: int, first_player: str,
                 top_left: str, winner: str) -> None:
        ''' initializes game board '''
        self._row = row
        self._column = column       
        self._logic = game_logic.othello(row, column, first_player, top_left, winner)        
        self._root_window = tkinter.Tk()
        
        # canvas window
        self._canvas = tkinter.Canvas(self._root_window, width = 500, height = 500,
                                      borderwidth = 0, highlightthickness = 0.5,
                                      background = '#298500', highlightbackground = 'black')
        self._canvas.grid(row = 0, column = 0, padx = 0, pady = 0,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        # initializes game logic and gui
        self._logic.new_game_state()
        self._draw_lines()
        self._logic.top_left()
        self._top_left_pieces()
        self._turn_and_score()
        self._buttons()
        
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._canvas.bind('<Configure>', self._on_canvas_resized)

        self._root_window.bind('<Control-KeyPress-z>', self._on_z_pressed)
        self._root_window.bind('<Control-KeyPress-x>', self._on_x_pressed)
        self._root_window.bind('<Control-KeyPress-f>', self._on_f_pressed)
        
# -------------------- HANDLES CTRL-F --------------------
    def _on_f_pressed(self, event: tkinter.Event) -> None:
        ''' player forfeits ask if want to play game again '''
        self._forfeit_window = tkinter.Toplevel()
        forfeit_message = self._logic.player() + ' forfeits.\n' + self._logic.get_opposite(self._logic.player()) + ' wins!\n\n'\
		                  + 'Would you like to play again?'            
        forfeit_label = tkinter.Label(self._forfeit_window, text = forfeit_message, font = ('Helvetica', 14))
        forfeit_label.grid(row = 0, column = 0)
        yes_button = tkinter.Button(self._forfeit_window, text = 'Yes', font = ('Helvetica', 14),
                                    command = self._yes_clicked)
        yes_button.grid(row = 1, column = 0, padx = 25, sticky = tkinter.W)
        no_button = tkinter.Button(self._forfeit_window, text = 'No', font = ('Helvetica', 14),
                                   command = self._no_clicked)
        no_button.grid(row = 1, column = 0, padx = 30)
        cancel_button = tkinter.Button(self._forfeit_window, text = 'Cancel', font = ('Helvetica', 14),
                                       command = self._cancel_clicked) 
        cancel_button.grid(row = 1, column = 0, padx = 10, sticky = tkinter.E)
        
    def _yes_clicked(self):
        ''' new game '''
        self._forfeit_window.destroy()
        self._root_window.destroy()
        othello_GUI()
		
    def _no_clicked(self):
        ''' game over '''
        self._forfeit_window.destroy()
        self._root_window.destroy()
       
    def _cancel_clicked(self):
        ''' resumes game '''
        self._forfeit_window.destroy()    

# -------------------- HANDLES CTRL-Z --------------------       										
    def _on_z_pressed(self, event: tkinter.Event) -> None:
        ''' undo move '''
        self._canvas.delete(tkinter.ALL)
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        self._draw_resized_lines(width, height)
        print(self._noob)
        for r in range(self._row):
            for c in range(self._column):
                spot_coord = self._index_to_coord(width, height, [r, c])
                if self._noob[r][c] == 'B':
                    self._canvas.create_oval(
                        spot_coord[0], spot_coord[1],
                        spot_coord[2], spot_coord[3],
                        fill = '#000000', outline = '#000000')
                elif self._noob[r][c] == 'W':
                    self._canvas.create_oval(
                        spot_coord[0], spot_coord[1],
                        spot_coord[2], spot_coord[3],
                        fill = '#FFFFFF', outline = '#000000')
                        
    def _on_x_pressed(self, event: tkinter.Event) -> None:
        ''' create rectange of valid moves '''
        self._canvas.delete(tkinter.ALL)
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        self._draw_resized_lines(width, height)
        self._draw_resized_spots(width, height)
        self._draw_resized_squares(width, height)
        
    def _draw_resized_squares(self, width, height):
        ''' draws resized squares to indicate valid moves '''
        current = self._logic.valid_moves(self._logic.player())
        for valid_moves in current:
            rect_coord = self._index_to_coord(width, height, valid_moves)
            square = self._canvas.create_rectangle(rect_coord[0],
		             rect_coord[1], rect_coord[2], rect_coord[3],
		             fill = self._get_color(self._logic.player()))	
		
# -------------------- HANDLES CLICK ON CANVAS --------------------    
    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        ''' draws spot if click coordinate is valid move '''
        current = self._logic.valid_moves(self._logic.player())
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        move = self._coord_to_index(width, height, event.x, event.y)
        if move in current:
            self._graphics_othello(width, height, move)
            self._turn_and_score()

    def _draw_resized_spots(self, width: int, height: int) -> None:
        ''' draw resized spots based on game board '''
        for r in range(self._row):
            for c in range(self._column):
                spot_coord = self._index_to_coord(width, height, [r, c])
                if self._logic.game_board()[r][c] == 'B':
                    self._canvas.create_oval(
                        spot_coord[0], spot_coord[1],
                        spot_coord[2], spot_coord[3],
                        fill = '#000000', outline = '#000000')
                elif self._logic.game_board()[r][c] == 'W':
                    self._canvas.create_oval(
                        spot_coord[0], spot_coord[1],
                        spot_coord[2], spot_coord[3],
                        fill = '#FFFFFF', outline = '#000000')
                    
    def _graphics_othello(self, width, height, move):
        ''' adds and changes pieces on board based on click coordinate '''
        self._canvas.delete(tkinter.ALL)
        self._draw_resized_lines(width, height)
        self._logic.game(move)
        self._draw_resized_spots(width, height)               
        current = self._logic.valid_moves(self._logic.player())
        nxt = self._logic.valid_moves(self._logic.get_opposite(self._logic.player()))
        if not current and len(nxt) >= 1:
            self._logic.change_turn()
            self._turn_and_score()
            self._same_player_window()
        if not current and not nxt:
            self._winner_and_score()
            self._winner_window()

# -------------------- HANDLES CONFIGURATION ON CANVAS --------------------
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        ''' resizes the board '''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        self._draw_resized_lines(width, height)
        self._draw_resized_spots(width, height)
    
    def _draw_resized_lines(self, width: int, height: int) -> None:
        ''' draw resized lines '''
        self._canvas.delete(tkinter.ALL)
        coord = 0
        for c in range(self._column):
            coord += width/self._column
            self._canvas.create_line(coord, 0, coord, height, width = '2')
        coord = 0
        for r in range(self._row):
            coord += height/self._row
            self._canvas.create_line(0, coord, width, coord, width = '2')

# -------------------- PLAYER TURN AND SCORE --------------------
    def _turn_and_score(self) -> None:
        ''' label that prints player's turn and score '''
        window_text = self._full_player() + "'s turn.\n\n\n\nScores:\nBlack: "+ str(self._logic.score('B')) + '\nWhite: ' + str(self._logic.score('W')) + '\n\n\n\n' + self._abbrev_to_full()
        self._score = tkinter.Label(self._root_window, text = window_text,
                                    font = ('Helvetica', 12))
        self._score.grid(row = 0, column = 1, columnspan = 4, padx = 0, pady = 0,
                         sticky = tkinter.N)

    def _winner_and_score(self) -> None:
        ''' label that prints winner and score '''
        window_text = self._logic.determine_winner() + '\n\n\n\nScores:\nBlack: '+ str(self._logic.score('B')) + '\nWhite: ' + str(self._logic.score('W')) + '\n\n\n\n' + self._abbrev_to_full()
        self._score = tkinter.Label(self._root_window, text = window_text,
                        font = ('Helvetica', 12))
        self._score.grid(row = 0, column = 1, columnspan = 4, padx = 0, pady = 0,
                        sticky = tkinter.N)

    def _full_player(self) -> str:
        ''' returns the full color name of player's turn '''
        if self._logic.player() == 'B':
            return 'Black'
        else:
            return 'White'
    
    def _abbrev_to_full(self) -> str:
        ''' returns the winner option '''
        if self._logic.winner() == 'L':
            return 'Winner: LEAST discs.'
        else:
            return 'Winner: MOST discs.'

# -------------------- EXIT/NEW GAME/INSTRUCTION BUTTONS --------------------       										
    def _buttons(self) -> None:
        ''' creates exit and new game button '''
        self._instruction_button = tkinter.Button(self._root_window, text = 'Rules', font = ('Helvetica', 12),
                                                 command = self._on_instruction_clicked)
        self._instruction_button.grid(row = 0, column = 1, sticky = tkinter.S)
        self._exit_button = tkinter.Button(self._root_window, text = 'Exit', font = ('Helvetica', 12),
                                     command = self._on_exit_clicked)
        self._exit_button.grid(row = 1, column = 1, columnspan = 4, sticky = tkinter.SW)
        new_game_button = tkinter.Button(self._root_window, text = 'New Game', font = ('Helvetica', 12),
                                         command = self._on_new_game_clicked)
        new_game_button.grid(row = 1, column = 1, columnspan = 4, sticky = tkinter.SE)
        
    def _on_instruction_clicked(self) -> None:
        ''' displays a window that shows the instructions '''
        self._instruction_window = tkinter.Toplevel()
        instruction_message = '1. Black always moves first.\n\
                               2. If on your turn you cannot outflank and flip at least one opposing disc, your turn is forfeited and\n   \
                               your opponent moves again. However, if a move is available to you, you may not forfeit your turn.\n\
                               3. A disc may outflank any number of discs in one or more rows in any number of directions at the same\n   \
                               time - horizontally, vertically or diagonally. (A row is defined as one or more discs in a continuous straight line)\n\
                               4. You may not skip over your own colour disc to outflank an opposing disc.\n\
                               5. Discs may only be outflanked as a direct result of a move and must fall in the direct line of the disc placed down.\n\
                               6. All discs outflanked in any one move must be flipped, even if it is to the player\'s advantage not to flip them at all.\n\
                               7. A player who flips a disc which should not have been turned may correct the mistake as long as the opponent\n   \
                               has not made a subsequent move. If the opponent has already moved, it is too late to change and the disc(s) remain as is.\n\
                               8. Once a disc is placed on a square, it can never be moved to another square later in the game.\n\
                               9. If a player runs out of discs, but still has an opportunity to outflank an opposing disc on his or her turn,\n   \
                               the opponent must give the player a disc to use. (This can happen as many times as the player needs and can use a disc).\n\
                               10. When it is no longer possible for either player to move, the game is over. Discs are counted and the player with\n   \
                               the majority of his or her colour discs on the board is the winner.'
        instruction_label = tkinter.Label(self._instruction_window,
                                          text = instruction_message, font = ('Helvetica', 11))
        instruction_label.grid(row = 0, column = 0 , sticky = tkinter.W)
        okay_button = tkinter.Button(self._instruction_window, text = 'Okay',
                                     command = self._okay_instruction_clicked)
        okay_button.grid(row = 1, column = 0)
        
    def _okay_instruction_clicked(self) -> None:
        self._instruction_window.destroy()

    def _on_exit_clicked(self) -> None:
        ''' new window appears saying are you sure you want to exit game '''
        self._exit_game = tkinter.Toplevel()
        exit_game_message = tkinter.Label(self._exit_game, text = 'Are you sure you want to exit?',
                               font = ('Helvetica', 14))
        exit_game_message.grid(row = 0, column = 0)
        yes_button = tkinter.Button(self._exit_game, text = 'Yes', font = ('Helvetica', 14),
                                    command = self._on_exit_yes_clicked)
        yes_button.grid(row = 1, column = 0, sticky = tkinter.SW)
        no_button = tkinter.Button(self._exit_game, text = 'No', font = ('Helvetica', 14),
                                   command = self._on_exit_no_clicked)
        no_button.grid(row = 1, column = 0, sticky = tkinter.SE)
        self._exit_game.grab_set()
        self._exit_game.wait_window()
        self._exit_game.mainloop()
                										
    def _on_exit_yes_clicked(self) -> None:
        ''' exits game '''
        self._exit_game.destroy()
        self._root_window.destroy()
		
    def _on_exit_no_clicked(self) -> None:
        ''' resumes the game '''
        self._exit_game.destroy()
		
    def _on_new_game_clicked(self) -> None:
        ''' new window appears saying are you sure you want to creates new game '''
        self._new_game = tkinter.Toplevel()
        new_game_message = tkinter.Label(self._new_game, text = 'Are you sure you want to create new game?',
                               font = ('Helvetica', 14))
        new_game_message.grid(row = 0, column = 0)
        yes_button = tkinter.Button(self._new_game, text = 'Yes', font = ('Helvetica', 14),
                                    command = self._on_new_game_yes_clicked)
        yes_button.grid(row = 1, column = 0, sticky = tkinter.SW)
        no_button = tkinter.Button(self._new_game, text = 'No', font = ('Helvetica', 14),
                                   command = self._on_new_game_no_clicked)
        no_button.grid(row = 1, column = 0, sticky = tkinter.SE)
        self._new_game.grab_set()
        self._new_game.wait_window()
        self._new_game.mainloop()
		
    def _on_new_game_yes_clicked(self) -> None:
        ''' creates new game '''
        self._new_game.destroy()
        self._root_window.destroy()
        othello_GUI()
		
    def _on_new_game_no_clicked(self) -> None:
        ''' resumes to game '''
        self._new_game.destroy()
                
# -------------------- DEALS WITH POP-UP WINDOWS --------------------
    def _winner_window(self) -> None:
        ''' top pop up window that shows winner and option to play again '''
        self._w_window = tkinter.Toplevel()
        message = self._logic.determine_winner() + '\n~~~ Congratulations! ~~~\n\nWould you like to play again?'
        w_label = tkinter.Label(self._w_window, text = message,
                                font = ('Helvetica', 14), width = 50)
        w_label.grid(row = 0, column = 0)
        yes_button = tkinter.Button(self._w_window, text = 'Yes', font = ('Helvetica', 12),
                                    command = self._yes_command)
        yes_button.grid(row = 1, column = 0, sticky = tkinter.W, padx = 230)
        no_button = tkinter.Button(self._w_window, text = 'No', font = ('Helvetica', 12),
                                   command = self._no_command)
        no_button.grid(row = 1, column = 0, sticky = tkinter.E, padx = 230)
        self._w_window.grab_set()
        self._w_window.wait_window()
        self._w_window.mainloop()
        
    def _yes_command(self) -> None:
        ''' new game '''
        self._w_window.destroy()
        self._root_window.destroy()
        othello_GUI()
        
    def _no_command(self) -> None:
        ''' game over '''
        self._w_window.destroy()
        self._root_window.destroy()
            
    def _same_player_window(self) -> None:
        ''' top pop up window indicating same player moves AGAIN '''
        self._sp_window = tkinter.Toplevel()
        message = self._full_player() +'\'s turn AGAIN because ' + self._logic.get_opposite(self._logic.player()) + ' doesn\'t any have VALID moves.'
        sp_label = tkinter.Label(self._sp_window, text = message,
                                 font = ('Helvetica', 14), width = 50)
        sp_label.grid(row = 0, column = 0)
        okay_button = tkinter.Button(self._sp_window, text = 'Okay',
                                     command = self._sp_window_command, font = ('Helvetica', 12))
        okay_button.grid(row = 1, column = 0, columnspan = 2)
        self._sp_window.grab_set()
        self._sp_window.wait_window()
        self._sp_window.mainloop()

    def _sp_window_command(self) -> None:
        ''' destroys same player window '''
        self._sp_window.destroy()        

# -------------------- COORD TO INDEX AND VICE VERSA --------------------
    def _coord_to_index(self, width, height, x_coord, y_coord) -> [int]:
        ''' returns the index of the click coordinate '''
        width_square, height_square = width/self._column, height/self._row
        C=0
        for r in range(self._row):
            R=0
            C+=1
            for c in range(self._column):
                R+=1
                if x_coord in range(int(width_square*(R-1)), int(width_square*(R)))\
                and y_coord in range(int(height_square*(C-1)), int(height_square*(C))):
                    return [r,c]

    def _index_to_coord(self, width, height, rc:[int]) -> [int and float]:
        ''' returns the create oval coordinates of an index '''
        width_square, height_square = width/self._column, height/self._row
        top_x = width_square * rc[1] + 8
        top_y = height_square * rc[0] + 8
        bottom_x = width_square * (rc[1] +1) - 8
        bottom_y = height_square * (rc[0] +1) - 8
        return [top_x, top_y, bottom_x, bottom_y]


# -------------------- INITIALIZE BOARD WITH ITEMS --------------------
    def _draw_lines(self) -> None:
        ''' initially draws lines on canvas '''
        coord = 0
        for c in range(self._column):
            coord += 502/self._column
            self._canvas.create_line(coord, 0, coord, 502, width = '2')
        coord = 0
        for r in range(self._row):
            coord += 502/self._row
            self._canvas.create_line(0, coord, 502, coord, width = '2')
            
    def _top_left_pieces(self) -> None:
        ''' initially draws four top left spots on canvas '''
        self._canvas.create_oval(502/self._column*(self._column/2-1)+8, 502/self._row*(self._row/2-1) + 8,
                                 502/self._column*(self._column/2) - 8, 502/self._row*(self._row/2) - 8,
                                 fill = self._get_color(self._logic.tl()), outline = '#000000')
        self._canvas.create_oval(502/self._column*(self._column/2)+8, 502/self._row*(self._row/2) +8,
                                 502/self._column*(self._column/2+1)-8, 502/self._row*(self._row/2+1)-8,
                                 fill = self._get_color(self._logic.tl()), outline = '#000000')
        self._canvas.create_oval(502/self._column*(self._column/2-1)+8, 502/self._row*(self._row/2) +8,
                                 502/self._column*(self._column/2) - 8, 502/self._row*(self._row/2+1)-8,
                                 fill = self._get_color(self._logic.get_opposite(self._logic.tl())), outline = '#000000')
        self._canvas.create_oval(502/self._column*(self._column/2)+8, 502/self._row*(self._row/2-1) + 8,
                                 502/self._column*(self._column/2+1)-8, 502/self._row*(self._row/2) - 8,
                                 fill = self._get_color(self._logic.get_opposite(self._logic.tl())), outline = '#000000')
        
    def _get_color(self, color: str) -> str:
        ''' returns spot color based on black or white '''
        if color == 'B':
            return '#000000'
        else:
            return '#FFFFFF'
        
# -------------------- MAINLOOP --------------------
    def start(self) -> None:
        ''' starts root window '''
        self._root_window.mainloop()        

if __name__ == '__main__':
    othello_GUI()
    
    
