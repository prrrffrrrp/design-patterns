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


class Parameters(object):
    figure_class = None

    def __init__(self, param):
        self.param = param

    def constructor(self, param):
        self.param = param

    @staticmethod
    def choose_figure(figure):
        new_figure = type('new_figure', (figure,), {
            "__init__": constructor,
            "perimeter": perimeter,
            "volume": volume})
        cls.figure_class = new_figure

    @classmethod
    def perimeter(cls, param):
        return cls.figure_class.perimeter(param)

    @classmethod
    def volume(cls, param):
        return cls.figure_class.volume(param)


figure = Parameters(10)
repr(figure)

figure.choose_figure(Square())
print(figure.perimeter())

figure.choose_figure(Triangle())
print(figure.perimeter())
print(figure.volume())
