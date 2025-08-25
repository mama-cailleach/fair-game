from .base_screen import BaseScreen

class GameScene(BaseScreen):
    def show(self):
        content = (
            "[Scene Placeholder]\n\n"
            "This is where the main game content will go.\n"
            "Choices, dialogue, and skill checks will be handled here.\n"
        )
        self.draw_frame(content)
        self.wait_for_key()
