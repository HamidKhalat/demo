#!/usr/bin/env python

from midiutil import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

mm = MIDIFile(1)
mm.addTempo(track,time,tempo)

for deg in degrees:
    mm.addNote(track,channel,deg,time,duration,volume)
    time = time + 1


with open("major-scale.sib", "wb") as output_file:
    mm.writeFile(output_file)