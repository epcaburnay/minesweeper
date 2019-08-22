import sys
from time import sleep
from os import system, name
from screen_board import ScreenBoard
from minefield import Minefield


class Minesweeper:
    """Creates text based Minesweeper game"""
    def __init__(self):
        self.screen_board = ScreenBoard(self)
        self.minefield = Minefield(self)
        self.number_bombs = 10
        # Generate bombs for minefield
        for bomb in range(self.number_bombs):
            self.minefield.generate_bombs()
        # Populate cells surrounding bombs
        self.minefield.populate_field()

    def run_game(self):
        # Game loop
        while True:
            self.clear()
            self.screen_board.print_board()
            self.input_action()
            # Checks if win condition is achieved
            if self.screen_board.check_win_condition():
                break

    def input_coordinates(self):
        """Asks for coordinates of the cell you want to open"""
        x_coord = self.check_input('row')
        y_coord = self.check_input('column')
        return x_coord, y_coord

    def input_action(self):
        """Asks input from player"""
        print("What would you like to do?")
        action = input("Input o to open cell, f to set flag, q to quit: ")
        if action.lower() == 'o':
            self.screen_board.open_cell()
        elif action.lower() == 'f':
            self.screen_board.set_flag()
        elif action.lower() == 'q':
            sys.exit()
        elif action.lower not in ['q', 'o', 'f']:
            print("Error: input is not valid.")
            sleep(2)

    def clear(self):
        """Clears the screen before the board is printed"""
        if name == 'nt':
            _ = system('cls')

    def check_input(self, coord_name):
        coord = input(f"Input {coord_name} coordinate from 0 to 9: ")
        try:
            coord = int(coord)
        except ValueError:
            print("Error! Invalid input.")
            coord = self.check_input(coord_name)
        else:
            if coord not in list(range(self.screen_board.board_width)):
                print("Input exceeds board dimensions.")
                coord = self.check_input(coord_name)
        finally:
            return coord

    def restart_game(self):
        """Asks if the player wants to play again"""
        choice = input("Do you want to restart the game? y/n: ")
        if choice.lower() == 'y':
            # Creates a new instance of the game if the choice is yes
            ms = Minesweeper()
            ms.run_game()
        elif choice.lower() == 'n':
            # Exits game if the choice is no
            sys.exit()
        else:
            print("Invalid input, exiting game.")
            sleep(10)
            sys.exit()


if __name__ == '__main__':
    ms = Minesweeper()
    ms.run_game()
