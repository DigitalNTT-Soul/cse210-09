import pygame
import os


def play_music(midi_filename):
    '''Stream music_file in a blocking manner'''
    pygame.mixer.music.load(midi_filename)
    while True:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()


path_to_here = os.path.abspath(__file__)
midi_file_path = os.path.join(os.path.dirname(path_to_here), 'music/Tron.mp3')
print(midi_file_path)
midi_filename = midi_file_path

# mixer config
freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024  # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)

# listen for interruptions
try:
    # use the midi file you just saved
    play_music(midi_filename)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit

play_music(os.path.abspath(midi_filename))
