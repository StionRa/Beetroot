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
