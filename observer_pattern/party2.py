class Party:
    def __init__(self, place):
        self.place = place
        self._invite = None
        self._observers = set()

    def add_friend(self, friend):
        return self._observers.add(friend)

    def del_friend(self, friend):
        return self._observers.remove(friend)

    def send_invites(self, invite):
        self._invite = self.place + ': ' + invite
        for friend in self._observers:
            friend.invite = self._invite


class Friend:
    def __init__(self, name):
        self.name = name
        self.invite = "No party..."

    def show_invite(self):
        return self.invite


party = Party("Midnight Pub")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invites("Friday, 9:00 PM")
party.del_friend(nick)
party.send_invites("Saturday, 10:00 AM")
party.add_friend(chuck)

john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
chuck.show_invite() == "No party..."
