# Weans Game Jam 2025 - Progress Tracker

## Initial Setup (August 2025)

- Project folder and git repository created and linked to GitHub.
- Main story for the game written in `texts/story(kids).md`, designed to be suitable and magical for children.
- Initial game design and structure outlined in `texts/actionplan.md`:
	- Game will be a Python CLI adventure with ASCII art and simple RPG mechanics (dice rolls, skill checks, dialogue choices).
	- Key stats: Wit, Perception, Spirit.
	- Story and scenes broken down into chapters for easy development.
- Copilot instructions and project guidelines created in `.github/copilot-instructions.md` and `.github/pre_copilot.md` to ensure all code and content is child-appropriate and easy to extend.

---

## Utility Module Refactor (26/08/2025)

- Created `screens/utils.py` to hold shared utility functions and classes.
- Moved `load_art` (for loading ASCII art) and `ArrowMenu` (for menu navigation) into `utils.py` for easy reuse across all screens.
- Updated `screens/char_choice_scene.py` to import these utilities from `utils.py`.

All major planning documents are in place. Next steps: begin coding the CLI framework and first scene.

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