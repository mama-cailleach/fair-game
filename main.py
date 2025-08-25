
from screens.title_screen import TitleScreen
from screens.game_scene import GameScene
from screens.art_test_scene import ArtTestScene
from screens.ui_template_scene import UITemplateScene
from screens.intro_scene_ui import IntroSceneUI
from screens.end_screen import EndScreen
from sound_manager import SoundManager


def main():
    # Start background music
    SoundManager.get().play_music('assets/audio/ourfestal.mp3', loop=True)
    # Start with the title screen
    screen = TitleScreen()
    screen.show()

    # Art test scene (for testing ASCII art display)
    scene = ArtTestScene()
    scene.show()

    # UI Template scene
    scene = UITemplateScene()
    scene.show()

    # Intro Scene UI
    scene = IntroSceneUI()
    scene.show()

    # Main game loop (placeholder for now, can be expanded to multiple scenes)
    scene = GameScene()
    scene.show()

    # End screen
    screen = EndScreen()
    screen.show()

if __name__ == "__main__":
    main()
