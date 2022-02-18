from GeekPI_relay_module import RelayBoard
import time


relayBoard = RelayBoard()

for r in relayBoard.relay_list:
    relayBoard.turn_on(r)
    time.sleep(1)

for r in relayBoard.relay_list:
    relayBoard.turn_off(r)

