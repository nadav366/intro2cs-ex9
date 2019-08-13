from helper import *
from car import *
from board import *
import sys

CORRECT_NAMES = "YBOGWR"
GET_INPUT = 'Please press car to move, direction ' \
            '("M" for all the legal moves)-'


VICTORY_MSG = "You won, well done!"
NON_MOVES_MSG = "There are no legal moves!"


class Game:
    """
    An object that is a rush-hour game.
    The object coordinates the game board, the participating teams,
    and the game rules.
    """

    def __init__(self, board):
        """
        Initialize new Game object and And places the legal vehicles in place
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        """
        Constitutes a queue in the game, receives input,
        checks it, and if necessary moves the appropriate vehicle.
        :return: True If the user won, False otherwise
        """
        print(self.__board)
        new_input = input(GET_INPUT)

        # Feature, printing a list of legal moves-
        if new_input == "M":
            self.__print_all_moves()
            return False

        if len(new_input) != 3 or new_input[1] != ",":
            print(ILLEGAL_INPUT_ERROR)
            return False

        self.__board.move_car(new_input[0], new_input[2])

        # Check if the move wins the game-
        if self.__board.cell_content(self.__board.target_location()) \
                is not None:
            print(VICTORY_MSG)
            return True

        return False

    def __print_all_moves(self):
        """
        A function that prints all the legal moves in the board
        :return: None
        """
        move_list = self.__board.possible_moves()
        for move in move_list:
            print("* The car", move[0], move[2])
        if len(move_list) == 0:
            print(NON_MOVES_MSG)

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        win = False
        while not win:
            win = self.__single_turn()

#####################################


def check_car_val(name, length, location, orientation):
    """
    A function that checks the legality of the vehicle-
    :param name: A string representing the car's name
    :param length: A positive int representing the car's length.
    :param location: A tuple representing the car head (row, col) location
    :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
    :return: True upon Vehicle location is valid, False otherwise
    """
    if name not in CORRECT_NAMES:
        return False

    if length < 2 or length > 4:
        return False

    if len(location) != 2:
        return False

    if orientation not in {0, 1}:
        return False
    return True


def add_cars(game_board):
    """
    A function that adds all valid cars to the clipboard from the
    resulting file.
    :param game_board: A board type object represents the game board
    """
    # Get the json file-
    json_loc = sys.argv[1]
    json_dict = load_json(json_loc)

    for name, inf_list in json_dict.items():
        if len(inf_list) != 3:
            continue
        length, location, orientation = inf_list
        if check_car_val(name, length, location, orientation):
            new_car = Car(name, length, location, orientation)
            game_board.add_car(new_car)


if __name__ == "__main__":
    game_board = Board()
    add_cars(game_board)
    one_game = Game(game_board)
    one_game.play()
