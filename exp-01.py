from music21 import stream, note, chord, converter

# Create a stream to hold the music elements
s = stream.Stream()

# Add some notes to the stream
s.append(note.Note("C4", quarterLength=1))
s.append(note.Note("D4", quarterLength=1))
s.append(note.Note("E4", quarterLength=1))
s.append(note.Note("F4", quarterLength=1))
s.append(note.Rest(quarterLength=1))
s.append(note.Note("G4", quarterLength=1))
s.append(note.Note("A4", quarterLength=1))
s.append(chord.Chord(["C4", "E4", "G4"], quarterLength=1))

# Display the music score
s.show('musicxml.png')


