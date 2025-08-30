from .ui_template_scene import UITemplateScene
from .utils import load_art, ArrowMenu

class Chapter2ChoiceScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        menu = ArrowMenu(["Observe who's passing", "Start Walking through the parade"])
        import msvcrt
        art_file_map = {
            "Observe who's passing": "chapter2_choice1.txt",
            "Start Walking through the parade": "chapter2_choice2.txt"
        }
        while True:
            selected = menu.get_selected()
            # Use placeholder art for now
            art = (
                "   .--.\n"
                "  /    \\\n"
                " |      |\n"
                "  \\    /\n"
                "   '--'\n"
                " (Placeholder Art)\n"
            )
            art_lines = art.split('\n')
            art_pad_top = max(0, (main_h - len(art_lines)) // 2)
            main_box = []
            main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
            for i in range(main_h):
                if art_pad_top <= i < art_pad_top + len(art_lines):
                    art_line = art_lines[i - art_pad_top].ljust(main_w)
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
            # Text box with title and menu
            text_box = []
            text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
            # Title line
            title = "What do you do next?".center(main_w + side_w + 3)
            text_box.append('│' + title + '│')
            # Menu lines
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
            # Arrow key and enter handling (Windows, msvcrt)
            key = msvcrt.getch()
            if key in (b'\r', b'\n'):
                break
            elif key == b'\xe0':
                arrow = msvcrt.getch()
                if arrow == b'H':
                    menu.move_up()
                elif arrow == b'P':
                    menu.move_down()
        # After selection, branch to the appropriate handler
        if menu.get_selected() == "Observe who's passing":
            self.handle_observe()
        else:
            self.handle_walk()
        return self.player

    def handle_observe(self):
        char_class = getattr(self.player, 'char_class', 'The Investigator')
        if char_class == "The Seer":
            lines = [
                "You quietly sit and attune to your environment.",
                "Then, you saw a group of wonderful witches preparing a ritual as they went.",
                "Your spirit connected, you felt a pull. It was this group.",
                "You knew you could trust them, you knew they will have answers for you",
            ]
            self.show_dialogue_with_ui(lines)
            self.wait_for_key("")
            # Transition to next scene here if needed
        else:
            # Transition to a new dialogue scene for branching
            from .chapter2_dialogues_scene import Chapter2DialoguesScene
            scene = Chapter2DialoguesScene(self.player)
            scene.show()

    def handle_walk(self):
        # Dialogue for 'Start Walking through the parade' branch, by player class
        investigator_lines = [
            "You tiptoed through the bustling fair, listening carefully.",
            "Every chat made you realize there wasn't much time left!",
            "Then, you saw a group of wonderful witches preparing a ritual as they went.",
            "Slightly outside of the main group, you could see they could be they could be trusted",
        ]
        explorer_lines = [
            "You tiptoed through the bustling fair, listening carefully.",
            "You saw a group of wonderful witches preparing a ritual as they went.",
            "Their motions were fluid and confident, you knew they would be the right people to help.",
            "They would know the way around obstacles you couldn't see.",
        ]
        seer_lines = [
            "You tiptoed through the bustling fair, listening carefully.",
            "Then, you saw a group of wonderful witches preparing a ritual as they went.",
            "Your spirit connected, you felt a pull. It was this group.",
            "You knew you could trust them, you knew they will have answers for you",
        ]
        char_class = getattr(self.player, 'char_class', 'The Investigator')
        if char_class == "The Investigator":
            lines = investigator_lines
        elif char_class == "The Explorer":
            lines = explorer_lines
        elif char_class == "The Seer":
            lines = seer_lines
        else:
            lines = ["[Unknown class]", "Change Scene Placeholder"]
        self.show_dialogue_with_ui(lines)
        self.wait_for_key("")

    def show_dialogue_with_ui(self, lines):
        # Show dialogue in the main UI layout, preserving art and side box
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        # Placeholder art for now
        art = (
            "   .--.\n"
            "  /    \\\n"
            " |      |\n"
            "  \\    /\n"
            "   '--'\n"
            " (Placeholder Art)\n"
        )
        art_lines = art.split('\n')
        art_pad_top = max(0, (main_h - len(art_lines)) // 2)
        main_box = []
        main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
        for i in range(main_h):
            if art_pad_top <= i < art_pad_top + len(art_lines):
                art_line = art_lines[i - art_pad_top].ljust(main_w)
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
        # Text box with dialogue lines
        text_box = []
        text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
        for j in range(text_h):
            if j < len(lines):
                line = lines[j].center(main_w + side_w + 3)
            else:
                line = ' ' * (main_w + side_w + 3)
            if j == text_h - 1:
                next_str = "> Next"
                line = line[:-len(next_str)-1] + next_str + ' '
            text_box.append('│' + line + '│')
        text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
        content = '\n'.join(main_box + text_box)
        self.draw_frame(content)

    def draw_text_box(self, lines):
        main_w = 70
        side_w = 20
        text_h = 6
        text_box = []
        text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
        for j in range(text_h):
            if j < len(lines):
                line = lines[j].center(main_w + side_w + 3)
            else:
                line = ' ' * (main_w + side_w + 3)
            if j == text_h - 1:
                next_str = "> Next"
                line = line[:-len(next_str)-1] + next_str + ' '
            text_box.append('│' + line + '│')
        text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
        self.draw_frame('\n'.join(text_box))