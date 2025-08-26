
from screens.title_screen import TitleScreen
from screens.art_test_scene import ArtTestScene
from screens.intro_scene_ui import IntroSceneUI
from screens.char_choice_scene import CharChoiceScene
from screens.end_screen import EndScreen
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
    scene.show()

    # End screen
    screen = EndScreen()
    screen.show()

if __name__ == "__main__":
    main()
