from .ui_template_scene import UITemplateScene
from .utils import load_art, ArrowMenu

class CharChoiceScene(UITemplateScene):
    def show(self):
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        menu = ArrowMenu(["The Investigator", "The Explorer", "The Seer"])
        # Attribute displays for each character
        attr = {
            "The Investigator": [
                "----[ MIND ]----",
                "---[ SOUL ]---",
                "--[ BODY ]--"
            ],
            "The Explorer": [
                "---[ MIND ]---",
                "--[ SOUL ]--",
                "----[ BODY ]----"
            ],
            "The Seer": [
                "--[ MIND ]--",
                "----[ SOUL ]----",
                "---[ BODY ]---"
            ]
        }
        import msvcrt
        while True:
            # Load art for the selected character
            art_file_map = {
                "The Investigator": "char_idle2_investigator.txt",
                "The Explorer": "char_idle2_explorer.txt",
                "The Seer": "char_idle2_seer.txt"
            }
            art = load_art(art_file_map[menu.get_selected()])
            art_lines = art.split('\n')
            art_pad_top = max(0, (main_h - len(art_lines)) // 2)
            main_box = []
            main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
            for i in range(main_h):
                if art_pad_top <= i < art_pad_top + len(art_lines):
                    art_line = art_lines[i - art_pad_top].ljust(main_w)
                else:
                    art_line = ' ' * main_w
                # Side box: name at top, then attributes
                if i == 2:
                    side_line = menu.get_selected().center(side_w)
                elif i == 5:
                    side_line = attr[menu.get_selected()][0].center(side_w)
                elif i == 6:
                    side_line = attr[menu.get_selected()][1].center(side_w)
                elif i == 7:
                    side_line = attr[menu.get_selected()][2].center(side_w)
                else:
                    side_line = ' ' * side_w
                main_box.append('│' + art_line + '│' + ' ' + '│' + side_line + '│')
            main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')
            # Text box with title and menu
            text_box = []
            text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
            # Title line
            title = "Choose your character".center(main_w + side_w + 3)
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
        # After selection, you can return menu.get_selected() or store the choice
