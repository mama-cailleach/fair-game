import pygame
import threading
import os

class SoundManager:
    _instance = None
    _music_thread = None
    _music_playing = False

    @staticmethod
    def get():
        if SoundManager._instance is None:
            SoundManager._instance = SoundManager()
        return SoundManager._instance

    def __init__(self):
        if SoundManager._instance is not None:
            raise Exception("SoundManager is a singleton!")
        pygame.mixer.init()
        self.music_loaded = False

    def play_music(self, filepath, loop=True):
        if not os.path.exists(filepath):
            print(f"[SoundManager] File not found: {filepath}")
            return
        if not self.music_loaded or pygame.mixer.music.get_busy() == 0:
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play(-1 if loop else 0)
            self.music_loaded = True
            SoundManager._music_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        SoundManager._music_playing = False

    def is_playing(self):
        return pygame.mixer.music.get_busy()
