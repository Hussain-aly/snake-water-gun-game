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

My Role
This game was developed independently as a solo project.
