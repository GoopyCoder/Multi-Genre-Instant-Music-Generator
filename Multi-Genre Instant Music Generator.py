"""
Isaac Powell
The purpose of this code is to randomly generate a chord progression for a user-selected genre.
"""

import os
from mido import MidiFile, MidiTrack, Message
import random


# Define common chord progressions for each genre
chord_progressions = {
    "hip-hop": [
        ["Am", "Dm", "Em", "G"],
        ["Dm", "G", "Am", "C"],
        ["Am", "C", "G", "F"],
        ["F", "C", "Dm", "Bb"],
        ["Dm", "G", "C", "A"],
        ["G", "C", "D", "Em"],
        ["Cm", "Gm", "Bb", "Ab"],
        ["Fm", "Bb", "Eb", "Cm"],
        ["Cm", "G", "Fm", "G"],
        ["Eb", "Bb", "Ab", "Cm"],
        ["Ab", "Eb", "Bb", "Cm"],
        ["Gm", "Eb", "F", "Dm"],
    ],
    "r&b": [
        ["Cmaj7", "Dm7", "G7", "Am7"],
        ["Am7", "D7", "Gmaj7", "Cmaj7"],
        ["Dm7", "G7", "Cmaj7", "Fmaj7"],
        ["Fmaj7", "Gm7", "Am7", "Dm7"],
        ["Em7", "A7", "Dmaj7", "Gmaj7"],
        ["Bbmaj7", "Dm7", "Gm7", "Cm7"],

        ["Am7", "D7", "Gmaj7", "Cmaj7"],
        ["Dm7", "G7", "Cmaj7", "Fmaj7"],
        ["Gm7", "C7", "Fmaj7", "Bbmaj7"],
        ["Am7", "D7", "Gmaj7", "Cmaj7"],
        ["Em7", "A7", "Dmaj7", "Gmaj7"],
        ["Bbmaj7", "Dm7", "Gm7", "Cm7"]
    ],
    "pop": [
        ["C", "G", "Am", "F"],
        ["Dm", "G", "C", "Am"],
        ["G", "D", "Em", "C"],
        ["F", "C", "G", "Am"],
        ["Am", "F", "C", "G"],
        ["D", "A", "Bm", "G"],

        ["E", "B", "C#m", "A"],
        ["F#m", "D", "A", "E"],
        ["C", "G", "Am", "F"],
        ["Dm", "G", "C", "Am"],
        ["G", "D", "Em", "C"],
        ["F", "Am", "Dm", "G"]
    ],
    "jazz": [
        ["Cmaj7", "Dm7", "G7", "Cmaj7"],
        ["Fmaj7", "G7", "Cmaj7", "Dm7"],
        # ["Dm7", "G7", "Cmaj7", "A7"],
        ["Am7", "D7", "Gmaj7", "Cmaj7"],
        ["Gm7", "C7", "Fmaj7", "Bbmaj7"],
        ["Em7", "A7", "Dmaj7", "Gmaj7"],

        ["Cmaj7", "Am7", "Dm7", "G7"],
        ["Fmaj7", "Bm7b5", "E7", "Amaj7"],
        ["Dm7", "G7", "Cmaj7", "Fmaj7"],
        ["Am7", "D7", "Gmaj7", "Cmaj7"],
        ["Gm7", "C7", "Fmaj7", "Bbmaj7"],
        ["Bbmaj7", "Eb7", "Abmaj7", "Dbmaj7"]
    ],
    "drake": [
        ["F#m7", "E", "Dmaj7", "C#m7"],  # Similar to the style in "One Dance"
        ["Bm7", "A", "Gmaj7", "F#m7"],  # Similar to the style in "Hotline Bling"
        ["Amaj7", "F#m7", "C#m7", "Bm7"],  # Similar to the style in "In My Feelings"
        ["C#m7", "A", "E", "F#m7"],  # Similar to the style in "God's Plan"
        ["E", "Bm7", "C#m7", "A"],  # Similar to the style in "Hold On, We're Going Home"
        ["Gmaj7", "F#m7", "Bm7", "E"],  # Similar to the style in "Passionfruit"
        ["Dmaj7", "C#m7", "F#m7", "E"],  # Similar to the style in "Too Good"
        ["Am7", "G", "F", "C"],  # Similar to the style in "Take Care"
        ["C#m7", "G#m7", "F#m7", "B"],  # Similar to the style in "Started From the Bottom"
        ["A", "E", "F#m7", "D"],  # Similar to the style in "Nice for What"
        ["F#m", "D", "A", "E"],  # Similar to the style in "The Motto"
        ["B", "F#", "E", "G#m"],  # Similar to the style in "Forever"
        ["G#m7", "C#m7", "F#", "B"],  # Similar to the style in "Best I Ever Had"
        ["E", "C#m", "A", "B"],  # Similar to the style in "Controlla"
        ["Am", "C", "G", "F"],  # Similar to the style in "Marvin's Room"
        ["F", "C", "Dm", "Bb"],  # Similar to the style in "Energy"
        ["Dm", "Am", "C", "G"],  # Similar to the style in "Jumpman"
        ["Bm", "G", "D", "A"],  # Similar to the style in "0 to 100 / The Catch Up"
        ["F#m7", "D", "E", "A"],  # Similar to the style in "Trophies"
        ["C#m", "F#", "A", "B"],  # Similar to the style in "HYFR"
        ["Amaj7", "C#m7", "F#m7", "G#m7"],
        ["Bm7", "G", "D", "A"],
        ["Dmaj7", "Bm7", "Gmaj7", "F#m7"],
        ["A", "G#m7", "F#m7", "E"],
        ["Amaj7", "Bm7", "C#m7", "Dmaj7"],
        ["G#m7", "F#m7", "E", "Dmaj7"]
    ]
}


