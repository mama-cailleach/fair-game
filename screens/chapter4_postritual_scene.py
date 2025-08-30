from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter4PostRitualScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter4.md (one per line, as in the file)
        lines = [
            "",
            "Margaret Pringle, Bessie Vickar, Annaple Thomsone,", 
            "and two friends both named Margaret Hamilton!",
            "They were the ancient witches of Bo'ness, here to help!",
            '"The ghost knight is sad and lonely," whispered Margaret Pringle.',
            '"To beat him, you need his shiny sword. It\'s special, and it will open the door!"',
            'Bessie Vickar added, "And inside that room, are our magical flying brooms!"',
            '"They\'ve been waiting for a hero like you to carry you back to the coronation!"',
            "",
            "'But first' said both Margaret Hamiltons in unison 'you will need these spells!'",
            "The witches went on and taught you a couple of handy spells to be used...",
            "",
            "[SPELLS]"
        ]
        idx = 0
        # Placeholder for art files to cycle through (add your images here)
        art_files = [
            'witches10.txt',
            'witches7.txt',
            'witches8.txt',
            'witches9.txt',
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        import msvcrt
        from .utils import ArrowMenu
        spell_data = {
            1: [
                "Broom Charm",
                "Feather Spell"
            ],
            2: [
                "Broom Charm",
                "Tickle Spell"
            ],
            3: [
                "Broom Charm",
                "Tickle Spell",
                "Liar Liar"
            ],
            4: [
                "Broom Charm",
                "Tickle Spell",
                "Black Cat",
                "Liars Liars"
            ]
        }
        while idx < len(lines):
            # Check for spirit skill check placeholder
            if '[SPELLS]' in lines[idx:idx+4]:
                outcome = getattr(self.player, 'soul_ritual_outcome', 0)
                spell_names = spell_data.get(outcome, spell_data[1])
                # Assign spells to player object so they persist for the fight scene
                self.player.spells = spell_names.copy()
                # Map spell names to their corresponding art files
                spell_art_map = {
                    "Broom Charm": "char_magic_broom.txt",
                    "Feather Spell": "char_magic_feather.txt",
                    "Tickle Spell": "char_magic_tickle.txt",
                    "Black Cat": "char_magic_cat.txt",
                    "Liar Liar": "char_magic_liar.txt",
                    "Liars Liars": "char_magic_liars.txt"
                }
                spell_art_files = [spell_art_map.get(name, "spell_placeholder.txt") for name in spell_names]
                menu = ArrowMenu(spell_names + ["Continue"])
                while True:
                    sel = menu.selected  # integer index
                    # If 'Continue' is selected, show a blank or default art
                    if sel == len(spell_names):
                        art_file = "char_magic1.txt"
                    else:
                        art_file = spell_art_files[sel]
                    art = load_art(art_file)
                    art_lines = art.split('\n')
                    main_box = []
                    main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
                    art_pad_top = max(0, (main_h - len(art_lines)) // 2)
                    for i in range(main_h):
                        if art_pad_top <= i < art_pad_top + len(art_lines):
                            art_line = art_lines[i - art_pad_top].ljust(main_w)
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
                    menu_lines = menu.get_display(main_w + side_w + 3)
                    for j in range(text_h):
                        if j < len(menu_lines):
                            line = menu_lines[j]
                        else:
                            line = ' ' * (main_w + side_w + 3)
                        text_box.append('│' + line + '│')
                    text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
                    content = '\n'.join(main_box + text_box)
                    self.draw_frame(content)
                    key = msvcrt.getch()
                    if key in (b'\r', b'\n'):
                        if sel == len(spell_names):
                            break
                    elif key == b'\xe0':
                        arrow = msvcrt.getch()
                        if arrow == b'H':
                            menu.move_up()
                        elif arrow == b'P':
                            menu.move_down()
                return
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
