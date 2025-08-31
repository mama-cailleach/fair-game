from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter5Scene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter5.md (one per line, as in the file)
        lines = [
            "Down below, Bo'ness was still bursting with Fair Day fun!",
            "Pipers played and crowds cheered, singing happily.",
            "'Hurry!', she said. They had no idea their town was in danger!",
            "You and the Queen flew closer and closer to the Town Hall.",
            "You arrived just as the pretend Queen's Champion was delivering its speech:",
            "",
            "'If anyone here, shall deny the Queen's title to the throne,", 
            "I am here ready to defend it, in single combat.'",
            "",
            "Everyone went quiet. This was your moment!",
            "You landed super softly, and the Queen quickly hid behind you.",
            "You stepped forward, your cloak swirling, and shouted, 'I challenge you!'",
            "",
            "The Champion laughed a big, booming laugh. 'You? A simple witch thinks she can fight me?'",
            "But then, a strong, clear voice rang out! The true Queen stepped forward,",
            "looking very grand and brave. 'I am the Queen! That one, on my throne, is a trickster!'",
            "",
            "Oh my, what a hullabaloo! The pretend Queen shrieked and leaped at the real Queen,",
            "a shiny dagger in her hand! And the Champion charged right at you!",
            "",
            "This is it! Now it's your time to fight the Champion!",
            "You'll see yours and the Champion's HP on the side.",
            "You can use actions based on your character or your learned spells",
            "Good Luck!"
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'walking5.txt',
            'champion2.txt',
            'queen6.txt',
            'queen7.txt',
            'crowning1.txt',
            'char_idle5.txt',
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
