from music21 import stream, chord, note

# Create a chord with the notes C4, E4, and G4
ch = chord.Chord(["C4", "E4", "G4"])

# Create a stream (score) and add the chord to it
score = stream.Score()
part = stream.Part()
part.append(ch)
score.append(part)

# Show the chord in text format (optional, for verification)
score.show('text')

# Write the score to a MusicXML file
score.write('musicxml', fp='chord_example.xml')

# Show the MusicXML (will open the default MusicXML viewer on your system)
score.show('musicxml')
