import random


class Minefield:
    """Creates the underlying minefield not shown on screen"""

    def __init__(self, ms_game):
        self.mineboard = ms_game.screen_board
        self.field = [[0 for i in range(self.mineboard.board_width)]
                      for j in range(self.mineboard.board_height)]
        self.bomb_x_coord = []
        self.bomb_y_coord = []

    def generate_bombs(self):
        """Function that randomizes bombs"""
        x_coord = random.randrange(self.mineboard.board_width)
        y_coord = random.randrange(self.mineboard.board_height)
        # Checks if there is already a bomb in the coordinate
        if self.field[x_coord][y_coord] != '*':
            self.field[x_coord][y_coord] = '*'
            # Updates list of the bombs' x and y coordinates
            self.bomb_x_coord.append(x_coord)
            self.bomb_y_coord.append(y_coord)
        else:
            self.generate_bombs()

    def reveal_field(self):
        """Reveals the minefield if the player wins or loses"""
        for i in range(self.mineboard.board_width):
            for j in range(self.mineboard.board_height):
                print(self.field[i][j], end=' ')

            print()

    def populate_field(self):
        """Adds 1 to cells next to bombs"""
        for coord in range(len(self.bomb_x_coord)):
            for i in range(self.bomb_x_coord[coord] - 1,
                           self.bomb_x_coord[coord] + 2):
                # check if x coord exceeds board index
                if i < 0 or i > self.mineboard.board_width - 1:
                    continue
                for j in range(self.bomb_y_coord[coord] - 1,
                               self.bomb_y_coord[coord] + 2):
                    # check if y coord exceeds board index
                    if j < 0 or j > self.mineboard.board_height - 1:
                        continue
                    elif self.field[i][j] == '*':
                        continue
                    else:
                        self.field[i][j] += 1

    def flood_fill(self, x, y):
        """Opens adjacent cells if the selected cell == 0"""
        # Assign selected cell from minefield to screen board
        self.mineboard.board[x][y] = self.field[x][y]
        # open all surrounding cells if selected cell == 0
        if self.field[x][y] == 0:
            for i in range(x - 1, x + 2):
                if i < 0 or i > self.mineboard.board_width - 1:
                    continue
                for j in range(y - 1, y + 2):
                    if j < 0 or j > self.mineboard.board_height - 1:
                        continue
                    elif self.mineboard.board[i][j] != '-':
                        continue
                    else:
                        self.flood_fill(i, j)
