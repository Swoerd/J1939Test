import can
import j1939

bus1 = can.interface.Bus('test', bustype='virtual', preserve_timestamps=True)
bus2 = can.interface.Bus('test', bustype='virtual')

msg1 = can.Message(timestamp=100000, arbitration_id=0x0CF004, data=[1,2,3, 4, 5, 6, 8, 10])

# Berichten verzonden op bus1 zullen hun timestamps vast houden wanneer deze ontvangen worden op bus 2
bus1.send(msg1)
msg2 = bus2.recv()

assert msg1.arbitration_id == msg2.arbitration_id
assert msg1.data == msg2.data
assert msg1.timestamp == msg2.timestamp

# Berichten verzonden op bus2 zullen hun timestamps niet vast houden wanneer deze ontvangen worden op bus 1
bus2.send(msg1)
msg3 = bus1.recv()

assert msg1.arbitration_id == msg3.arbitration_id
assert msg1.data == msg3.data
assert msg1.timestamp != msg3.timestamp

print("Message 1:", msg1)
print("Arbitration ID:", msg1.arbitration_id)
print("Data:", msg1.data)
print("Timestamp:", msg1.timestamp)
#print("PGN:", msg1.pgn)

print("Message 2:", msg2)
print("Arbitration ID:", msg2.arbitration_id)
print("Data:", msg2.data)
print("Timestamp:", msg2.timestamp)
#print("PGN:", msg1.pgn)

print("Message 3:", msg3)
print("Arbitration ID:", msg3.arbitration_id)
print("Data:", msg3.data)
print("Timestamp:", msg3.timestamp)
#print("PGN:", msg1.pgn)