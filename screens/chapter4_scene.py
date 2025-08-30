from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter4Scene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter4.md (one per line, as in the file)
        lines = [
            "",
            "You caught your breath and thought hard.",
            "You couldn't fight a ghost by yourself, but you knew some very wise helpers!",
            "All you need is to do a ritual for the witches.",
            "[CHECK_SOUL_FOR_RITUAL]",
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'witches5.txt',
            'witches6.txt',
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        while idx < len(lines):
            # Check for soul skill check placeholder
            if '[CHECK_SOUL_FOR_RITUAL]' in lines[idx:idx+4]:
                # Run skill check for Soul
                outcome_num = run_skill_check(self.player, 'Soul', self, main_w, main_h, side_w)
                # Store the outcome in the player object for later use
                self.player.soul_ritual_outcome = outcome_num
                # Show ritual outcome
                text_lines = [
                    "",
                    "You performed your wee ritual.",
                    "Swirly smoke floated up, and the air felt tingly.",
                    "Slowly, five shimmering figures appeared:"
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
                # Transition to the next scene (chapter4_postritual_scene)
                from .chapter4_postritual_scene import Chapter4PostRitualScene
                next_scene = Chapter4PostRitualScene(self.player)
                next_scene.show()
                return
            # Normal page rendering (should not be reached in this minimal scene)
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
