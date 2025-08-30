from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check
import sys
import os

class Chapter1Scene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Placeholder for chapter 1 story text
        lines = [
            "You didn't have a cozy bed for the night, but you found the biggest,",
            "most beautiful arch in town: the Queen's Arch!",
            "'I'm sure she wouldn't mind if I snoozed here', you thought.",
            "Snuggling into a secret spot where no one would see, you closed your eyes...",
            "The air is quiet and still. In the deepest hours of the night,",
            "you hear a strange sound and a whisper that tickles your ears.",
            "You peek through a tiny crack in the arch,",
            "but it's too dark to see anything...",
            "",
            "The air crackles with power as a whisper from the unseen speaks to you.",
            "It is time to test one of your skills, wanderer.",
            "Focus your thoughts, press ENTER and let your path be revealed...",
            "[SKILL_CHECK]",
            "",
            "",
            "",
            # outcome chooses one of the dialogues from chapter1.py
            "",
            "Your heart goes thump-thump-thump! Is the Queen okay? Is the Town safe?",
            "You have stumbled upon a big, bad secret that needs to be stopped!",
            "The Fair Day is about to begin, and you know you must find a way to save it."
            # end of chapter 1
        ]
        idx = 0
        # Placeholder for art files to cycle through
        art_files = [
            'castle2.txt',
            'nightcastle.txt',
            'char_knee2.txt',
            "3nightpeeps.txt",
            "face2.txt"
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        while idx < len(lines):
            # Check for skill check placeholder
            if '[SKILL_CHECK]' in lines[idx:idx+4]:
                # Run skill check for Perception (example)
                from importlib.util import spec_from_file_location, module_from_spec
                dialogue_path = os.path.join(os.path.dirname(__file__), '../assets/dialogues/chapter1.py')
                spec = spec_from_file_location('chapter1_dialogue', dialogue_path)
                chapter1_dialogue = module_from_spec(spec)
                sys.modules['chapter1_dialogue'] = chapter1_dialogue
                spec.loader.exec_module(chapter1_dialogue)
                # Run the skill check (let's use 'Mind' for this example)
                outcome_num = run_skill_check(self.player, 'Mind', self, main_w, main_h, side_w)
                outcome_map = {4: 'Yes and', 3: 'Yes but', 2: 'No but', 1: 'No and'}
                outcome_key = outcome_map[outcome_num]
                dialogue_lines = chapter1_dialogue.dialogue_1[outcome_key]
                # Show the dialogue result in the text box (4 lines)
                text_lines = dialogue_lines
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
                continue
            # Normal page rendering
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
