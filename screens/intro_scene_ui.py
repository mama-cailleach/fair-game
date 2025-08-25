from .ui_template_scene import UITemplateScene

class IntroSceneUI(UITemplateScene):
    def show(self):
        main_text = "Welcome to Bo'ness!"
        # The intro story lines
        lines = [
            "You are a wanderer who has just arrived in town on the night of the FAIR E'EN.",
            "The air is thick with anticipation, and the streets are alive", 
            "with the sounds of the Kinnel Band marching through town.",
            "You follow with the crowd, laughter and joy fill the air as you see marvelous arches.",
            "They stop to play for the Queen elect, as she smiles the warmest smile towards you.",
            "It all seems awfy braw, but something doesn't feel right...",
            "Strange things are afoot, and your adventure is about to begin!"
        ]
        idx = 0
        while idx < len(lines):
            # Show up to 3 lines at a time
            text_lines = lines[idx:idx+3]
            # Use the same dimensions as UITemplateScene
            main_w = 70
            main_h = 22
            side_w = 20
            text_h = 6
            # Main rectangle with centered main_text
            main_box = []
            main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
            for i in range(main_h):
                if i == main_h // 2:
                    line = main_text.center(main_w)
                else:
                    line = ' ' * main_w
                main_box.append('│' + line + '│' + ' ' + '│' + ' ' * side_w + '│')
            main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')
            # Text box
            text_box = []
            text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
            for j in range(text_h):
                if j < len(text_lines):
                    line = text_lines[j].ljust(main_w + side_w + 3)
                else:
                    line = ' ' * (main_w + side_w + 3)
                text_box.append('│' + line + '│')
            text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
            content = '\n'.join(main_box + text_box)
            self.draw_frame(content)
            self.wait_for_key("Press Enter to continue...")
            idx += 3
        # After all lines, return to allow next scene
