from .ui_template_scene import UITemplateScene
from .utils import load_art

class OutroScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter6.md (one per line, as in the file)
        lines = [
            "The cheers that filled the air then were the loudest, happiest cheers ever!",
            "Not just for the Fair Day, but for their Queen, for their freedom,", 
            "and for you, the brave hero who saved them!",
            "The true Queen was crowned with lots of claps and happy tears.",
            "Songs were sung even louder, full of joy and victory!",
            "As the big parade went to Dougie Park for more fun, you were with your new witch friends.",
            "All of you smiling and laughing. You, the wanderer, the secret witch, the unexpected hero.",
            "Partying with them, no longer an outsider, but a special part of Bo'ness's happy story.",
            "",
            "The air was filled with music, laughter,", 
            "and the promise of many more Fair Days to come,",
            "all thanks to your courage and cleverness!",
            "",
            "",
            "THE END",
            ""
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'crowning2.txt',
            'crowning3.txt',
            'boness1.txt',
            'theend.txt'
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
