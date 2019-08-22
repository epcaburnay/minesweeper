class ScreenBoard:
    """Creates and updates the board on screen"""
    def __init__(self, ms_game):
        """Board settings"""
        self.ms = ms_game
        self.board_width = 10
        self.board_height = 10
        # Generates dashes that appears on screen
        self.board = [['-' for i in range(self.board_width)]
                      for j in range(self.board_height)]

    def print_board(self):
        """Prints the board on screen"""
        for i in range(self.board_width):
            for j in range(self.board_height):
                print(self.board[i][j], end=' ')

            print()

    def check_win_condition(self):
        counter = 0
        for i in range(self.board_width):
            for j in range(self.board_height):
                if self.board[i][j] == '-' or self.board[i][j] == 'F':
                    counter += 1
        if counter == self.ms.number_bombs:
            self.ms.clear()
            self.ms.minefield.reveal_field()
            print("You win!")
            self.ms.restart_game()
            return True
        else:
            return False

    def set_flag(self):
        """Sets a flag over a cell"""
        x_coord, y_coord = self.ms.input_coordinates()
        # If cell is not flagged, places flag on cell
        if self.board[x_coord][y_coord] == '-':
            self.board[x_coord][y_coord] = 'F'
        # Flag is undone
        elif self.board[x_coord][y_coord] == 'F':
            self.board[x_coord][y_coord] = '-'
        # Cannot flag revealed cells
        else:
            print("Cell cannot be flagged.")

    def open_cell(self):
        x_coord, y_coord = self.ms.input_coordinates()
        # check if cell is already open
        if self.board[x_coord][y_coord] != '-':
            print("That cell has already been opened!")
        # Check if opened cell is a mine
        elif self.ms.minefield.field[x_coord][y_coord] == '*':
            self.ms.clear()
            self.ms.minefield.reveal_field()
            print("Game over!")
            self.ms.restart_game()
        else:
            self.ms.minefield.flood_fill(x_coord, y_coord)
