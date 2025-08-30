from .ui_template_scene import UITemplateScene
from .utils import load_art, run_skill_check

class Chapter2DialoguesScene(UITemplateScene):
    def __init__(self, player):
        self.player = player

    def show(self):
        # Lines from chapter2.md (one per line, as in the file)
        lines = [
            "",
            "You look out at the parade, your eyes darting through the happy crowds, ",
            "searching for someone who might hold the first clue.",
            "",
            "First, you spot a group of flower girls, giggling and gossiping among themselves.",
            "The Queen has just dismissed them, and they seem a bit annoyed, ",
            "but also excited to be sharing a secret.",
            "They look like they know something important.",
            "Just then, a few small faeries flicker by, their wings shimmering.",
            "They look at the Queen but do not approach her. ",
            "You notice the Champion seems to be keeping them away.",
            "They just exchange knowing glances with each other, as if they have a task of their own.",
            "A little further away, a group of witches watches the parade from a distance.",
            "They are separate from the main crowd, but they seem happy and at peace.",
            "They feel like the right people to talk to, like they might understand your quest",
            "in a way no one else would."
        ]
        idx = 0
        art_files = [
            'walking2.txt',
            '3girls1.txt',
            'girls1.txt',
            'witches3.txt',
        ]
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        # Show intro lines in pages of 4
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

        # After intro, show menu for who to talk to
        from .utils import ArrowMenu
        import msvcrt
        # Art file mapping for menu and handlers
        art_file_map = {
            "Flower Girls": "3girls1.txt",
            "Faeries": "girls1.txt",
            "Witches": "witches3.txt"
        }
        while True:
            if self.player.char_class == "The Explorer":
                menu = ArrowMenu(["Flower Girls", "Witches"])
            else:
                menu = ArrowMenu(["Flower Girls", "Faeries", "Witches"])
            while True:
                selected_option = menu.get_selected()
                art_file = art_file_map.get(selected_option, 'chapter2_1.txt')
                art = load_art(art_file)
                art_lines = art.split('\n')
                # Build main art/side box
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
                # Build text box
                menu_lines = menu.get_display(main_w + side_w + 3)
                text_box = []
                text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
                title = "Who do you want to talk to?".center(main_w + side_w + 3)
                text_box.append('│' + title + '│')
                for j in range(text_h - 1):
                    if j < len(menu_lines):
                        line = menu_lines[j]
                    else:
                        line = ' ' * (main_w + side_w + 3)
                    text_box.append('│' + line + '│')
                text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
                # Draw everything
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
            # Branch to handler for each choice, passing art file
            choice = menu.get_selected()
            if choice == "Flower Girls":
                self.handle_flower_girls(art_file=art_file_map["Flower Girls"])
            elif choice == "Faeries":
                self.handle_faeries(art_file=art_file_map["Faeries"])
            elif choice == "Witches":
                self.handle_witches(art_file="darkfae1.txt")
                return  # End scene after witches

    def handle_flower_girls(self, art_file=None):
        from .utils import ArrowMenu
        import msvcrt
        import random
        menu_flowers = ArrowMenu([
                "'Did you notice something different about the queen?'",
                "'Hi it's my first day here, I was travelling over night'",
                "'Where are you going to?'",
                "Talk to someone else"
            ])
        while True:
            # Draw menu
            menu_lines = menu_flowers.get_display(70 + 20 + 3)
            self.show_dialogue_box(["The Flower Girls giggle and look at you curiously."] + menu_lines, art_file="3girls2.txt")
            key = msvcrt.getch()
            if key in (b'\r', b'\n'):
                choice = menu_flowers.get_selected()
                if choice == "'Did you notice something different about the queen?'":
                    responses = [
                        [
                            "",
                            " - She was so odd! Not at all like she was yesterday!",
                            "",
                            " - I don't know what bug bit her, but she looked so grumpy.",
                        ],
                        [
                            "",
                            " - She was so quick to send us away...it was kind of rude.",
                            "",
                            " - I heard her dress wasn't even the right shade of Fair Day blue!",
                        ]
                    ]
                    self.show_dialogue_box(random.choice(responses), art_file=art_file)
                    self.wait_for_key("")
                elif choice == "'Hi it's my first day here, I was travelling over night'":
                    responses = [
                        [
                            "",
                            " - Oh, are you new? It's the best day ever!",
                            "",
                            " - We're parading to the Town Hall, then we'll sing and prepare for the crowning.",
                        ],
                        [
                            "",
                            " - The Queen gets her crown, and then we all dance and have fun!",
                            "",
                            " - There's going to be a big dance and a special present for the Queen.",
                        ]
                    ]
                    self.show_dialogue_box(random.choice(responses), art_file=art_file)
                    self.wait_for_key("")
                elif choice == "'Where are you going to?'":
                    responses = [
                        [
                            "",
                            " - To the Town Hall, for the crowning and dancing!",
                            "",
                            " - To sing the songs for the Queen!",
                        ],
                        [
                            "",
                            " - We're going to see the Queen get her crown at the Town Hall!",
                            "",
                            " - And a big parade and celebration to the park!",
                        ]
                    ]
                    self.show_dialogue_box(random.choice(responses), art_file=art_file)
                    self.wait_for_key("")
                elif choice == "Talk to someone else":
                    return  # Go back to main menu
            elif key == b'\xe0':
                arrow = msvcrt.getch()
                if arrow == b'H':
                    menu_flowers.move_up()
                elif arrow == b'P':
                    menu_flowers.move_down()

    def handle_faeries(self, art_file=None):
        from .utils import ArrowMenu
        import msvcrt
        import random
        menu_faeries = ArrowMenu([
                "'Hi, did you notice anything odd today?'",
                "'What was that with the Champion all about?'",
                "'How much time is there until the crowning?'",
                "Talk to someone else"
            ])
        while True:
            menu_lines = menu_faeries.get_display(70 + 20 + 3)
            self.show_dialogue_box(["The faeries hover nearby, their wings shimmering."] + menu_lines, art_file="girls2.txt")
            key = msvcrt.getch()
            if key in (b'\r', b'\n'):
                choice = menu_faeries.get_selected()
                if choice == "'Hi, did you notice anything odd today?'":
                    responses = [
                        [
                            "",
                            " - The air is… wrong. Like a bad note in a sweet song.",
                            "",
                            " - The Queen's sparkle is dim today, it's a very sad thing.",
                        ],
                        [
                            "",
                            " - We can feel it, a creeping shadow from the south.",
                            "",
                            " - The magic here feels… off. It's not right.",
                        ]
                    ]
                    self.show_dialogue_box(random.choice(responses), art_file=art_file)
                    self.wait_for_key("")
                elif choice == "'What was that with the Champion all about?'":
                    responses = [
                        [
                            "",
                            " - He's suddenly not a friend of our folk anymore.",
                            "",
                            " - He stopped us from getting close to the Queen. But why?",
                        ],
                        [
                            "",
                            " - His spirit turned dark. We can feel it.",
                            "",
                            " - He is being too serious for a day of such joy.",
                        ]
                    ]
                    self.show_dialogue_box(random.choice(responses), art_file=art_file)
                    self.wait_for_key("")
                elif choice == "'How much time is there until the crowning?'":
                    responses = [
                        [
                            "",
                            " - The bells will ring soon, when the sun is highest.",
                            "",
                            " - The magic will be at its peak at noon.",
                        ],
                        [
                            "",
                            " - The dance and crowning are close.",
                            "",
                            " - Not long until the crown get's it's place on her head.",
                        ]
                    ]
                    self.show_dialogue_box(random.choice(responses), art_file=art_file)
                    self.wait_for_key("")
                elif choice == "Talk to someone else":
                    return  # Go back to main menu
            elif key == b'\xe0':
                arrow = msvcrt.getch()
                if arrow == b'H':
                    menu_faeries.move_up()
                elif arrow == b'P':
                    menu_faeries.move_down()

    def handle_witches(self, art_file=None):
        # Framework for Witches dialogue/choices
        self.show_dialogue_box([
            "You tiptoed through the bustling fair, listening carefully. ",
            "Flower girls giggling. ",
            "Friendly faeries flying. ",
            "Every step made you realize there wasn't much time left!",
        ], art_file=art_file)
        self.wait_for_key("")

    def show_dialogue_box(self, lines, art_file=None):
        # Show dialogue with main art and side box, consistent with other scenes
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        # Use provided art file or default to first art
        if art_file is None:
            art_file = 'chapter2_1.txt'
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
        # Dialogue text box at bottom
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
