from .base_screen import BaseScreen
import msvcrt
import sys

class EndScreen(BaseScreen):
    def show(self):
        credits = (
            "Thank you for playing!\n\n"
            "Created for Weans Game Jam: Summer 2025\n\n"
            "by mama\n"
            "mama666.itch.io\n\n"
            "Thanks so much Cler for:\n" 
            "testing, inspiration and support! <3 S2\n\n\n"
            "Whit's fur ye'll no go by ye!"
            "\n\n\n\n\n\n\n\n\n"
            "Press ENTER to play again or ESC to exit."
        )
        self.draw_frame(credits)
        while True:
            key = msvcrt.getch()
            if key in (b'\r', b'\n'):  # ENTER
                return  # Signal to main loop to restart the game
            elif key == b'\x1b':  # ESC
                sys.exit(0)
