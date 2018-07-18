class Chat:
    def __init__(self):
        self.dialog = []

    def connect_human(self, human):
        human.chat = self
        print(human.name, 'connected')

    def connect_robot(self, robot):
        robot.chat = self
        print(robot.name, 'connected')

    def show_human_dialogue(self):
        human_dialogue = """"""
        for line in self.dialog:
            human_dialogue += line[0] + ' said: ' + line[1] + '\n'
        return human_dialogue[:-1]

    def show_robot_dialogue(self):
        vowels = 'aeiouAEIOU'
        robot_dialog = """"""
        for line in self.dialog:
            robot_dialog += line[0] + ' said: '
            for letter in line[1]:
                if letter in vowels:
                    robot_dialog += '0'
                else:
                    robot_dialog += '1'
            robot_dialog += '\n'

        return robot_dialog[:-1]

    def recv_message(self, name, message):
        self.dialog.append((name, message))


class Chatter:
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, message):
        self.chat.recv_message(self.name, message)


class Human(Chatter):
    pass


class Robot(Chatter):
    pass


chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")

chat.connect_human(karl)
chat.connect_robot(bot)

karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")

print(chat.show_human_dialogue())
print(chat.show_robot_dialogue())
assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""
