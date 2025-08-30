import random
import time
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Skill check system: coin toss + stat, with animation and outcome
def run_skill_check(player, attribute, scene, main_w=70, main_h=22, side_w=20):
    # Animation frames for coin toss
    frames = [
        "   ...   ",
        "   ....   ",
        "   .......   ",
        "   ...........   "
    ]
    art_frames = [
    "char_idle3.txt",
    "char_idle4.txt",
    "char_idle5.txt",
    "char_idle4.txt",
    "char_idle3.txt",
    "char_idle4.txt",
    "char_idle5.txt",
    "char_idle4.txt",
    "char_idle3.txt"
    ]
    # Show animation in the main box
    for i in range(8):
        #frame = frames[i % len(frames)]
        # Cycle through art frames
        art_file = art_frames[i % len(art_frames)]
        art = load_art(art_file)
        art_lines = art.split('\n')
        art_pad_top = max(0, (main_h - len(art_lines)) // 2)
        main_box = []
        main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
        for j in range(main_h):
            if art_pad_top <= j < art_pad_top + len(art_lines):
                art_line = art_lines[j - art_pad_top].center(main_w)
            #if j == main_h // 2:
            #    art_line = frame.center(main_w)
            else:
                art_line = ' ' * main_w
            # Side box: show player class and attributes
            if j == 2:
                side_line = player.char_class.center(side_w)
            elif j == 5:
                side_line = player.attr_labels[0].center(side_w)
            elif j == 6:
                side_line = player.attr_labels[1].center(side_w)
            elif j == 7:
                side_line = player.attr_labels[2].center(side_w)
            else:
                side_line = ' ' * side_w
            main_box.append('│' + art_line + '│' + ' ' + '│' + side_line + '│')
        main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')
            # Add text box UI (empty except for '> Next' on last line)
        text_h = 6
        text_box = []
        text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
        for k in range(text_h):
            if k == text_h - 1:
                next_str = "> Wait"
                line = ' ' * (main_w + side_w + 3 - len(next_str) - 1) + next_str + ' '
            else:
                line = ' ' * (main_w + side_w + 3)
            text_box.append('│' + line + '│')
        text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
        scene.draw_frame('\n'.join(main_box + text_box))
        time.sleep(0.08)
    # Coin toss: 0 or 1
    coin = random.choice([0, 1])
    stat = player.stats[attribute]
    total = stat + coin
    # Clamp to 1-4
    total = max(1, min(4, total))
    # Outcome text
    outcome_map = {
        4: "A Bonny Lilt!!",
        3: "A Wee Glimmer!",
        2: "A Muckle Stumble!",
        1: "A Bit of a Fankle!"
    }
    outcome = outcome_map[total]
    # Show result in main box
    result_lines = [
        f"Skill Check: {attribute.upper()}",
        f"{attribute} Score: {stat}  |  Coin Bonus: +{coin}",
        f"Result: {stat} + {coin} = {total}",
        f"Outcome: {outcome}",
        ""
    ]
    main_box = []
    main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
    for j in range(main_h):
        if 2 <= j < 2 + len(result_lines):
            art_line = result_lines[j-2].center(main_w)
        else:
            art_line = ' ' * main_w
        # Side box: show player class and attributes
        if j == 2:
            side_line = player.char_class.center(side_w)
        elif j == 5:
            side_line = player.attr_labels[0].center(side_w)
        elif j == 6:
            side_line = player.attr_labels[1].center(side_w)
        elif j == 7:
            side_line = player.attr_labels[2].center(side_w)
        else:
            side_line = ' ' * side_w
        main_box.append('│' + art_line + '│' + ' ' + '│' + side_line + '│')
    main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')
    # Add text box UI (empty except for '> Next' on last line)
    text_h = 6
    text_box = []
    text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
    for k in range(text_h):
        if k == text_h - 1:
            next_str = "> Next"
            line = ' ' * (main_w + side_w + 3 - len(next_str) - 1) + next_str + ' '
        else:
            line = ' ' * (main_w + side_w + 3)
        text_box.append('│' + line + '│')
    text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
    scene.draw_frame('\n'.join(main_box + text_box))
    # Wait for Enter
    try:
        input()
    except Exception:
        pass
    return total
import os

def load_art(filename):
    # Use resource_path to find the file in both dev and PyInstaller .exe
    art_path = resource_path(os.path.join('assets', 'art', filename))
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
            lines.append((prefix + opt).center(width))
        return lines

    def get_selected(self):
        return self.options[self.selected]
