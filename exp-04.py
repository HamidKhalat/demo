from music21 import stream, chord, note, metadata, converter


# Function to generate chords as music21 chord objects
def generate_chords():
    chords = [
        chord.Chord(["C4", "E4", "G4"]),
        chord.Chord(["G3", "B3", "D4"]),
        chord.Chord(["A3", "C4", "E4"]),
        chord.Chord(["F3", "A3", "C4"]),
        chord.Chord(["D3", "F3", "A3"]),
        chord.Chord(["E3", "G#3", "B3"]),
        chord.Chord(["A3", "C#4", "E4"])
    ]
    return chords

# Create a music21 stream to hold the score
score = stream.Score()

# Add metadata
score.metadata = metadata.Metadata()
score.metadata.title = "Generated Chords"
score.metadata.composer = "AI Composer"

# Create a music21 part to hold the chords
part = stream.Part()

# Generate and add chords to the part
chords = generate_chords()
for c in chords:
    part.append(c)

# Add the part to the score
score.append(part)

# View the score
score.show()

# Optionally save the score to a MusicXML file
score.write('musicxml', fp='generated_chords.xml')
