class Computer:
    def __init__(self):
        self.on = True

    def are_you_on(self):
        if self.on:
            return 'Yes'
        else:
            return 'No'


def is_computer_on():
    computer = Computer()
    return computer.are_you_on()
