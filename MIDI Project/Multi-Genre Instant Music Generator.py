"""
Isaac Powell
The purpose of this code is to randomly generate a chord progression for a user-selected genre.
"""
import os
from mido import MidiFile, MidiTrack, Message
import random
from CHORDS import chord_to_midi
from Progressions import chord_progressions
from Drum_Patterns import gen_kick, gen_closed_hat, gen_snare


# Ask the user to select a genre
genre_input = int(input("Select a genre of hip-hop (1), r&b (2), pop (3), jazz (4), OVO (5), OZ (6): "))

# Check if the entered genre is valid
if genre_input > 0 and genre_input <= len(chord_progressions):
    genres = list(chord_progressions.keys())
    selected_genre = genres[genre_input - 1]

    # Randomly select a chord progression from the chosen genre
    selected_chord_progression = random.choice(chord_progressions[selected_genre])

    # Print the selected chord progression
    print(f"Random {selected_genre} chord progression: {selected_chord_progression}")
else:
    print("Invalid genre. Please select from hip-hop (1), r&b (2), pop (3), jazz (4), OVO (5), OZ (6).")

#Obtain Chords used from progression chosen
chord_1 = selected_chord_progression[0]
chord_2 = selected_chord_progression[1]
chord_3 = selected_chord_progression[2]
chord_4 = selected_chord_progression[3]

#Convert the chords to MIDI
midi_chord_1 = chord_to_midi.get(chord_1)
midi_chord_2 = chord_to_midi.get(chord_2)
midi_chord_3 = chord_to_midi.get(chord_3)
midi_chord_4 = chord_to_midi.get(chord_4)

midi_chords = [midi_chord_1, midi_chord_2, midi_chord_3, midi_chord_4]

# Create a new MIDI file
midi_file = MidiFile()

# Create new MIDI tracks
chord_track = MidiTrack()
bass_track = MidiTrack()
kick_track = MidiTrack()
snare_track = MidiTrack()
closed_hat_track = MidiTrack()
midi_file.tracks.append(chord_track)
midi_file.tracks.append(bass_track)
midi_file.tracks.append(kick_track)
midi_file.tracks.append(snare_track)
midi_file.tracks.append(closed_hat_track)

#Add the Chord MIDI
for midi_chord in midi_chords:
    for note in midi_chord:
        # print(note)
        chord_track.append(Message('note_on', note=note, velocity=64, time=0))
    chord_track.append(Message('note_off', note=midi_chord[0], velocity=64, time=1920))
    if len(midi_chord) == 6:
        for x in range(5):
            chord_track.append(Message('note_off', note=midi_chord[x+1], velocity=64, time=0))
    if len(midi_chord) ==5:
        for x in range(4):
            chord_track.append(Message('note_off', note=midi_chord[x+1], velocity=64, time=0))
    if len(midi_chord) ==4:
        for x in range(3):
            chord_track.append(Message('note_off', note=midi_chord[x+1], velocity=64, time=0))
    else:
        for x in range(2):
            chord_track.append(Message('note_off', note=midi_chord[x+1], velocity=64, time=0))

#Add the Bassline MIDI
for midi_chord in midi_chords:
    bass_track.append(Message('note_on', note=midi_chord[0], velocity=64, time=0))
    bass_track.append(Message('note_off', note=midi_chord[0], velocity=0, time=1920))

kick_track = gen_kick(kick_track)
snare_track = gen_snare(snare_track)
closed_hat_track = gen_closed_hat(closed_hat_track)



# Get the current working directory (where the script is located)
current_directory = os.getcwd()

# Specify the filename (you can customize this as needed)
file_name = 'chord_midi_file.mid'

# Specify the full file path, including the current directory, filename, and extension
file_path = os.path.join(current_directory, file_name)

# Save the MIDI file to the current directory
midi_file.save(file_path)

print(f"MIDI file saved to: {file_path}")