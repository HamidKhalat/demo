from music21 import stream, note, key, pitch, environment
from midi2audio import FluidSynth

# Create a stream
s = stream.Stream()

# Define the key signature (C Major)
k = key.KeySignature(0)
s.append(k)

# Define the pitches for a C Major scale with quarter-tone subdivisions
quarter_tone_intervals = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
base_note = pitch.Pitch('C4')

for interval in quarter_tone_intervals:
    p = base_note.transpose(interval)
    n = note.Note(p)
    n.quarterLength = 1  # Set the duration of each note
    s.append(n)

# Set the path to MuseScore executable
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/Applications/MuseScore 3.app/Contents/MacOS/mscore'  # Adjust this path

# Export to PNG
png_filename = 'quarter_tone_scale.png'
s.write('musicxml.png', fp=png_filename)

# Export to MIDI
midi_filename = 'quarter_tone_scale.mid'
s.write('midi', fp=midi_filename)

# Convert MIDI to audio (WAV format)
fs = FluidSynth()
wav_filename = 'quarter_tone_scale.wav'
fs.midi_to_audio(midi_filename, wav_filename)

print(f"PNG score saved as {png_filename}")
print(f"MIDI file saved as {midi_filename}")
print(f"WAV audio file saved as {wav_filename}")
