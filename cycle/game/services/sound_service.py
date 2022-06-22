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

        # Load music
        self._path_for_tron = os.path.abspath(__file__)
        self._tron_file_path = os.path.join(os.path.dirname(self._path_for_tron), 'music/Tron.mp3')
        pygame.mixer.music.load(self._tron_file_path)

    def play_music(self):
        '''Stream music_file in a blocking manner'''
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

    def play_wilhelm(self):
        self._path_for_wil = os.path.abspath(__file__)
        self._wil_file_path = os.path.join(os.path.dirname(self._path_for_wil), 'music/wilhelmscream.mp3')
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self._wil_file_path))

    def stop_music(self):
        pygame.mixer.music.stop()
    #     pygame.mixer.music.pause()




"""

# start playing the background music
pygame.mixer.music.load(os.path.join(os.getcwd(), 'sound', 'main_theme.wav'))
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)  # loop forever
Then later in the code, you can play sound effects through Channels:

# play a sound on channel 0 with a max time of 600 milliseconds
pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound\gun_fire.wav'), maxtime=600)

# you can play a longer sound on another channel and they won't conflict
pygame.mixer.Channel(1).play(pygame.mixer.Sound("sound\death.wav"), maxtime=2000)
For more information on Channels

if you are looking to set the volume of an individual channel, you can use the set_volume() function:

channel.set_volume(0.5)  # play at 50% volume

"""