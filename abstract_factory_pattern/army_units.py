class Army(object):
    def train_swordsman(self):
        raise NotImplementedError()

    def train_lancer(self):
        raise NotImplementedError()

    def train_archer(self):
        raise NotImplementedError()


class Soldier(object):
    def __init__(self):
        self._name = None
        self._army_type = None
        self._type = None
        self._local_type = None

    #  def __str__(self):
    #      return (self._local_type + ' ' +
    #              self._name + ', ' +
    #              self._army_type + ' ' +
    #              self._type.lower())

    def introduce(self):
        return (self._local_type + ' ' +
                self._name + ', ' +
                self._army_type + ' ' +
                self._type.lower())


class Swordsman(Soldier):
    def __init__(self, name, army_type, local_type):
        self._name = name
        self._army_type = army_type
        self._type = self.__class__.__name__
        self._local_type = local_type


class Lancer(Soldier):
    def __init__(self, name, army_type, local_type):
        self._name = name
        self._army_type = army_type
        self._type = self.__class__.__name__
        self._local_type = local_type


class Archer(Soldier):
    def __init__(self, name, army_type, local_type):
        self._name = name
        self._army_type = army_type
        self._type = self.__class__.__name__
        self._local_type = local_type


class EuropeanArmy(Army):
    def __init__(self):
        self.army_type = 'European'

    def train_swordsman(self, name):
        local_type = 'Knight'
        return Swordsman(name, self.army_type, local_type)

    def train_lancer(self, name):
        local_type = 'Raubritter'
        return Lancer(name, self.army_type, local_type)

    def train_archer(self, name):
        local_type = 'Ranger'
        return Archer(name, self.army_type, local_type)


class AsianArmy(Army):
    def __init__(self):
        self.army_type = 'Asian'

    def train_swordsman(self, name):
        local_type = 'Samurai'
        return Swordsman(name, self.army_type, local_type)

    def train_lancer(self, name):
        local_type = 'Ronin'
        return Lancer(name, self.army_type, local_type)

    def train_archer(self, name):
        local_type = 'Shinobi'
        return Archer(name, self.army_type, local_type)


my_army = EuropeanArmy()
enemy_army = AsianArmy()

soldier_1 = my_army.train_swordsman("Jaks")
soldier_2 = my_army.train_lancer("Harold")
soldier_3 = my_army.train_archer("Robin")

soldier_4 = enemy_army.train_swordsman("Kishimoto")
soldier_5 = enemy_army.train_lancer("Ayabusa")
soldier_6 = enemy_army.train_archer("Kirigae")

assert soldier_1.introduce() == "Knight Jaks, European swordsman"
assert soldier_2.introduce() == "Raubritter Harold, European lancer"
assert soldier_3.introduce() == "Ranger Robin, European archer"

print(soldier_4.introduce())
assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
