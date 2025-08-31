from .ui_template_scene import UITemplateScene
from .utils import load_art, ArrowMenu, run_skill_check
import msvcrt

class Chapter3MazeScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        lines = [
            #Lines for after the mini game
            "Deep inside the spooky house, you find a giant, heavy door.",
            "Then, you heard a tiny, muffled sound from inside.",
            "A soft cry, like someone was tied up. It had to be the real Queen!",
            "Your wiggling and giggling had woken something else!",
            "",
            "A sudden, cold WHOOSH made you jump!", 
            "You saw a sparkly, see-through shape—a ghostly knight!",
            "It was guarding the door! It pushed you away!",
            "",
            "You quickly scrambled out of the house, your heart doing a wild dance in your chest.",
            "You ran and ran until you tripped over a big, mossy rock.",
            "",
            "",
            "You looked down. It was a tall, jagged stone, half-hidden by plants.",
            "This was the Witches' Stone!",
            ""
        ]
        idx = 0
        art_files = [
            'door2.txt',
            'person1.txt',
            'forrest1.txt',
            'forrest2.txt'
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6

        # Show intro lines as usual
        while idx < len(lines):
            text_lines = lines[idx:idx+4]
            art_file = art_files[(idx // 4) % len(art_files)]
            art = load_art(art_file)
            art_lines = art.split('\n')
            main_box = []
            main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
            art_pad_top = max(0, (main_h - len(art_lines)) // 2)
            for i in range(main_h):
                if art_pad_top <= i < art_pad_top + len(art_lines):
                    art_line = art_lines[i - art_pad_top].center(main_w)
                else:
                    art_line = ' ' * main_w
                if i == 2:
                    side_line = self.player.char_class.center(side_w)
                elif i == 5:
                    side_line = self.player.attr_labels[0].center(side_w)
                elif i == 6:
                    side_line = self.player.attr_labels[1].center(side_w)
                elif i == 7:
                    side_line = self.player.attr_labels[2].center(side_w)
                else:
                    side_line = ' ' * side_w
                main_box.append('│' + art_line + '│' + ' ' + '│' + side_line + '│')
            main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')
            # Text box
            text_box = []
            text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
            for j in range(text_h):
                if j < len(text_lines):
                    line = text_lines[j].center(main_w + side_w + 3)
                else:
                    line = ' ' * (main_w + side_w + 3)
                if j == text_h - 1:
                    next_str = "> Next"
                    line = line[:-len(next_str)-1] + next_str + ' '
                text_box.append('│' + line + '│')
            text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
            content = '\n'.join(main_box + text_box)
            self.draw_frame(content)
            self.wait_for_key("")
            idx += 4
