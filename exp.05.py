import numpy as np
from music21 import environment, stream, chord, note, pitch

# Create an environment object
env = environment.Environment()

# Update this path to the Sibelius executable
env['musicxmlPath'] = '/Applications/Sibelius.app/Contents/MacOS/Sibelius'

# Function to generate frequency-modulated notes including microtones
def generate_modulated_chord(root_freq, modulation, num_notes):
    freqs = [root_freq * (2 ** (n / 12)) * modulation for n in range(num_notes)]
    microtonal_notes = []
    for freq in freqs:
        p = pitch.Pitch()
        p.frequency = freq
        # Calculate the microtonal deviation in cents
        deviation = 1200 * np.log2(freq / p.standardPitchFrequency)
        p.microtone = pitch.Microtone(deviation)
        n = note.Note()
        n.pitch = p
        n.quarterLength = 1
        microtonal_notes.append(n)
    return chord.Chord(microtonal_notes)

# Create a stream for the chord progression
chord_stream = stream.Stream()

# Generate a simple chord progression with frequency modulation
root_freqs = [261.63, 220.00, 174.61, 196.00]  # C4, A3, F3, G3 in Hz
modulation = 1.05  # Simple modulation factor

# Add frequency-modulated chords to the stream
for root_freq in root_freqs:
    modulated_chord = generate_modulated_chord(root_freq, modulation, 3)  # Generate a triad
    chord_stream.append(modulated_chord)

# Add a simple melody to accompany the chords
melody = [
    note.Note("C5", quarterLength=1),
    note.Note("A4", quarterLength=1),
    note.Note("F4", quarterLength=1),
    note.Note("G4", quarterLength=1)
]

# Add melody notes to the stream
for n in melody:
    chord_stream.append(n)

# Show the chord progression using Sibelius
chord_stream.show()
