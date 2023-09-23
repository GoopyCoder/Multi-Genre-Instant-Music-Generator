"""
Isaac Powell
The purpose of this code is to randomly generate a chord progression for a user-selected genre.
"""

import os
from mido import MidiFile, MidiTrack, Message
import random
from CHORDS import chord_to_midi
from Progressions import chord_progressions


# Ask the user to select a genre
genre_input = int(input("Select a genre (hip-hop (1), r&b (2), pop (3), jazz (4), OVO (5)): "))

# Check if the entered genre is valid
if genre_input > 0 and genre_input <= len(chord_progressions):
    genres = list(chord_progressions.keys())
    selected_genre = genres[genre_input - 1]

    # Randomly select a chord progression from the chosen genre
    selected_chord_progression = random.choice(chord_progressions[selected_genre])

    # Print the selected chord progression
    print(f"Random {selected_genre} chord progression: {selected_chord_progression}")
else:
    print("Invalid genre. Please select from hip-hop (1), r&b (2), pop (3), jazz (4), OVO (5).")

chord_1 = selected_chord_progression[0]
chord_2 = selected_chord_progression[1]
chord_3 = selected_chord_progression[2]
chord_4 = selected_chord_progression[3]

midi_chord_1 = chord_to_midi.get(chord_1)
midi_chord_2 = chord_to_midi.get(chord_2)
midi_chord_3 = chord_to_midi.get(chord_3)
midi_chord_4 = chord_to_midi.get(chord_4)

# # Create a new MIDI file
midi_file = MidiFile()

# # Create new MIDI tracks
track = MidiTrack()
bass_track = MidiTrack()
midi_file.tracks.append(track)
midi_file.tracks.append(bass_track)

midi_chords = [midi_chord_1, midi_chord_2, midi_chord_3, midi_chord_4]


for midi_chord in midi_chords:
    for note in midi_chord:
        # print(note)
        track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=midi_chord[0], velocity=64, time=1920))
    if (len(midi_chord) ==5):
        track.append(Message('note_off', note=midi_chord[1], velocity=64, time=0))
        track.append(Message('note_off', note=midi_chord[2], velocity=64, time=0))
        track.append(Message('note_off', note=midi_chord[3], velocity=64, time=0))
        track.append(Message('note_off', note=midi_chord[4], velocity=64, time=0))
    elif (len(midi_chord) ==4):
        track.append(Message('note_off', note=midi_chord[1], velocity=64, time=0))
        track.append(Message('note_off', note=midi_chord[2], velocity=64, time=0))
        track.append(Message('note_off', note=midi_chord[3], velocity=64, time=0))
    else:
        track.append(Message('note_off', note=midi_chord[1], velocity=64, time=0))
        track.append(Message('note_off', note=midi_chord[2], velocity=64, time=0))

for midi_chord in midi_chords:
    bass_track.append(Message('note_on', note=midi_chord[0], velocity=64, time=0))
    bass_track.append(Message('note_off', note=midi_chord[0], velocity=0, time=1920))
    if (len(midi_chord) ==5):
        track.append(Message('note_off', note=midi_chord[1], velocity=0, time=0))
        track.append(Message('note_off', note=midi_chord[2], velocity=0, time=0))
        track.append(Message('note_off', note=midi_chord[3], velocity=0, time=0))
        track.append(Message('note_off', note=midi_chord[4], velocity=0, time=0))
    if (len(midi_chord) ==4):
        bass_track.append(Message('note_off', note=midi_chord[1], velocity=0, time=0))
        bass_track.append(Message('note_off', note=midi_chord[2], velocity=0, time=0))
        bass_track.append(Message('note_off', note=midi_chord[3], velocity=0, time=0))
    else:
        bass_track.append(Message('note_off', note=midi_chord[1], velocity=0, time=0))
        bass_track.append(Message('note_off', note=midi_chord[2], velocity=0, time=0))
                          



# Get the current working directory (where the script is located)
current_directory = os.getcwd()

# Specify the filename (you can customize this as needed)
file_name = 'chord_midi_file.mid'

# Specify the full file path, including the current directory, filename, and extension
file_path = os.path.join(current_directory, file_name)

# Create a new MIDI file
midi_file = MidiFile()

# Save the MIDI file to the current directory
midi_file.save(file_path)

print(f"MIDI file saved to: {file_path}")
