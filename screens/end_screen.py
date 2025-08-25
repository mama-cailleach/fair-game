from .base_screen import BaseScreen

class EndScreen(BaseScreen):
    def show(self):
        credits = (
            "Thank you for playing!\n\n"
            "Created for Weans Game Jam 2025.\n\n"
            "by mama\n"
        )
        self.draw_frame(credits)
        self.wait_for_key("Press Enter to exit...")
