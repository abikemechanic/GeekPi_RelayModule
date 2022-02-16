import time


class Relay:
    def __init__(self, relay_number):
        self.relay_number = relay_number
        self.state = 0
