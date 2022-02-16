import time
import smbus

from Relay import Relay


class RelayBoard:
    def __init__(self, device_address=0x10, device_bus=1):
        self.device_address = device_address
        self.device_bus = device_bus

        self.bus = smbus.SMBUS(self.device_bus)
        self.relay_list = list()
        for i in range(4):
            self.relay_list.append(Relay(i))

    def toggle(self, relay_number):
        state = self.relay_list[relay_number]
        if state:
            self.bus.write_byte_data(self.device_address, relay_number, 0x00)
        else:
            self.bus.write_byte_data(self.device_address, relay_number, 0xFF)

    def get_state(self, relay_number=None):
        if relay_number:
            return self.relay_list[relay_number].state
        else:
            return list(map(lambda a: a.state, self.relay_list))

    def set_state(self, state, relay_number=None):
        """
        sets the state of the relay to either on(1) or off(0)
        :param state: either 1 for one or 0 for off
        :param relay_number: the identifier of the relay (1, 2, 3, 4)
        :return: Nothing
        """

        if type(state) is str():
            state = state.lower()

        if state not in [1, 0, 'on', 'off']:
            raise ValueError('The value of state must be one of (1, 0, on, off)')

        if type(state) == list():
            for i in range(4):
                self.relay_list[i].state = state[i]

        elif type(relay_number) == int():
            if self.get_state() != state:
                self.toggle(relay_number)
                self.relay_list[relay_number].state = state
