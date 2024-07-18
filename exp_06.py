from music21 import stream, note, scale, key

# Create a stream
s = stream.Stream()

# Define the key signature (C Major)
k = key.KeySignature(0)
s.append(k)

# Create the C Major scale
major_scale = scale.MajorScale('C')

# Add the notes of the C Major scale to the stream
for pitch in major_scale.getPitches('C4', 'C5'):
    n = note.Note(pitch)
    s.append(n)

# Export to MusicXML
s.write('musicxml', 'major_scale.xml')
