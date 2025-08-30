from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter4KnightBattleScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        import msvcrt
        from .utils import ArrowMenu
        # Use the same spell data as postritual scene
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
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        # Get outcome from player object
        outcome = getattr(self.player, 'soul_ritual_outcome', 1)
        spell_names = spell_data.get(outcome, spell_data[1])
        menu = ArrowMenu(spell_names)
        art_files = ["spell_placeholder.txt"] * len(spell_names)
        # Dialogue outcomes for each spell
        spell_dialogue = {
            "Broom Charm": [
                "Hmm is not time to use this right now",
                "[GO BACK TO THE MENU]"
            ],
            "Feather Spell": [
                "A ghostly feather tickles the knight's cheek, causing him to flinch.",
                "As he swats at the empty air, you tackle his sword from his grasp.",
                "Startled, he disappears into the shadows.",
                "[MOVE ON TO NEXT SCENE]"
            ],
            "Tickle Spell": [
                "The knight suddenly erupts into uncontrollable giggles",
                "His armor shakes with laughter.",
                "He drops his sword with a clatter.",
                " 'Touché!' he chuckles, before vanishing.",
                "[MOVE ON TO NEXT SCENE]"
            ],
            "Black Cat": [
                "You summon a shimmering black cat, which lets out a playful meow.",
                "The knight is smitten, and he drops his sword to pick up the new friend.",
                "He hugs you, presents you with his sword as a gift, ",
                "and skips down the hall, playing with his new companion.",
                "[MOVE ON TO NEXT SCENE]"
            ],
            "Liar Liar": [
                "Hmm is not time to use this right now",
                "[GO BACK TO THE MENU]"
            ],
            "Liars Liars": [
                "Hmm is not time to use this right now",
                "[GO BACK TO THE MENU]"
            ]
        }
        while True:
            sel = menu.selected
            # Show art for selected spell
            art_file = art_files[sel]
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
            # Text box: show title and menu
            text_box = []
            text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
            title = "Choose your spell:".center(main_w + side_w + 3)
            text_box.append('│' + title + '│')
            menu_lines = menu.get_display(main_w + side_w + 3)
            for j in range(text_h - 1):
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
                spell = spell_names[sel]
                dialogue = spell_dialogue.get(spell, ["Nothing happens."])
                # Remove bracketed action lines for display, but keep for logic
                display_lines = [d for d in dialogue if not (d.startswith('[') and d.endswith(']'))]
                # Show up to 4 lines at once, then > Next
                idx2 = 0
                while idx2 < len(display_lines):
                    main_box2 = main_box.copy()
                    text_box2 = []
                    text_box2.append('┌' + '─' * (main_w + side_w + 3) + '┐')
                    for j in range(4):
                        if idx2 + j < len(display_lines):
                            line = display_lines[idx2 + j].center(main_w + side_w + 3)
                        else:
                            line = ' ' * (main_w + side_w + 3)
                        text_box2.append('│' + line + '│')
                    # Fill remaining lines if less than text_h
                    for j in range(text_h - 1 - 4):
                        text_box2.append('│' + ' ' * (main_w + side_w + 3) + '│')
                    # Last line: > Next
                    next_str = "> Next"
                    line = ' ' * (main_w + side_w + 3 - len(next_str) - 1) + next_str + ' '
                    text_box2.append('│' + line + '│')
                    text_box2.append('└' + '─' * (main_w + side_w + 3) + '┘')
                    content2 = '\n'.join(main_box2 + text_box2)
                    self.draw_frame(content2)
                    self.wait_for_key("")
                    idx2 += 4
                # If this spell moves on, break loop, else return to menu
                if any("MOVE ON TO NEXT SCENE" in d for d in dialogue):
                    return
                # Otherwise, go back to menu
            elif key == b'\xe0':
                arrow = msvcrt.getch()
                if arrow == b'H':
                    menu.move_up()
                elif arrow == b'P':
                    menu.move_down()
