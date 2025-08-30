from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter2Scene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter2.md (one per line, as in the file)
        lines = [
            "When morning came, the town was wide awake and super excited! ",
            "The happy sound of bagpipes filled the air, like a giant, musical yawn.",
            "From your secret spot, you watched as the Fair Day started. Laughter all around.",
            "And then, there she was: the Queen! But you knew it wasn't the real Queen. ",
            "It was the pretend Queen! She smiled and waved, but her eyes looked a bit cold.",
            "Nobody else seemed to notice, because they were all so excited for the fair. ",
            "But you saw the tiny differences, like spotting a sneaky fox in a field of sheep.",
            "You looked at the people walking with her. Who was there with her the night before?",
            "Was it her shiny Champion? Or maybe the people carrying the scepter and crown? ",
            "You knew someone important was part of the night before. ",
            "You stayed hidden, letting the happy noise wash over you. ",
            "The day was bright and jolly, everyone was heading to the Town Hall for the crowning.",
            "",
            "You knew you had to do something, and fast!",
            "",
            ""
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'piper1.txt',
            'queen3.txt',
            'champion1.txt',
            'face1.txt',
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        while idx < len(lines):
            text_lines = lines[idx:idx+4]
            art_file = art_files[(idx // 4) % len(art_files)]
            art = load_art(art_file)
            art_lines = art.split('\n')
            # Main rectangle with ASCII art centered vertically
            main_box = []
            main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
            art_pad_top = max(0, (main_h - len(art_lines)) // 2)
            for i in range(main_h):
                if art_pad_top <= i < art_pad_top + len(art_lines):
                    art_line = art_lines[i - art_pad_top].center(main_w)
                else:
                    art_line = ' ' * main_w
                # Side box: show player class and attributes
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
        # After all lines, return to allow next scene
