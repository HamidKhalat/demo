import random
import matplotlib.pyplot as plt
from music21 import stream, note, pitch, environment, converter
import tempfile
import os

# Function to create a microtonal scale over 2 octaves
def generate_microtonal_scale(base_note, octaves, intervals):
    scale = []
    for octave in range(octaves):
        for interval in intervals:
            p = base_note.transpose(interval + 12 * octave)
            scale.append(p)
    return scale

# Create a stream
s = stream.Stream()

# Define the pitches for a microtonal scale with quarter-tone subdivisions over 2 octaves
quarter_tone_intervals = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
base_note = pitch.Pitch('C4')

# Generate the microtonal scale
microtonal_scale = generate_microtonal_scale(base_note, 2, quarter_tone_intervals)

# Randomly select 10 pitches from the microtonal scale
random_pitches = random.sample(microtonal_scale, 10)

# Add the randomly selected pitches to the stream
for p in random_pitches:
    n = note.Note(p)
    n.quarterLength = 1  # Set the duration of each note
    s.append(n)

# Plot the pitch contour as a breakpoint function
plt.figure(figsize=(10, 6))
pitch_values = [p.midi for p in random_pitches]
plt.plot(pitch_values, marker='o', linestyle='-', color='b')
plt.title('Pitch Contour of Random Microtonal Scale')
plt.xlabel('Note Index')
plt.ylabel('MIDI Pitch Value')
plt.grid(True)
bpf_filename = 'pitch_contour.png'
plt.savefig(bpf_filename)
plt.close()

# Export the score to PNG using music21 and matplotlib
# Create a temporary file to save the score as a PDF
with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
    pdf_path = temp_pdf.name

# Save the stream as a PDF
s.write('pdf', fp=pdf_path)

# Convert the PDF to PNG using pdf2image
from pdf2image import convert_from_path
pages = convert_from_path(pdf_path, 300)  # 300 is the DPI
score_filename = 'score.png'
if pages:
    pages[0].save(score_filename, 'PNG')

# Clean up the temporary PDF file
os.remove(pdf_path)

print(f"PNG score saved as {score_filename}")
print(f"Pitch contour saved as {bpf_filename}")

# Display the PNG files in PyCharm's plot window
img1 = plt.imread(score_filename)
img2 = plt.imread(bpf_filename)

fig, axs = plt.subplots(2, 1, figsize=(10, 12))

axs[0].imshow(img1)
axs[0].set_title('Score')
axs[0].axis('off')

axs[1].imshow(img2)
axs[1].set_title('Pitch Contour')
axs[1].axis('off')

plt.tight_layout()
plt.show()
