from music21 import stream, note, key, pitch

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

# Export to MusicXML
s.write('musicxml', 'quarter_tone_scale1.xml')