chord_to_midi = {
    "C#m": [61, 64, 68, 71],
    "C#m9": [61, 64, 68, 71, 75, 78],
    "Amaj9": [69, 73, 76, 80, 84],
    "Emaj9": [64, 68, 71, 75, 79],
    "F#m11": [66, 69, 72, 76, 79, 82],
    "G#maj7": [56, 60, 63, 67, 71],
    "B": [59, 63, 66],
    "F#": [66, 70, 73],
    "Cm7": [60, 63, 67, 70],
    "Gm7": [55, 59, 62, 65],
    "Am7": [57, 60, 64, 67],
    "Dm7": [62, 66, 69, 72],
    "G7": [55, 59, 62, 66],
    "Cmaj7": [60, 64, 67, 71],
    "E": [64, 68, 71],
    "A": [57, 61, 64],
    "C#maj7": [61, 65, 68, 72],
    "Emaj7": [64, 68, 71, 75],
    "F#m7": [66, 69, 73, 76],
    "Gm": [55, 59, 62],
    "B7": [59, 63, 66, 71],
    "D7": [62, 66, 69, 74],
    "Gmaj7": [55, 59, 62, 67],
    "Em7": [64, 67, 70, 74],
    "C#m7": [61, 64, 68, 71],
    "Cm": [60, 63, 67],
    "Dmaj7": [62, 66, 69, 73],
    "Bb": [58, 62, 65, 70],
    "Amaj7": [69, 73, 76, 80],
    "F#7": [66, 70, 73, 77],
    "Bmaj7": [59, 63, 66, 70, 74],
    "A7": [69, 73, 76, 79],
    "D": [62, 66, 69],
    "C": [60, 64, 67],
    "G": [55, 59, 62],
    "Am": [57, 60, 64],
    "F": [53, 57, 60],
    "Dm": [62, 65, 69],
    "Em": [64, 67, 71],
    "Bm": [59, 62, 66],
    "E7": [64, 67, 71, 76],
    "G#m7": [56, 60, 63, 67],
    "C#7#9": [61, 65, 68, 72, 75],
    "F#maj7#11": [66, 70, 74, 77, 81],
    "D#m9": [63, 67, 70, 75, 78],
    "Bmaj9#11": [59, 63, 66, 71, 74, 77],
    "C#m11": [61, 64, 68, 71, 75],
    "Am9": [57, 60, 64, 69, 72],
    "G#m7#11": [56, 60, 63, 68, 72],
    "D#7#9": [63, 67, 70, 75, 78],
    "G#m7#11": [56, 60, 63, 68, 72],
    "G#m7": [56, 60, 63, 67],
    "Bmaj7#11": [59, 63, 66, 70, 74],
    "F#7#9": [66, 70, 73, 78],
    "F#m9": [66, 69, 73, 78, 81],
    "Emaj7#11": [64, 68, 71, 75, 79],
    "C#m7#11": [61, 64, 68, 72, 76],
    "G#m7": [56, 60, 63, 67],
    "F#maj9": [66, 69, 73, 78, 81],
    "G#7#11": [56, 60, 63, 68, 72],
    "F#maj7#11": [66, 70, 74, 77, 81],
    "D#m7": [63, 67, 70, 73],
    "B7#11": [59, 63, 66, 71, 74],
    "Gm7#11": [55, 59, 62, 65, 68],
    "C7#9": [60, 64, 67, 70, 74],
    "Fmaj7#11": [65, 69, 72, 76, 79],
    "Cmaj9": [60, 64, 67, 71, 74],
    "Dm11": [62, 66, 69, 74, 78, 81],
    "G7#11": [55, 59, 62, 66, 70, 74],
    "Fmaj7": [53, 57, 60, 64, 67],
    "Cmaj7#11": [60, 64, 67, 71, 75],
    "Bbmaj7#11": [58, 62, 65, 69, 72],
    "C#m7#11": [61, 64, 68, 72, 75],
    "G#maj7#11": [56, 60, 63, 67, 71],
    "Bm7": [59, 62, 66, 69],
    "C#7#9": [61, 65, 68, 72, 75],
    "D#m9": [63, 67, 70, 75, 78],
    "G#m7#11": [56, 60, 63, 68, 72],
    "Am9": [57, 60, 64, 69, 72],
    "Bmaj9#11": [59, 63, 66, 71, 74, 77],
    "C#m11": [61, 64, 68, 71, 75],
    "Bmaj7#11": [59, 63, 66, 70, 74],
    "F#7#9": [66, 70, 73, 78],
    "F#m9": [66, 69, 73, 78, 81],
    "Emaj7#11": [64, 68, 71, 75, 79],
    "G#m7#11": [56, 60, 63, 68, 72],
    "D#7#9": [63, 67, 70, 75, 78],
    "G#m7#11": [56, 60, 63, 68, 72],
    "F#7#9": [66, 70, 73, 78],
    "F#m9": [66, 69, 73, 78, 81],
    "Emaj7#11": [64, 68, 71, 75, 79],
    "C#m7#11": [61, 64, 68, 72, 76],
    "G#maj7#11": [56, 60, 63, 67, 71],
    "Bm7": [59, 62, 66, 69],
    "C#7#9": [61, 65, 68, 72, 75],
    "D#m9": [63, 67, 70, 75, 78],
    "G#m7#11": [56, 60, 63, 68, 72],
    "Am9": [57, 60, 64, 69, 72],
    "G#m7#11": [56, 60, 63, 68, 72],
    "C#7": [61, 64, 68, 72],
    "F#maj7": [66, 70, 74, 77]
}

