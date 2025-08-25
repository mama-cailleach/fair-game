import os
import shutil

class BaseScreen:
    WIDTH = 80
    HEIGHT = 30

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_frame(self, content):
        self.clear()
        lines = content.split('\n')
        padded_lines = [line.center(self.WIDTH) for line in lines]
        empty = ' ' * self.WIDTH
        print('\n' * ((self.HEIGHT - len(padded_lines)) // 2))
        for line in padded_lines:
            print(line)
        print('\n' * (self.HEIGHT - len(padded_lines) - ((self.HEIGHT - len(padded_lines)) // 2)))

    def wait_for_key(self, prompt="Press Enter to continue..."):
        input(prompt.center(self.WIDTH))
