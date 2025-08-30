from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter4Scene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter4.md (one per line, as in the file)
        lines = [
            "You caught your breath and thought hard.",
            "You couldn't fight a ghost by yourself, but you knew some very wise helpers!",
            "",
            "[CHECK_SPIRIT_FOR_RITUAL] (choose ritual?)",
            "",
            "You performed your little ritual.",
            "Swirly smoke floated up, and the air felt tingly.",
            "Slowly, five shimmering figures appeared:",
            "Margaret Pringle, Bessie Vickar, Annaple Thomsone, and two friends both named Margaret Hamilton!",
            "They were the ancient witches of Bo'ness, here to help!",
            "",
            "(maybe add some dialogue choices)",
            "",
            '"The ghost knight is sad and lonely," whispered Margaret Pringle.',
            '"To beat him, you need his shiny sword. It\'s special, and it will open the door!"',
            'Bessie Vickar added, "And inside that room, beyond the knight, are our magical flying brooms!"',
            '"They\'ve been waiting for a hero like you to carry you back to the coronation!"',
            "",
            "# The Queen's Great Escape",
            "",
            "Feeling brave, you went back to the spooky Carriden House.",
            "GO IN",
            "MAZE",
            "IF ALREADY DONE THE MAZE PATH WILL BE MARKED",
            "",
            "You found the ghostly knight, and this time, you were ready!",
            "You used your own clever magic and what the ancient witches taught you.",
            "*choices all of them are good, maybe dialogue choices from above can inform the ritual....*",
            "(Maybe you made a bright light, or tickled his arm until he dropped his sword!)",
            "*depending on choice a different outcome, but they are all successful*",
            "However you did it, you bravely faced the knight, and its sparkly form faded away.",
            "You picked up its ancient blade.",
            "",
            "The sword felt warm and buzzy in your hand.",
            "You touched it to the big, locked door, and click! The door swung open!",
            "Inside, tied up but safe, was the real Queen!",
            "",
            "Her eyes, a little tired but full of thanks, sparkled at you.",
            '"Thank you, thank you!" she whispered.',
            '"We must hurry! Linlithgow is trying to take over the crown,',
            'they want to steal Bo\'ness and destroy our town!"',
            "",
            "(look for brooms/a way to escape)",
            "",
            "You spotted some beautiful, shiny brooms in the corner.",
            '"Look!" you said, a big smile on your face.',
            '"They\'re waiting for us!" With the Queen holding on tight,',
            'you both jumped on a broom and zoomed into the sky!'
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'chapter4_1.txt',
            'chapter4_2.txt',
            'chapter4_3.txt',
            'chapter4_4.txt',
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        while idx < len(lines):
            # Check for spirit skill check placeholder
            if '[CHECK_SPIRIT_FOR_RITUAL]' in lines[idx:idx+4]:
                # Run skill check for Spirit
                outcome_num = run_skill_check(self.player, 'Spirit', self, main_w, main_h, side_w)
                # Placeholder: you can map outcome_num to dialogue later
                text_lines = [
                    "You feel the ancient magic swirl around you...",
                    "The ritual is complete!",
                    "(Outcome: {} - add branching here)".format(outcome_num),
                    ""
                ]
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
                continue
            # Normal page rendering
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
