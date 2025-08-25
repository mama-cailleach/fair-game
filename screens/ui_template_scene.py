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
