from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter2WitchesScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter2.md (one per line, as in the file)
        lines = [
            "",
            "Before you could even introduce yourself they knew.",
            "They felt warm and gentle as the breeze.",
            "And your conversation flowed easily.",
            "They were the Witches of Bo'ness, known for their magical dances and clever songs! ",
            "You felt a special tingle, a feeling you knew well, because you were a witch too! ",
            "You had actually come to Bo'ness to find a secret, old place called the Witches' Stone.",
            "As you chatted with the friendly witches, you all became fast friends. ",
            "One kind witch, who was a special friend to the real Queen, leaned in and whispered, ",
            "'The Queen seemed... different today, not herself at all.' ",
            "This was your chance! You leaned in too, and whispered about what happened in the night ",
            "Her eyes grew wide! She quickly handed you an old, crinkly map. ",
            "",
            "'This will lead you to the Witches' Stone, dear friend. Be careful!' she said.",
            "The answers you seek might be there...",
            "> Open The Map"
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'chapter2_1.txt',
            'chapter2_2.txt',
            'chapter2_3.txt',
            'chapter2_4.txt',
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
