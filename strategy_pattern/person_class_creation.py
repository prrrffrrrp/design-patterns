class Person(object):
    @classmethod
    def spawn(cls, firstname, lastname, **attributes):
        new_class = type(lastname, (cls,), attributes)
        globals()[lastname] = new_class
        return new_class(firstname)

    def __init__(self, firstname):
        self.firstname = firstname

    def say_hi(self, to_person):
        print("Hi {}".format(to_person.wholename()))

    def wholename(self):
        return "{} {}".format(
            self.firstname.capitalize(),
            self.__class__.__name__
        )


def punch(self, person):
    print("{} punched {}! ({} damage)".format(
        self.wholename(),
        person.wholename(),
        self.punch_damage
    ))


def kick(self, person):
    print("{} kicked {}! ({} damage)".format(
        self.wholename(),
        person.wholename(),
        self.kick_damage
    ))


#########################################################

frank = Person.spawn("Frank", "Puncherson",
                     punch_damage=10,
                     punch=punch
                     )
harold = Person.spawn("Harold", "Hill")

frank.punch(harold)

franks_bro = Puncherson("Ralph")
franks_bro.punch(harold)

harold.say_hi(frank)
