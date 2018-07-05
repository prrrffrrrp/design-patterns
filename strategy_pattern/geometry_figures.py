###########################################################################
#  You often work with the different geometrical figures and with their
#  parameters - the perimeter, area, and volume. You are tired of doing it
#  manually, so you’ve decided to automate this process, and therefore you
#  need to write a particular program. In this program you should create
#  the class Parameters which will choose one of the few figures (the CIRCLE,
#  RIGHT TRIANGLE, SQUARE, RIGHT PENTAGON, RIGHT HEXAGON, CUBE) using the
#  choose_figure() method and will count the perimeter, area,
#  and volume with the help of the following methods:
#
#      perimeter() - returns the perimeter of the figure;
#      area() - returns the area of the figure;
#      volume() - returns the volume of the figure.
#
#  Also you have to create a class for each figure and use the Strategy
#  design pattern to solve this mission.
#  Every figure, except the cube, has the volume = 0.
#  If the result has no decimal places, you should return it as int(),
#  in other case - round it to the 2 decimal points.
############################################################################
import math


class Figure(object):
    @staticmethod
    def volume(self):
        return 0


class Circle(Figure):
    @staticmethod
    def perimeter(param):
        print('Circle perimeter: pi x diameter')
        return math.pi * param

    @staticmethod
    def area(param):
        pass


class Triangle(Figure):
    @staticmethod
    def perimeter(param):
        print("Triangle perimeter: a + b + c")
        return param * 3

    @staticmethod
    def area(param):
        pass


class Square(Figure):
    @staticmethod
    def perimeter(param):
        print("Square perimeter: a x 4")
        return param * 4

    @staticmethod
    def area(param):
        pass


class Pentagon(Figure):
    @staticmethod
    def perimeter(param):
        pass

    @staticmethod
    def area(param):
        pass


class Hexagon(Figure):
    @staticmethod
    def perimeter(param):
        pass

    @staticmethod
    def area(param):
        pass


class Cube(Figure):
    @staticmethod
    def perimeter(param):
        pass

    @staticmethod
    def area(self):
        pass

    @staticmethod
    def volume(param):
        return param ** 3


class Parameters:
    def __init__(cls, param):
        cls.param = param

    @classmethod
    def choose_figure(cls, figure_class):
        return figure_class


###########################################################################
figure = Parameters(10)

figure.choose_figure(Circle())
figure.area() == 314.16

figure.choose_figure(Triangle())
figure.perimeter() == 30

figure.choose_figure(Square())
figure.area() == 100

figure.choose_figure(Pentagon())
figure.perimeter() == 50

figure.choose_figure(Hexagon())
figure.perimeter() == 60

figure.choose_figure(Cube())
figure.volume() == 1000

