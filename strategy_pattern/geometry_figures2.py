class Figure(object):
    @staticmethod
    def perimeter(param):
        pass

    @staticmethod
    def volume(param):
        return 0


class Square(Figure):
    @staticmethod
    def perimeter(param):
        return param * 4


class Triangle(Figure):
    @staticmethod
    def perimeter(param):
        return param * 3


class Cube(Figure):
    @staticmethod
    def volume(param):
        return param ** 3


class Parameters(object):
    def __init__(self, param):
        if type(param) not in [float, int]:
            raise AttributeError
        else:
            self.param = param

        self.figure = None

    def choose_figure(self, figure):
        self.figure = figure

    def perimeter(self):
        result = self.figure.perimeter(self.param)
        return self.check_type(result)

    def volume(self):
        result = self.figure.volume(self.param)
        return self.check_type(result)

    @staticmethod
    def check_type(result):
        if type(result) is float:
            return float("{0:.2f}".format(result))
        return result


figure = Parameters(7.5673)
repr(figure)

print('Square')
figure.choose_figure(Square())
print(figure.perimeter())

print('Triangle:')
figure.choose_figure(Triangle())
print(figure.perimeter())
print(figure.volume())

print('Cube:')
figure.choose_figure(Cube())
print(figure.volume())
