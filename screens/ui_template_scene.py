from .base_screen import BaseScreen

class UITemplateScene(BaseScreen):
    def show(self):
        # Dimensions
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        total_w = main_w + side_w + 3  # 3 for borders/spaces
        total_h = main_h + text_h + 3  # 3 for borders/spaces

        # Draw main rectangle (image area)
        main_box = []
        main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
        for _ in range(main_h):
            main_box.append('│' + ' ' * main_w + '│' + ' ' + '│' + ' ' * side_w + '│')
        main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')

        # Draw text box (underneath both)
        text_box = []
        text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
        for _ in range(text_h):
            text_box.append('│' + ' ' * (main_w + side_w + 3) + '│')
        text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')

        # Combine
        content = '\n'.join(main_box + text_box)
        self.draw_frame(content)
        self.wait_for_key("This is the UI template. Press Enter to continue...")

    def show_dialogue_box(self, lines, main_w=70, side_w=20, text_h=6):
        
        # Draws a dialogue box with up to text_h lines, with "> Next" on the last line
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
        # Draw the box below the main art/side box
        content = '\n'.join(text_box)
        self.draw_frame(content)

