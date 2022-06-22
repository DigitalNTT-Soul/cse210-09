import pygame
import os


class SoundService:

    def __init__(self):
        freq = 44100
        bitsize = -16
        channels = 2
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(0.4)
        path_to_here = os.path.abspath(__file__)
        midi_file_path = os.path.join(os.path.dirname(path_to_here), 'music/Tron.mp3')
        pygame.mixer.music.load(midi_file_path)

    def play_music(self):
        '''Stream music_file in a blocking manner'''
        if not pygame.mixer.music.get_busy():
          pygame.mixer.music.play()

    def play_wilhelm(self):
        path_to_here = os.path.abspath(__file__)
        midi_file_path = os.path.join(os.path.dirname(path_to_here), 'music/wilhelmscream.mp3')
        pygame.mixer.music.load(midi_file_path)

SoundService().play_music()




