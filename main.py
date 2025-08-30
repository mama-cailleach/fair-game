
from screens.title_screen import TitleScreen
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
from screens.chapter5_scene import Chapter5Scene
from screens.outro_scene import OutroScene
from sound_manager import SoundManager


def main():
    # Start background music
    # SoundManager.get().play_music('assets/audio/ourfestal.mp3', loop=True)
    
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

    '''
    # Chapter 4 Scene (pass player object)
    scene = Chapter4Scene(player)
    scene.show()

    # Chapter 5 Scene (pass player object)
    scene = Chapter5Scene(player)
    scene.show()

    # Outro Scene (pass player object)
    scene = OutroScene(player)
    scene.show()
    '''

    # End screen
    screen = EndScreen()
    screen.show()

if __name__ == "__main__":
    main()
