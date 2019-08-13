EMPTY_CELL = "_"
EMPTY_SRT = ""
NEW_LINE = "\n"
SPACE = " "

RIGHT = "r"
LEFT = "l"
UP = "u"
DOWN = "d"

CORECT_DIRC = RIGHT+LEFT+UP+DOWN

ILLEGAL_INPUT_ERROR = "Invalid input!"
ILLEGAL_MOVE_ERROR = "Invalid move!"
ILLEGAL_NAME_ERROR = "Invalid color input!"
ILLEGAL_DIRC_ERROR = "Invalid direction!"
NOT_EMPTY_CELL_ERROR = ("A selected cell is not empty! The car", "in it!")
OUT_MOVE_ERROR = "move out of board!"


class Board:
    """
    An object that is a rush-hour board.
    The object concentrates all the interactions between vehicles on the board,
    and their movement.
    """

    SIDE_LENGTH = 7
    VICTORY_CELL = (3, 7)

    def __init__(self):
        self.__board = [
            [EMPTY_CELL for i in range(self.SIDE_LENGTH)]
            for j in range(self.SIDE_LENGTH)
        ]
        self.__board[self.VICTORY_CELL[0]].append(EMPTY_CELL)
        self.__cars = dict()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        string = EMPTY_SRT
        for row_index in range(len(self.__board)):
            for cher in self.__board[row_index]:
                string += cher + SPACE
            if row_index == self.VICTORY_CELL[0]:
                string = string[0:-2]
                string += ">>"
            string += NEW_LINE
        return string

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cells_list = []
        for row in range(self.SIDE_LENGTH):
            for col in range(self.SIDE_LENGTH):
                cells_list.append((row, col))

        cells_list.append(self.VICTORY_CELL)
        return cells_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        list_to_fill = []
        for name, car in self.__cars.items():
            moves_per_car = car.possible_moves()

            for one_dirc in moves_per_car:
                row, col = car.movement_requirements(one_dirc)[0]
                if self.__in_empty_bord(row, col):
                    list_to_fill.append((name,
                                         one_dirc, moves_per_car[one_dirc]))
        return list_to_fill

    def __in_empty_bord(self, row, col):
        """
        A function that receives a coordinate (divided into row and column)
        and returns the parent cell to a table and blank.
        :param row: An integer, represents the quadratic row
        :param col: Integer, represents the column cordit
        :return: True If the cell exists and empty, another False
        """
        if (row, col) == self.VICTORY_CELL:
            return True

        if row < 0 or row >= self.SIDE_LENGTH or\
                col < 0 or col >= self.SIDE_LENGTH:
            return False

        if self.__board[row][col] != EMPTY_CELL:
            return False
        return True

    def target_location(self):
        """
        This function returns the coordinates of the location which is to
        be filled for victory.
        :return: (row,col) of goal location
        """
        return self.VICTORY_CELL

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row, col = coordinate
        if self.__board[row][col] == EMPTY_CELL:
            return None
        return self.__board[row][col]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        if car.get_name() in self.__cars:
            return False

        # Check that all the cells of the vehicle are exist and empty-
        for one_loc in car.car_coordinates():
            if one_loc not in self.cell_list():
                return False
            if self.cell_content(one_loc):
                return False

        for one_loc in car.car_coordinates():
            row, col = one_loc
            self.__board[row][col] = car.get_name()

        car_name = car.get_name()
        self.__cars[car_name] = car
        return True

    def __check_move(self, name, dirc):
        """
        A function that checks the integrity of the move-
        :param name: name of the car to move
        :param dirc: string representing the direction that user wants to move
        :return: True upon move is valid, False otherwise
        """

        if name not in self.__cars:
            print(ILLEGAL_NAME_ERROR)
            return False

        if dirc not in CORECT_DIRC:
            print(ILLEGAL_DIRC_ERROR)
            return False

        car = self.__cars[name]

        if dirc not in car.possible_moves():
            print(ILLEGAL_MOVE_ERROR)
            return False

        if car.movement_requirements(dirc)[0] not in self.cell_list():
            print(OUT_MOVE_ERROR)
            return False

        cell = self.cell_content(car.movement_requirements(dirc)[0])
        if cell:
            print(NOT_EMPTY_CELL_ERROR[0], cell, NOT_EMPTY_CELL_ERROR[1])
            return False

        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        if not self.__check_move(name, movekey):
            return False

        car = self.__cars[name]
        row, col = car.car_coordinates()[0]
        car.move(movekey)
        car_length = len(car.car_coordinates())

        if movekey == UP:
            self.__board[row - 1][col] = car.get_name()
            self.__board[row + car_length - 1][col] = EMPTY_CELL
        elif movekey == DOWN:
            self.__board[row + car_length][col] = car.get_name()
            self.__board[row][col] = EMPTY_CELL
        elif movekey == RIGHT:
            self.__board[row][col + car_length] = car.get_name()
            self.__board[row][col] = EMPTY_CELL
        elif movekey == LEFT:
            self.__board[row][col - 1] = car.get_name()
            self.__board[row][col + car_length - 1] = EMPTY_CELL
        return True
