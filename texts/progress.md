# Weans Game Jam 2025 - Progress Tracker

# Battle System & Buff Logic Improvements (30/08/2025)
# Dynamic Art & Animation Improvements (30/08/2025)

- Added support for cycling between multiple ASCII art images as animation frames in skill checks and other scenes, allowing for dynamic, whimsical visual effects.
- Post-ritual spell selection scene now displays the correct ASCII art for each spell when selected, using a direct mapping from spell name to art file.
- All UI frames (including skill checks and dialogue) can now display any ASCII art from the assets/art folder, with easy switching between static and animated art.
- Improved documentation and code comments to clarify how to use art files for both static and animated displays in all scenes.
- Asset loading and resource_path logic confirmed to work for both development and PyInstaller builds.

- Analyze Weakness buff now applies to the next attack of any type (class action or spell), not just Tackle. The bonus is automatically added to the next damage calculation and then reset.
- All player attack and spell effects now display in the normal text box area, preserving the main art and side menu UI.
- Added a helper to render battle effect text in the standard UI, replacing the old show_dialogue_box method for a more consistent experience.
- Fixed spell persistence and ensured spell menu always reflects the player's learned spells from Chapter 4.
- Improved code clarity and modularity for future extensibility.

# Major Scene & System Additions (28-30/08/2025)

- Created new modular scenes for Chapter 4 and Chapter 5, including:
	- Ritual, post-ritual, knight battle, post-battle, broom, and post-fight scenes.
	- Each scene uses the shared UI template for consistent art, side menu, and text box layout.
- Implemented a robust, modular fight system for Chapter 5:
	- Player can choose between class actions and spells, with branching menus.
	- Champion AI includes Tackle, Heal, and Smug actions, with stateful buffs and debuffs.
	- All battle logic is now modular and easy to extend for new actions or effects.
- Improved spell system:
	- Spells are now assigned to the player object after the Chapter 4 ritual and persist through to the fight scene.
	- Spell menu in battle always reflects the player's learned spells.
	- Each spell has unique effects (damage, stun, etc.) and is handled in the main battle loop.
- All scenes and battles now use the ArrowMenu for interactive choices, with menu state preserved across loops.
- UI improvements:
	- All effect and action text appears in the normal text box area, never breaking the main art or side menu.
	- HP for both player and Champion is always visible in the side menu during battle.
	- Modular draw_battle_ui helper ensures consistent rendering of effects and state.



## Major Scene & Dialogue System Updates (28/08/2025)

- Implemented interactive branching dialogue menus for Flower Girls and Faeries in Chapter 2, using ArrowMenu and random dialogue sets.
- Added class-based branching: Seer gets unique dialogue, Explorer/Investigator get menu-driven choices.
- Dialogue scenes now always display the main art and side box for consistency.
- Main menu in dialogue scenes now loops until "Witches" is chosen, which advances the story.
- Chapter 3 now features a universal choice (for all classes) to try to enter the mansion, with Yes/No options.
- If "Yes" is chosen, a BODY skill check is performed:
	- Success: player gets inside, sees special dialogue, and (placeholder) transitions to a maze mini-game scene.
	- Failure: player sees a different outcome and proceeds to the next scene.
- If "No" is chosen, all players see the ghost/stone sequence and move to the next scene.
- All scene transitions and branching logic are now modular and easy to extend.

---

## Core Skill Check System Added (27/08/2025)

- Added a reusable coin toss skill check system (`run_skill_check`) to `screens/utils.py`.
- The function animates a coin toss, adds the result to the player's stat, and determines the outcome (YES AND, YES BUT, NO BUT, NO AND) for dialogue branching.
- Designed for easy use in any scene or chapter.

---

## Utility Module Refactor (26/08/2025)

- Created `screens/utils.py` to hold shared utility functions and classes.
- Moved `load_art` (for loading ASCII art) and `ArrowMenu` (for menu navigation) into `utils.py` for easy reuse across all screens.
- Updated `screens/char_choice_scene.py` to import these utilities from `utils.py`.

All major planning documents are in place. Next steps: begin coding the CLI framework and first scene.

---

## Game Structure & Features Expanded (25/08/2025)

- Added `sound_manager.py` using pygame for easy background music and sound effects.
- Background music (`ourfestal.mp3`) now plays from the title screen and continues through all scenes.
- Created `screens/ui_template_scene.py` for a consistent UI layout: main rectangle (art), side box (menu/info), and text box (dialogue).
- Updated `screens/intro_scene_ui.py` to use the new UI template and show intro text in 3-line pages.
- Added `screens/art_test_scene.py` for testing and previewing ASCII art in the main rectangle.
- Improved modularity and consistency across all scenes.
- Updated `main.py` to integrate all new scenes and start music at launch.

## Game Structure Implemented (25/08/2025)

- Created `main.py` as the entry point with the main game loop and screen transitions.
- Set up `screens/` directory with modular screen classes:
	- `base_screen.py`: Base class for consistent UI, screen clearing, and centering.
	- `title_screen.py`: Title/logo and start prompt.
	- `intro_screen.py`: Introductory story screen.
	- `game_scene.py`: Template for main scenes/chapters.
	- `end_screen.py`: Ending/credits screen.
- All screens use a shared frame and UI style for consistency.
- The game now transitions: Title → Intro → Main Scene → End.
  
## Initial Setup (25/08/2025)

- Project folder and git repository created and linked to GitHub.
- Main story for the game written in `texts/story(kids).md`, designed to be suitable and magical for children.
- Initial game design and structure outlined in `texts/actionplan.md`:
	- Game will be a Python CLI adventure with ASCII art and simple RPG mechanics (dice rolls, skill checks, dialogue choices).
	- Key stats: Wit, Perception, Spirit.
	- Story and scenes broken down into chapters for easy development.


---