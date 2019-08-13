DIRECTIONS_DICT = {
    'u': "can move up",
    'd': "can to move down",
    'r': "can to move right",
    'l': "can to move left"
}

RIGHT = "r"
LEFT = "l"
UP = "u"
DOWN = "d"


class Car:
    """
    An object that is a "car" in a rush-hour game.
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        row, col = self.__location
        list_to_work = []
        if self.__orientation == 1:
            for i in range(self.__length):
                list_to_work.append((row, col + i))

        else:
            for i in range(self.__length):
                list_to_work.append((row + i, col))

        return list_to_work

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
         permitted by this car.
        """
        dict_to_work = {}

        if self.__orientation == 0:
            dict_to_work[UP] = DIRECTIONS_DICT[UP]
            dict_to_work[DOWN] = DIRECTIONS_DICT[DOWN]
        else:
            dict_to_work[LEFT] = DIRECTIONS_DICT[LEFT]
            dict_to_work[RIGHT] = DIRECTIONS_DICT[RIGHT]

        return dict_to_work

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        row, col = self.__location
        if movekey == LEFT:
            return [(row, col - 1)]
        if movekey == RIGHT:
            return [(row, col + self.__length)]
        if movekey == UP:
            return [(row - 1, col)]
        if movekey == DOWN:
            return [(row + self.__length, col)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey not in self.possible_moves():
            return False
        row, col = self.__location
        if movekey == UP:
            self.__location = (row - 1, col)
        elif movekey == DOWN:
            self.__location = (row + 1, col)
        elif movekey == LEFT:
            self.__location = (row, col - 1)
        elif movekey == RIGHT:
            self.__location = (row, col + 1)
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
