from .ui_template_scene import UITemplateScene
from .utils import load_art, ArrowMenu
import msvcrt

class Chapter5FightScene(UITemplateScene):
    def draw_battle_ui(self, main_lines, text_lines, plyr_hp, champ_hp):
        # Draws the main art/side box and puts text_lines in the normal text box area
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6
        art = load_art("battle_placeholder.txt")
        art_lines = art.split('\n')
        art_pad_top = max(0, (main_h - len(art_lines)) // 2)
        main_box = []
        main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
        for i in range(main_h):
            if art_pad_top <= i < art_pad_top + len(art_lines):
                art_line = art_lines[i - art_pad_top].center(main_w)
            else:
                art_line = ' ' * main_w
            # Side box: show player class, stats, and spells
            if i == 2:
                side_line = self.player.char_class.center(side_w)
            elif i == 4:
                side_line = f"HP: {plyr_hp}".center(side_w)
            elif i == 5:
                side_line = f"Champion: {champ_hp}".center(side_w)
            elif i == 7 and hasattr(self.player, "spells"):
                side_line = "Spells:".center(side_w)
            elif i >= 8 and hasattr(self.player, "spells"):
                idx = i - 8
                spells = getattr(self.player, "spells", [])
                if idx < len(spells):
                    side_line = spells[idx][:side_w].center(side_w)
                else:
                    side_line = ' ' * side_w
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
            text_box.append('│' + line + '│')
        text_box.append('└' + '─' * (main_w + side_w + 3) + '┘')
        content = '\n'.join(main_box + text_box)
        self.draw_frame(content)
    def __init__(self, player):
        self.player = player

    def show(self):
        # Initial HP
        champion_hp = 10
        player_hp = 10 + self.player.stats.get("Body", 0)
        main_w = 70
        main_h = 22
        side_w = 20
        text_h = 6

        # Build action list based on class and spells
        class_actions = {
            "The Investigator": [
                ("Analyze Weakness", "Use your sharp mind to spot an opening.", "Mind", 3),
                ("Spirit Shield", "Block with a magical shield.", "Soul", 2)
            ],
            "The Explorer": [
                ("Acrobatic Leap", "Leap and strike from above!", "Body", 3),
                ("Tackle", "Tackle the Champion fiercely.", "Body", 2)
            ],
            "The Seer": [
                ("Premonition", "Predict the Champion's move and counter.", "Soul", 3),
                ("Tackle", "Tackle the Champion fiercely.", "Body", 2)
            ]
        }
        # Add spell actions (all use SOUL, but logic will branch below)
        spell_actions = []
        for spell in getattr(self.player, "spells", []):
            spell_actions.append((spell, f"Cast {spell}!", "Soul", 0))  # base_attack not used, logic below

        # Combine actions for menu
        actions = class_actions.get(self.player.char_class, [])
        spell_names = [s[0] for s in spell_actions]
        # Battle loop
        import random
        # Buff/debuff state
        champion_smug_buff = 0
        player_defense = 0
        analyze_weakness_buff = 0
        premonition_debuff = 0
        champion_stun = 0
        feather_stun = 0
        tickle_stun = 0
        while True:
            champ_hp = champion_hp
            plyr_hp = player_hp
            champion_smug_buff = 0
            player_defense = 0
            analyze_weakness_buff = 0
            premonition_debuff = 0
            champion_stun = 0
            feather_stun = 0
            tickle_stun = 0
            while champ_hp > 0 and plyr_hp > 0:
                # Main action menu: class actions + 'Cast a Spell' if spells exist
                menu_options = [a[0] for a in actions]
                if spell_actions:
                    menu_options.append("Cast a Spell")
                menu = ArrowMenu(menu_options)
                while True:
                    # Draw UI
                    art = load_art("battle_placeholder.txt")
                    art_lines = art.split('\n')
                    art_pad_top = max(0, (main_h - len(art_lines)) // 2)
                    main_box = []
                    main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
                    for i in range(main_h):
                        if art_pad_top <= i < art_pad_top + len(art_lines):
                            art_line = art_lines[i - art_pad_top].center(main_w)
                        else:
                            art_line = ' ' * main_w
                        # Side box: show player class, stats, and spells
                        if i == 2:
                            side_line = self.player.char_class.center(side_w)
                        elif i == 4:
                            side_line = f"HP: {plyr_hp}".center(side_w)
                        elif i == 5:
                            side_line = f"Champion: {champ_hp}".center(side_w)
                        elif i == 7 and hasattr(self.player, "spells"):
                            side_line = "Spells:".center(side_w)
                        elif i >= 8 and hasattr(self.player, "spells"):
                            idx = i - 8
                            spells = getattr(self.player, "spells", [])
                            if idx < len(spells):
                                side_line = spells[idx][:side_w].center(side_w)
                            else:
                                side_line = ' ' * side_w
                        else:
                            side_line = ' ' * side_w
                        main_box.append('│' + art_line + '│' + ' ' + '│' + side_line + '│')
                    main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')
                    # Text box with action menu
                    text_box = []
                    text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
                    title = "Choose your action:".center(main_w + side_w + 3)
                    text_box.append('│' + title + '│')
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
                    key = msvcrt.getch()
                    if key in (b'\r', b'\n'):
                        break
                    elif key == b'\xe0':
                        arrow = msvcrt.getch()
                        if arrow == b'H':
                            menu.move_up()
                        elif arrow == b'P':
                            menu.move_down()
                # Player action
                action_idx = menu.selected
                if spell_actions and action_idx == len(actions):
                    # Spell menu
                    spell_menu = ArrowMenu([s[0] for s in spell_actions])
                    while True:
                        # Draw spell menu
                        art = load_art("battle_placeholder.txt")
                        art_lines = art.split('\n')
                        art_pad_top = max(0, (main_h - len(art_lines)) // 2)
                        main_box = []
                        main_box.append('┌' + '─' * main_w + '┐' + ' ' + '┌' + '─' * side_w + '┐')
                        for i in range(main_h):
                            if art_pad_top <= i < art_pad_top + len(art_lines):
                                art_line = art_lines[i - art_pad_top].center(main_w)
                            else:
                                art_line = ' ' * main_w
                            # Side box: show player class, stats, and spells
                            if i == 2:
                                side_line = self.player.char_class.center(side_w)
                            elif i == 4:
                                side_line = f"HP: {plyr_hp}".center(side_w)
                            elif i == 5:
                                side_line = f"Champion: {champ_hp}".center(side_w)
                            elif i == 7 and hasattr(self.player, "spells"):
                                side_line = "Spells:".center(side_w)
                            elif i >= 8 and hasattr(self.player, "spells"):
                                idx = i - 8
                                spells = getattr(self.player, "spells", [])
                                if idx < len(spells):
                                    side_line = spells[idx][:side_w].center(side_w)
                                else:
                                    side_line = ' ' * side_w
                            else:
                                side_line = ' ' * side_w
                            main_box.append('│' + art_line + '│' + ' ' + '│' + side_line + '│')
                        main_box.append('└' + '─' * main_w + '┘' + ' ' + '└' + '─' * side_w + '┘')
                        # Text box with spell menu
                        text_box = []
                        text_box.append('┌' + '─' * (main_w + side_w + 3) + '┐')
                        title = "Choose a spell:".center(main_w + side_w + 3)
                        text_box.append('│' + title + '│')
                        spell_menu_lines = spell_menu.get_display(main_w + side_w + 3)
                        for j in range(text_h - 1):
                            if j < len(spell_menu_lines):
                                line = spell_menu_lines[j]
                            else:
                                line = ' ' * (main_w + side_w + 3)
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
                                spell_menu.move_up()
                            elif arrow == b'P':
                                spell_menu.move_down()
                    spell_idx = spell_menu.selected
                    action = spell_actions[spell_idx]
                else:
                    action = actions[action_idx]
                # --- CLASS ACTIONS LOGIC ---
                action_name, action_desc, stat, base_attack = action
                # Investigator
                if action_name == "Analyze Weakness":
                    mind = self.player.stats.get("Mind", 0)
                    analyze_weakness_buff = mind
                    self.draw_battle_ui([], [
                        "You use your keen mind to take a moment and see this Champion's weakness",
                        f"Your next attack will deal added +{mind} damage"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    damage = 0
                elif action_name == "Spirit Shield":
                    soul = self.player.stats.get("Soul", 0)
                    player_defense = soul
                    self.draw_battle_ui([], [
                        "You tap into your soul to conjure a shield around you",
                        f"You gain +{soul} of Defense against the next attack!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    damage = 0
                # Explorer
                elif action_name == "Acrobatic Leap":
                    body = self.player.stats.get("Body", 0)
                    soul = self.player.stats.get("Soul", 0)
                    damage = body + soul
                    self.draw_battle_ui([], [
                        "You leap like a cat and land on the Champion!",
                        f"He takes {damage} damage!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    champ_hp -= damage
                elif action_name == "Tackle":
                    body = self.player.stats.get("Body", 0)
                    damage = body
                    self.draw_battle_ui([], [
                        "A classic tackle!",
                        f"The Champion takes {damage} damage!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    champ_hp -= damage + analyze_weakness_buff
                    if analyze_weakness_buff:
                        self.draw_battle_ui([], [
                            f"Your Analyze Weakness bonus adds +{analyze_weakness_buff} damage!"
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                        analyze_weakness_buff = 0
                # Seer
                elif action_name == "Premonition":
                    soul = self.player.stats.get("Soul", 0)
                    premonition_debuff = soul
                    self.draw_battle_ui([], [
                        "You see into the future and know exactly what's going to happen!",
                        f"The champion gets a -{soul} to his next move."
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    damage = 0
                # --- SPELLS LOGIC ---
                elif action_name in spell_names:
                    soul = self.player.stats.get("Soul", 0)
                    # Broom Charm
                    if action_name == "Broom Charm":
                        damage = 1 + soul
                        if analyze_weakness_buff:
                            damage += analyze_weakness_buff
                            analyze_weakness_buff = 0
                        self.draw_battle_ui([], [
                            "The broom you used to come here comes alive again.",
                            f"It goes brushing the Champion for {damage} damage!"
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                        champ_hp -= damage
                    # Feather Spell
                    elif action_name == "Feather Spell":
                        feather_stun = 1
                        self.draw_battle_ui([], [
                            "A little feather tickles the opponent!",
                            "It can't move for this round."
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                    # Tickle Spell
                    elif action_name == "Tickle Spell":
                        tickle_stun = 2
                        self.draw_battle_ui([], [
                            "The Champion starts to laugh uncontrollably!",
                            "He will take 2 turns to recover."
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                    # Liar Liar, Pants on Fire
                    elif action_name == "Liar Liar":
                        damage = 2 + soul
                        if analyze_weakness_buff:
                            damage += analyze_weakness_buff
                            analyze_weakness_buff = 0
                        self.draw_battle_ui([], [
                            "You lied to us all! How can you be the Champion?",
                            f"Fire comes up from his pants for {damage} damage!"
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                        champ_hp -= damage
                    # Black Cat
                    elif action_name == "Black Cat":
                        damage = 3 + soul
                        self.draw_battle_ui([], [
                            "A ghostly black cat appears and starts scratching the Champion's face!",
                            f"Ouch! He takes {damage} damage!"
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                        champ_hp -= damage
                    # Liars Liars, Pants on Fire
                    elif action_name == "Liars Liars":
                        damage = 4 + soul
                        self.draw_battle_ui([], [
                            "Do you smell something burning? Oh, it's the Champion and the fake Queen!",
                            f"Both of their pants are on fire as they take {damage} damage!"
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                        champ_hp -= damage
                # Default: if not handled, do nothing
                else:
                    damage = 0

                if champ_hp <= 0:
                    self.draw_battle_ui([], [
                        "The Champion is defeated!",
                        "You win the battle!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    return  # Move on to next scene
                # --- CHAMPION TURN ---
                # Handle stuns
                if feather_stun > 0:
                    self.draw_battle_ui([], [
                        "The Champion is tickled by a feather and can't move this round!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    feather_stun -= 1
                    continue
                if tickle_stun > 0:
                    self.draw_battle_ui([], [
                        "The Champion is still laughing and can't move this round!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    tickle_stun -= 1
                    continue
                # Champion's turn: Tackle, Heal, or Smug
                champ_action = random.choice(["Tackle"]*2 + ["Heal", "Smug"])
                if champ_action == "Tackle":
                    champ_attack = 3 + champion_smug_buff
                    if premonition_debuff:
                        champ_attack = max(0, champ_attack - premonition_debuff)
                        self.draw_battle_ui([], [
                            f"Your Premonition reduces the Champion's attack by {premonition_debuff}!"
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                        premonition_debuff = 0
                    if player_defense:
                        champ_attack = max(0, champ_attack - player_defense)
                        self.draw_battle_ui([], [
                            f"Your Spirit Shield blocks {player_defense} damage!"
                        ], plyr_hp, champ_hp)
                        self.wait_for_key("")
                        player_defense = 0
                    self.draw_battle_ui([], [
                        "The Champion uses Tackle!",
                        f"You lose {champ_attack} HP!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    plyr_hp -= champ_attack
                    champion_smug_buff = 0
                elif champ_action == "Heal":
                    self.draw_battle_ui([], [
                        "The Champion uses Heal!",
                        "He regains 2 HP!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    champ_hp += 2
                elif champ_action == "Smug":
                    self.draw_battle_ui([], [
                        "The Champion looks smug...",
                        "His next Tackle will be stronger!"
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    champion_smug_buff += 1
                if plyr_hp <= 0:
                    self.draw_battle_ui([], [
                        "Oh no! You fainted!",
                        "Press ENTER to try again."
                    ], plyr_hp, champ_hp)
                    self.wait_for_key("")
                    break  # Restart battle loop
