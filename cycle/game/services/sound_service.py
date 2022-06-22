import pygame
import os


class SoundService:

    def __init__(self):
        self._freq = 44100
        self._bitsize = -16
        self._channels = 2
        self._buffer = 1024
        pygame.mixer.init(self._freq, self._bitsize, self._channels, self._buffer)
        pygame.mixer.music.set_volume(0.4)

        # Load Tron music
        self._path_for_tron = os.path.abspath(__file__)
        self._tron_file_path = os.path.join(os.path.dirname(self._path_for_tron), 'music/Tron.mp3')
        pygame.mixer.music.load(self._tron_file_path)

        # Load wilheim music
        # self._path_for_wil = os.path.abspath(__file__)
        # self._wil_file_path = os.path.join(os.path.dirname(self._path_for_wil), 'music/wilhelmscream.mp3')
        # pygame.mixer.music.load(self._wil_file_path)

    def play_music(self):
        '''Stream music_file in a blocking manner'''
        if not pygame.mixer.music.get_busy():
          pygame.mixer.music.play()

    # def play_wilhelm(self):
        
        # pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()
    #     pygame.mixer.music.pause()

# wilhelm = SoundService()
# wilhelm.play_wilhelm()



