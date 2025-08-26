import os

def load_art(filename):
    art_path = os.path.join('assets', 'art', filename)
    if not os.path.exists(art_path):
        return '[Art not found]'
    with open(art_path, encoding='utf-8') as f:
        return f.read()

class ArrowMenu:
    def __init__(self, options):
        self.options = options
        self.selected = 0

    def move_up(self):
        self.selected = (self.selected - 1) % len(self.options)

    def move_down(self):
        self.selected = (self.selected + 1) % len(self.options)

    def get_display(self, width):
        lines = []
        for i, opt in enumerate(self.options):
            prefix = '> ' if i == self.selected else '  '
            lines.append((prefix + opt).ljust(width))
        return lines

    def get_selected(self):
        return self.options[self.selected]
