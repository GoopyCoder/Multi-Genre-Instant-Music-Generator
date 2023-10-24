import os
from mido import MidiFile, MidiTrack, Message
import random


# track = MidiTrack()
# bass_track = MidiTrack()
# kick_track = MidiTrack()
# snare_track = MidiTrack()
# closed_hat_track = MidiTrack()









    #Basic Kick Pattern
def kick1(kick_track):
    for x in range(16):
        kick_track.append(Message('note_on', note = 60, velocity = 127, time = 0))
        kick_track.append(Message('note_off', note = 60, velocity = 127, time = 480))

def kick2(kick_track):
    for x in range(2):
        kick_track.append(Message('note_on', note=60, velocity=127, time=0))
        kick_track.append(Message('note_off', note=60, velocity=127, time=960))  # Half of measure_time
        kick_track.append(Message('note_on', note=60, velocity=127, time=240))  # Quarter of measure_time
        kick_track.append(Message('note_off', note=60, velocity=127, time=240))
        kick_track.append(Message('note_on', note=60, velocity=127, time=960))  # Half of measure_time
        kick_track.append(Message('note_off', note=60, velocity=127, time=240))  # Syncopated
        kick_track.append(Message('note_on', note=60, velocity=127, time=480))  # Three-quarters of measure_time
        kick_track.append(Message('note_off', note=60, velocity=127, time=720))  # Quarter of measure_time

def kick3(kick_track):
    for x in range(2):
        kick_track.append(Message('note_on', note=60, velocity=127, time=0))
        kick_track.append(Message('note_off', note=60, velocity=127, time=480))
        kick_track.append(Message('note_on', note=60, velocity=127, time=240))  # Syncopated
        kick_track.append(Message('note_off', note=60, velocity=127, time=240))
        kick_track.append(Message('note_on', note=60, velocity=127, time=960))
        kick_track.append(Message('note_off', note=60, velocity=127, time=480))
        kick_track.append(Message('note_on', note=60, velocity=127, time=480))
        kick_track.append(Message('note_off', note=60, velocity=127, time=240))  # Syncopated

#Rhythm
def kick4(kick_track):
    for x in range(2):
        kick_track.append(Message('note_on', note = 60, velocity = 127, time = 0))
        kick_track.append(Message('note_on', note = 60, velocity = 127, time = 720))
        kick_track.append(Message('note_on', note = 60, velocity = 127, time = 720))
        kick_track.append(Message('note_off', note = 60, velocity = 127, time = 480))
        kick_track.append(Message('note_on', note = 60, velocity = 127, time = 0))
        kick_track.append(Message('note_on', note = 60, velocity = 127, time = 720))
        kick_track.append(Message('note_on', note = 60, velocity = 127, time = 480))
        kick_track.append(Message('note_off', note = 60, velocity = 127, time = 720))






















    #Basic Snare Pattern
def snare1(snare_track):
    for x in range(4):
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 960))

    #Snare Pattern 2
def snare2(snare_track):
    for x in range(1):
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 720))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 0))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 240))

    #Snare Pattern 2
def snare3(snare_track):
    for x in range(1):
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 960))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 240))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 720))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 720))
        snare_track.append(Message('note_on', note = 60, velocity = 127, time = 0))
        snare_track.append(Message('note_off', note = 60, velocity = 127, time = 240))










    #Basic Hi-Hat Pattern
def closed_hat1(closed_hat_track):
    for x in range(16):
        closed_hat_track.append(Message('note_on', note = 60, velocity = 127, time = 0))
        closed_hat_track.append(Message('note_off', note = 60, velocity = 127, time = 240))
        closed_hat_track.append(Message('note_on', note = 60, velocity = 85, time = 0))
        closed_hat_track.append(Message('note_off', note = 60, velocity = 85, time = 240))









kicks = [kick1, kick2, kick3, kick4]
snares = [snare1, snare2, snare3]
closed_hats = [closed_hat1]

random_snare = random.randint(1, 3) - 1
random_kick = random.randint(2, 4) - 1
random_closed_hat = random.randint(1, 1) - 1


def gen_kick(kick_track):
    kicks[random_kick](kick_track)
    return kick_track

def gen_snare(snare_track):
    snares[random_snare](snare_track)
    return snare_track

def gen_closed_hat(closed_hat_track):
    closed_hats[random_closed_hat](closed_hat_track)
    return closed_hat_track