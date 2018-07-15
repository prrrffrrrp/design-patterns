class Parties:
    def __init__(self):
        self._invite = None
        self._observers = set()

    def add_friend(self, friend):
        return self._observers.add(friend)

    def del_friend(self, friend):
        if friend in self._observers:
            return self._observers.remove(friend)
        else:
            print("You don't have a friend named {} in your party list".format
                  (friend.name))

    def notify(self):
        for friend in self._observers:
            friend.update(self._invite)


class Party(Parties):
    def __init__(self, place):
        super().__init__()
        self.place = place

    def send_invites(self, invite):
        self._invite = self.place + ': ' + invite
        self.notify()


class Friend:
    def __init__(self, name):
        self.name = name
        self.invite = "No party..."

    def update(self, invite):
        self.invite = invite
        print('You have a new invite')

    def show_invite(self):
        print(self.invite)
        self.invite = "No party..."


party = Party("Midnight Pub")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")
adam = Friend("Adam")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invites("Friday, 9:00 PM")
party.del_friend(nick)
party.del_friend(adam)
party.send_invites("Saturday, 10:00 AM")
party.add_friend(chuck)

john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
chuck.show_invite() == "No party..."
