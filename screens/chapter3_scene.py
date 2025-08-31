from .ui_template_scene import UITemplateScene
from .utils import load_art, ArrowMenu, run_skill_check
import msvcrt

class Chapter3Scene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        lines = [
            "Looking at the map...",
            "Next to the Witches' Stone... you see another name: Carriden House.",
            "A shiver ran down your spine. This was it!",
            "This was why you were truly meant to be in Bo'ness!",
            "",
            "You hurried away from the noisy fair, following the map down a twisty, old path.",
            "Soon, you saw a big, abandoned mansion, all dark windows and broken bits.",
            "Like a sleeping monster made of stone.",
        ]
        idx = 0
        art_files = [
            'map1.txt',
            'castle3.txt'
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6

        # Show intro lines as usual
        while idx < len(lines):
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

        # Choice point for all classes
        menu = ArrowMenu(["Yes", "No "])
        while True:
            # Draw the choice UI
            art = load_art("castle6.txt")
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
            # Text box with the choice
            text_box = []
            text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
            prompt = "Try to find a way inside?".center(main_w + side_w + 3)
            text_box.append('│' + prompt + '│')
            menu_lines = menu.get_display(main_w + side_w + 3)
            for j in range(text_h - 2):
                if j < len(menu_lines):
                    line = menu_lines[j]
                else:
                    line = ' ' * (main_w + side_w + 3)
                text_box.append('│' + line + '│')
            # Last line: > Next
            next_str = "      "
            line = ' ' * (main_w + side_w + 3 - len(next_str) - 1) + next_str + ' '
            text_box.append('│' + line + '│')
            text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
            content = '\n'.join(main_box + text_box)
            self.draw_frame(content)
            key = msvcrt.getch()
            if key in (b'\r', b'\n'):
                break
            elif key == b'\xe0':
                arrow = msvcrt.getch()
                if arrow == b'H':
                    menu.move_up()
                elif arrow == b'P':
                    menu.move_down()
        choice = menu.get_selected()
        if choice == "No ":
            # Show ghost/stone dialogue, then proceed to next scene
            ghost_lines = [
                "",
                "A sudden, cold WHOOSH made you jump!",
                 "You saw a sparkly, see-through shape—a ghostly knight!",
                 "",
                 "",
                "You ran and ran and ran until you tripped over.",
                "You looked down. It was a low, wide, smooth, mossy stone, hidden in undergrowth.",
                "This was the Witches' Stone!"
            ]
            idx = 0
            art_files = [
            'person1.txt',
            'forrest1.txt'
            ]
            while idx < len(ghost_lines):
                text_lines = ghost_lines[idx:idx+4]
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
            # Proceed to next scene (return from show)
            return
        else:
            # YES: Skill check (BODY)
            outcome_num = run_skill_check(self.player, 'Body', self, main_w, main_h, side_w)
            outcome_map = {4: 'Success', 3: 'Success', 2: 'Fail', 1: 'Fail'}
            outcome_key = outcome_map[outcome_num]
            if outcome_key in ['Success']:
                # Success: show success dialogue, then transition to maze scene (placeholder)
                success_lines = [
                    "",
                    "You found a way inside, but it was so dusty and cluttered with old things.",
                    "It is hard to move! But you push through.",
                    "",
                ]
                idx = 0
                while idx < len(success_lines):
                    text_lines = success_lines[idx:idx+4]
                    art_file = "door5.txt"
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
                # Placeholder: transition to maze mini-game scene here
                from .chapter3_maze_scene import Chapter3MazeScene
                maze_scene = Chapter3MazeScene(self.player)
                maze_scene.show()
                #return
            else:
                # Failure: show failure dialogue, then proceed to next scene
                fail_lines = [
                    "",
                    "You tried to get inside, but the door was locked tight!",
                    "You pushed and pulled, but it wouldn't budge.",
                    "",
                    "",
                    "Your wiggling and giggling had woken something else!",
                    "A sudden, cold WHOOSH made you jump!", 
                    "You saw a sparkly, see-through shape—a ghostly knight!",
                    "It was guarding the door! It pushed you away!",
                    "You quickly scrambled out of the house, your heart doing a wild dance in your chest.",
                    "You ran and ran and ran until you tripped over.",
                    "You looked down. It was a low, wide, smooth, mossy stone, hidden in undergrowth.",
                    "",
                    "",
                    "This was the Witches' Stone!"
                    "",
                ]
                idx = 0
                art_files = [
                'door5.txt',
                'person1.txt',
                'forrest1.txt',
                'forrest2.txt'
                ]
                while idx < len(fail_lines):
                    text_lines = fail_lines[idx:idx+4]
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
                return