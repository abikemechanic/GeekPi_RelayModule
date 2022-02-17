import time


class Relay:
    def __init__(self, relay_number):
        self.relay_number = relay_number
        self.state = 0
        self._relay_id = ''

    @property
    def relay_id(self):
        return self._relay_id

    @relay_id.setter
    def relay_id(self, value):
        self._relay_id = value

