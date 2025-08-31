import os
from screens.utils import resource_path
from screens.title_screen import TitleScreen
from screens.title_screen_2 import TitleScreen2
from screens.art_test_scene import ArtTestScene
from screens.intro_scene_ui import IntroSceneUI
from screens.char_choice_scene import CharChoiceScene
from screens.end_screen import EndScreen
from screens.chapter1_scene import Chapter1Scene
from screens.chapter2_scene import Chapter2Scene
from screens.chapter2_choice_scene import Chapter2ChoiceScene
from screens.chapter2_witches_scene import Chapter2WitchesScene
from screens.chapter3_scene import Chapter3Scene
from screens.chapter4_scene import Chapter4Scene
from screens.chapter4_poststone_scene import Chapter4PostStoneScene
from screens.chapter4_knightbattle_scene import Chapter4KnightBattleScene
from screens.chapter4_postbattle_scene import Chapter4PostBattleScene
from screens.chapter5_scene import Chapter5Scene
from screens.chapter5_fight_scene import Chapter5FightScene
from screens.chapter5_postfight_scene import Chapter5PostFightScene
from screens.outro_scene import OutroScene
from sound_manager import SoundManager


def main():

    
    while True:

        # Stop any music that might still be playing (e.g., from credits/end screen)
        if SoundManager.get().is_music_playing():
            SoundManager.get().stop_music()


        festal_path = resource_path(os.path.join('assets', 'audio', 'ourfestal.mp3'))
        kinneil_path = resource_path(os.path.join('assets', 'audio', 'kinneil.mp3'))
        journeyhome_path = resource_path(os.path.join('assets', 'audio', 'journeyhome.mp3'))
        ourchosen_path = resource_path(os.path.join('assets', 'audio', 'ourchosen.mp3'))
        bestday_path = resource_path(os.path.join('assets', 'audio', 'bestday.mp3'))

        # Our Festal Day

        SoundManager.get().play_music(festal_path, loop=True)
        screen = TitleScreen2()
        screen.show()

        # Start with the title screen
        screen = TitleScreen()
        screen.show()

        # Art test scene (for testing ASCII art display)
        scene = ArtTestScene()
        scene.show()
    
        # Intro Scene UI
        scene = IntroSceneUI()
        scene.show()

        # Character Choice Scene
        scene = CharChoiceScene()
        player = scene.show()

        # Chapter 1 Scene (pass player object)
        scene = Chapter1Scene(player)
        scene.show()    

        SoundManager.stop_music(festal_path)
        SoundManager.get().play_music(kinneil_path, loop=True)
        # Chapter 2 Scene (pass player object)
        scene = Chapter2Scene(player)
        scene.show()

        # Chapter 2 Choice Scene (pass player object)
        scene = Chapter2ChoiceScene(player)
        scene.show()

        # Chapter 2 Witches Scene (pass player object)
        scene = Chapter2WitchesScene(player)
        scene.show()

        # Chapter 3 Scene (pass player object)
        scene = Chapter3Scene(player)
        scene.show()   

        SoundManager.stop_music(kinneil_path)
        SoundManager.get().play_music(journeyhome_path, loop=True)
        # Chapter 4 Scene (pass player object)
        scene = Chapter4Scene(player)
        scene.show()

        # Chapter 4 Post Stone Scene (pass player object)
        scene = Chapter4PostStoneScene(player)
        scene.show()

        # Chapter 4 Knight Battle Scene (pass player object)
        scene = Chapter4KnightBattleScene(player)
        scene.show()

        # Chapter 4 Post Battle Scene (pass player object)
        scene = Chapter4PostBattleScene(player)
        scene.show()

        SoundManager.stop_music(journeyhome_path)
        SoundManager.get().play_music(ourchosen_path, loop=True)
        # Chapter 5 Scene (pass player object)
        scene = Chapter5Scene(player)
        scene.show()

        # Chapter 5 Fight Scene (pass player object)
        scene = Chapter5FightScene(player)
        scene.show()

        # Chapter 5 Post Fight Scene (pass player object)
        scene = Chapter5PostFightScene(player)
        scene.show()

        SoundManager.stop_music(ourchosen_path)
        SoundManager.get().play_music(bestday_path, loop=True)
        # Outro Scene (pass player object)
        scene = OutroScene(player)
        scene.show()

        # End screen
        screen = EndScreen()
        screen.show()

if __name__ == "__main__":
    main()
