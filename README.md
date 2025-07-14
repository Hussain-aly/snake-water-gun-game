This is a classic text-based game implemented in Python, where a player competes against a computer opponent. It was developed as a foundational project to solidify core programming concepts and introduce basic game logic.

How to Play
Players choose one option: Snake, Water, or Gun. The computer then makes its own random selection, and the winner is determined based on the following rules:

Snake drinks Water (Snake wins)

Gun shoots Snake (Gun wins)

Water rusts Gun (Water wins)

If both the player and the computer choose the same option, the round is a draw.

The game continues in a loop until the player decides to exit.

Key Features
Interactive command-line interface for engaging gameplay.

Implements the classic rules of Snake, Water, Gun to determine win, loss, or draw conditions.

Utilizes random selection for the computer's move, ensuring varied gameplay.

Technologies Used
Python: The primary programming language used for the entire game logic.

random module: Essential for generating the computer's unpredictable choice.

if/elif/else statements: Crucial for implementing the game's decision-making logic and outcome determination.

while True loop: Ensures continuous gameplay, allowing multiple rounds until the user chooses to quit.

How to Run
Clone the repository:

git clone https://github.com/Hussain-aly/snake-water-gun-game.git

Navigate to the project directory:

cd snake-water-gun-game

Run the game:

python "snake, water, gun Game .py"

(Note: The filename snake, water, gun Game .py contains spaces and commas. It's generally recommended to rename files without spaces or special characters for easier command-line usage, e.g., snake_water_gun_game.py. If you rename it, update this instruction.)

Future Enhancements (Optional)
Add score tracking and display for multiple rounds.

Implement a graphical user interface (GUI) using libraries like Tkinter or Pygame.

Allow players to set the number of rounds to play.

Improve input validation for player choices.

My Role
This game was developed independently as a solo project.
