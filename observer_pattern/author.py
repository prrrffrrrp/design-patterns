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

    def set_info(self, info):
        self._info = info
        self.notify(info)

    def notify(self, info):
        for observer in self._observers:
            observer.update(info)


class Bookshop:
    def __init__(self, name):
        self._name = name

    def update(self, info):
        print(self._name, 'has got the notification:', info)


wro = Bookshop('Wro')
wa = Bookshop('Wawa')
kra = Bookshop('Kra')


writter = Author()

writter.add_bookshop(wro)
writter.add_bookshop(wa)

writter.set_info('My new book will be avaible soon')

writter.add_bookshop(kra)

writter.set_info("I don't think i'll ever finish my book")

writter.del_bookshop(wa)

writter.set_info("I'm done")

print(writter._info)
