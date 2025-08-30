
from .ui_template_scene import UITemplateScene
from .utils import load_art

class IntroSceneUI(UITemplateScene):
    def show(self):
        # The intro story lines
        lines = [
            "",
            "The air is thick with anticipation, and the streets are alive", 
            "with the sounds of the Kinnel Band marching through town.",
            "",
            "You follow with the crowd, laughter and joy fill the air as you see marvelous arches.",
            "They stop to play for the Queen elect, as she smiles the warmest smile towards you.",
            "",
            "It all seems awfy braw, but something doesn't feel right...",
            "Strange things are afoot, and your adventure is about to begin!"
        ]
        idx = 0
        # List of art files to cycle through for each page
        art_files = [
            'piper1.txt',
            'castle2.txt',
            'castle3.txt'
        ]
        while idx < len(lines):
            # Show up to 3 lines at a time
            text_lines = lines[idx:idx+3]
            # Pick art file for this page (cycle if fewer arts than pages)
            art_file = art_files[(idx // 3) % len(art_files)]
            art = load_art(art_file)
            art_lines = art.split('\n')
            # Use the same dimensions as UITemplateScene
            main_w = 70
            main_h = 22
            side_w = 20
            text_h = 6
            # Main rectangle with ASCII art centered vertically
            main_box = []
            main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
            art_pad_top = max(0, (main_h - len(art_lines)) // 2)
            for i in range(main_h):
                if art_pad_top <= i < art_pad_top + len(art_lines):
                    line = art_lines[i - art_pad_top].center(main_w)
                else:
                    line = ' ' * main_w
                main_box.append('│' + line + '│' + ' ' + '│' + ' ' * side_w + '│')
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
                    # Place '> Next' at the bottom right, with one space before the border
                    next_str = "> Next"
                    line = line[:-len(next_str)-1] + next_str + ' '
                text_box.append('│' + line + '│')
            text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
            content = '\n'.join(main_box + text_box)
            self.draw_frame(content)
            self.wait_for_key("")
            idx += 3
        # After all lines, return to allow next scene