chord_to_midi.update({
    "Ab9": [56, 60, 63, 66, 70],
    "Eb11": [63, 67, 70, 74, 77, 80],
    "Bb7": [58, 62, 65, 68],
    "Dm11": [62, 66, 69, 74, 78, 81],
    "Em13": [64, 68, 71, 75, 79, 82],
    "G9": [55, 59, 62, 67, 70],
    "G11": [55, 59, 62, 66, 70, 74],
    "C13": [60, 64, 67, 71, 74, 78],
    "Am11": [57, 60, 64, 67, 71, 74],
    "Fmaj9": [53, 57, 60, 65, 69],
    "Bb9": [58, 62, 65, 70, 74],
    "Dm9": [62, 66, 69, 74, 77],
    "C7": [60, 64, 67, 70],
    "A7": [57, 61, 64, 68],
    "Cm9": [60, 63, 67, 70, 74],
    "Gm11": [55, 59, 62, 65, 69, 74],
    "Bb13": [58, 62, 65, 69, 74, 77],
    "Ab7": [56, 60, 63, 68],
    "Fm9": [53, 57, 60, 65, 69],
    "Bb11": [58, 62, 65, 69, 74],
    "Eb13": [63, 67, 70, 74, 79, 82],
    "Cm11": [60, 63, 67, 70, 74, 77],
    "G13": [55, 59, 62, 67, 71, 74],
    "Fm7": [53, 57, 60, 65],
    "C9": [60, 64, 67, 70, 74],
    "Em11": [64, 68, 71, 75, 79, 82]
})

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



# echo_print_midi()


# # Create a new MIDI file
midi_file = MidiFile()

# # Create new MIDI tracks
track = MidiTrack()
bass_track = MidiTrack()
midi_file.tracks.append(track)
midi_file.tracks.append(bass_track)

midi_chords = [midi_chord_1, midi_chord_2, midi_chord_3, midi_chord_4]

# for midi_chord in midi_chords:
#     for note in midi_chord:
#         print(midi_chord, note)
#         track.append(Message('note_on', note=note, velocity=64, time=0))

#     # Add note-off messages for all notes in the chord after a duration (e.g., 2500 ticks)
#     for note in midi_chord:
#         track.append(Message('note_off', note=note, velocity=64, time=2500))

print(midi_chord_1)
print(midi_chord_2)
print(midi_chord_3)
print(midi_chord_4)

for midi_chord in midi_chords:
    for note in midi_chord:
        print(note)
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
                          

output_directory = 'c:/Users/ipowe.DESKTOP-G3Q2I40/Desktop/python'

# Specify the full file path, including the filename and extension
file_path = os.path.join(output_directory, 'chord_midi_file.mid')

# Save the MIDI file to the specified path
midi_file.save(file_path)

print(f"MIDI file saved to: {file_path}")