import rtmidi
import time

midiout = rtmidi.MidiOut()
ports = midiout.get_ports()
print(ports)
midiout.open_port(5)


with midiout:
    note_on = [0x90, 60, 100]
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
    time.sleep(0.8)
    midiout.send_message(note_off)
    time.sleep(0.5)
    midiout.send_message(note_on)
    time.sleep(0.8)
    midiout.send_message(note_off)
    time.sleep(0.5)
