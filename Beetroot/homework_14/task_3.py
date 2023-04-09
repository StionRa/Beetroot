# TV controller
#
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
class TVController:
    index = 0

    def __init__(self, channels):
        self.index = 0
        self.channels = channels

    def first_channel(self):
        TVController.index = 0
        return self.channels[TVController.index]

    def last_channel(self):
        TVController.index = len(self.channels) - 1
        return self.channels[TVController.index]

    def turn_channel(self, n):
        TVController.index = n - 1
        return self.channels[TVController.index]

    def next_channel(self):
        if TVController.index == 2:
            return self.first_channel()
        else:
            TVController.index += 1
        return self.channels[TVController.index]

    def previous_channel(self):
        if TVController.index == 0:
            return self.last_channel()
        else:
            TVController.index -= 1
        return self.channels[TVController.index]

    def current_channel(self):
        return self.channels[TVController.index]

    def is_exist(self, ch):
        x = 0 <= ch - 1 < len(self.channels) if isinstance(ch, int) else ch in self.channels
        return 'Yes' if x else 'No'


CHANNELS = ["BBC", "Discovery", "TV1000"]


controller = TVController(CHANNELS)

while True:
    choise = input(""" Welcome to TV controller
    To control the remote control, make a selection:
    1. first channel:
    2. last channel:
    3. turn on the selected channel 1 -"BBC", 2 - "Discovery", 3 - "TV1000":
    4. next channel:
    5. prev channel:
    6. current channel:
    7. to check if a channel with this number exists, enter any number:
    8. to check if a channel with this Name exists, enter any Name:
    9. To Exit from TV Controller
    """)
    if choise == "1":
        print(controller.first_channel())
    elif choise == "2":
        print(controller.last_channel())
    elif choise == "3":
        x = int(input("enter channel number from 1 to 3"))
        print(controller.turn_channel(x))
    elif choise == "4":
        print(controller.next_channel())
    elif choise == "5":
        print(controller.previous_channel())
    elif choise == "6":
        print(controller.current_channel())
    elif choise == "7":
        x = int(input("Enter channel number from 1 to 3"))
        print(controller.is_exist(x))
    elif choise == "8":
        y = input("Enter channel name BBC, Discovery, TV1000")
        print(controller.is_exist(y))
    elif choise == "9":
        print("BYE!!!")
        break
    else:
        print("Wrong Enter!!!")