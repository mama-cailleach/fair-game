Game Structure and Challenges
We can structure the game as a series of distinct scenes or "chapters." Each chapter will have a specific goal, with the core gameplay revolving around dialogue, simple exploration, and skill checks.
•	Skill Checks: Instead of a complex system, let's use a very simple one. The player can have a few stats (e.g., Wit, Perception, or Spirit). When a check is needed, the game asks the player to type a command like roll D20. A number is randomly generated, and if it's high enough, they succeed. This is a great way to add TTRPG flavor without complex combat.
Here's a breakdown of the story into manageable game scenes and challenges:
________________________________________
Scene 1: The Wanderer's Arrival & Whispered Conspiracy
•	Goal: Introduce the player character, the setting (Bo'ness and the Queen's Arch), and the central conflict.
•	Gameplay: This will be a mostly narrative-driven scene. The player reads the text about arriving from Glasgow and settling in the Queen's Arch. The core interaction is a skill check: a Perception roll.
•	Challenge: The game prompts the player to roll Perception. If the roll succeeds, the player overhears the full conversation about the imposter Queen, the old foundry, and the Crimson Fleet. If the roll fails, they only hear muffled whispers, but the word "imposter" is enough to hint at the conspiracy. The outcome doesn't change the story, but it makes the player feel like their choice mattered.

Day 1 Task: Build the basic text-based framework. Can the game display the opening text? Can it prompt the player for a "roll"? Can it display a success/fail message based on the result? This is the foundation for everything else.

Scene 2: The Imposter's Entrance & Seeking Help
•	Goal: The player witnesses the imposter Queen and begins to gather information.
•	Gameplay: This is a simple hub-and-spoke dialogue system. The player can choose to talk to a few different characters from a menu.
o	Characters: The Flower Girls and the Witches of Bo'ness.
•	Dialogue Checks: When talking to the Flower Girls, a Wit roll can be used to get them to reveal their gossip about the Queen's "sharp tone".
•	The Witches: This is a guaranteed path. The player's identity as a witch is revealed, and they receive the map to the Witches' Stone. No roll needed here, as it's a key plot point.
•	
Day 2 Task: Implement the dialogue system. Create the menu for the player to choose who to talk to. Write the dialogue for the Flower Girls and the Witches. Add the Wit roll logic. Make sure the game can transition from this scene to the next.

Scene 3: The Haunted House & The Witches' Stone
•	Goal: Find and rescue the real Queen. This is the main puzzle/action sequence.
•	Gameplay: This scene is about overcoming two linked challenges.
o	Challenge 1: The Ghostly Knight. The player arrives at Carriden House and finds the locked door guarded by a spectral knight. Instead of combat, the challenge is a multi-step Spirit check.
o	Step 1: The player must successfully roll Spirit to perceive the invisible knight.
o	Step 2: A second roll Spirit is needed to defeat the knight and claim its blade.
o	
o	Challenge 2: The Locked Door. The player uses the blade to unlock the door. This is an automatic success after the knight is defeated.
o	Outcome: The real Queen is found and rescued, and they discover the flying brooms.
Day 3 Task: Write the text for the Carriden House scene. Implement the Spirit skill checks. If the player fails, the game can simply say something like, "The knight's spectral form sends you sprawling. You need a moment to collect yourself." and then prompt them to try again, with some flavor text about the witches' wisdom helping them. This way, the player can't get permanently stuck.


Scene 4: The Final Confrontation
•	Goal: Return to the town and defeat the Champion and the imposter Queen.
•	Gameplay: This is the big finale. It should be quick and cinematic.
o	The Challenge: When the Champion bellows his challenge, the player responds. The game can present this as a choice: "Challenge him yourself" or "Have the Queen step forward". The player's choice determines who fights the Champion, but the outcome is always the same: they are defeated. This gives the player agency without requiring a complex combat system.
•	Final Actions: The Bo'ness witches appear, reveal the imposter's true identity as the Princess of Linlithgow, and the villains flee.

Day 4 Task: Write the finale text. Implement the choice and the resulting narrative. Add sound effects (the bagpipes, a triumph song) to give this a grand, satisfying feel.


Scene 5: The Happy Ending
•	Goal: The Queen is crowned, and the player is celebrated.
•	Gameplay: This is a final, celebratory narrative scene.
o	Content: A description of the true Queen being crowned, the renewed celebration of Fair Day, and a final line about the player no longer being an outsider.
o	
Day 5 Task: Write the ending and polish everything. Check for typos, clean up the code, and ensure the game is ready for submission.


