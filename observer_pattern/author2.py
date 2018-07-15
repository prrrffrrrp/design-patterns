class Author:
    def __init__(self):
        self._info = None
        self._observers = set()

    def add_bookshop(self, observer):
        if not isinstance(observer, Bookshop):
            raise TypeError()
        self._observers.add(observer)

    def del_bookshop(self, observer):
        self._observers.remove(observer)

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer()


class Bookshop:
    def __init__(self, name, author):
        self._name = name
        self.author = author

    def __call__(self):
        print(self._name, 'has got the notification:', self.author.info)


writter = Author()

wro = Bookshop('Wro', writter)
wa = Bookshop('Wawa', writter)
kra = Bookshop('Kra', writter)


writter.add_bookshop(wro)
writter.add_bookshop(wa)

writter.info = 'My new book will be avaible soon'

writter.add_bookshop(kra)

writter.info = "I don't think i'll ever finish my book"

writter.del_bookshop(wa)

writter.info = "I'm done"

print(writter.info)
