from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter4PostBattleScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter5.md (one per line, as in the file)
        lines = [
        "However you did it, you bravely faced the knight." ,
        "And its sparkly form faded away.",
        "You picked up its ancient blade.",
        "",
        "The sword felt warm and buzzy in your hand.",
        "You touched it to the big, locked door, and click! The door swung open!",
        "Inside, tied up but safe, was the real Queen!",
        "",
        "Her eyes, a little tired but full of thanks, sparkled at you.",
        "'Thank you, thank you!' she whispered.",
        "'We must hurry! Linlithgow is trying to take over the crown,",
        "'they want to steal Bo'ness and destroy our town!'",
        "You spotted some beautiful, shiny brooms in the corner.",
        "'Look!' you said, a big smile on your face.",
        "'They're waiting for us!' With the Queen holding on tight,",
        "> USE BROOM CHARM <",
        "",
        "Just like the witches taught you, you used the broom charm.",
        "You both jumped on a broom and zoomed into the sky!",
        ""
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'chapter5_1.txt',
            'chapter5_2.txt',
            'chapter5_3.txt',
            'chapter5_4.txt',
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
