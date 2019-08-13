from game import *


def test_car_1():
    car1 = Car("BX", 8, (7, 8), 0)
    for i in range(8):
        assert (7 + i, 8) == car1.car_coordinates()[i]

    assert "BX" == car1.get_name()

    assert "u" in car1.possible_moves()
    assert "d" in car1.possible_moves()
    assert "r" not in car1.possible_moves()
    assert "l" not in car1.possible_moves()
    assert 2 == len(car1.possible_moves())

    assert [(6, 8)] == car1.movement_requirements("u")
    assert [(15, 8)] == car1.movement_requirements("d")

    assert True is car1.move("u")
    assert (6, 8) == car1.car_coordinates()[0]

    assert False is car1.move("r")
    for i in range(8):
        assert (6 + i, 8) == car1.car_coordinates()[i]


def test_car_2():
    car1 = Car("G", 3, (0, 2), 1)
    for i in range(3):
        assert (0, 2+i) == car1.car_coordinates()[i]

    assert "G" == car1.get_name()

    assert "u" not in car1.possible_moves()
    assert "d" not in car1.possible_moves()
    assert "r" in car1.possible_moves()
    assert "l" in car1.possible_moves()
    assert 2 == len(car1.possible_moves())

    assert [(0, 5)] == car1.movement_requirements("r")
    assert [(0, 1)] == car1.movement_requirements("l")

    assert True is car1.move("l")
    assert (0, 1) == car1.car_coordinates()[0]


