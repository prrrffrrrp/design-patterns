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

class Figure(object):
    def __init__(self, param):
        self._param = param


class Circle:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle:
    def perimeter(self):
        pass

    def area(self):
        pass










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

