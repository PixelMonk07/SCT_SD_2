# SCT_SD_2

Skillcraft Technology Internship 2nd project - number guessing game

# Number Guessing Game

Welcome to the **Number Guessing Game**! This is a simple Python-based project where the user is asked to guess a randomly generated number between 1 and 100. The program provides feedback on whether the guessed number is higher or lower than the target until the correct number is guessed.

## How It Works

1. **Random Number Generation**: The game generates a random number between 1 and 100.
2. **User Input**: The player is prompted to input their guess.
3. **Feedback Loop**: The game tells the player if their guess is too high, too low, or correct.
4. **Victory**: Once the correct number is guessed, the game congratulates the player and ends.

## Features

- **Input Validation**: The game ensures that the user's input is a valid integer and between the valid range of 1 to 100.
- **Continuous Feedback**: The player receives real-time feedback on their guess, helping them adjust for the next attempt.
- **Error Handling**: If a non-integer value is entered, the game prompts the user to enter a valid number without crashing.

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Run the Python script using the following command:

   ```bash
   python number_guessing_game.py
   ```

4. Follow the on-screen instructions to start playing.

## Sample Output

```bash
Welcome to the number guessing game!
Enter a number between 1-100: 50
Higher number please!
Enter a number between 1-100: 75
Lower number please!
Enter a number between 1-100: 63
Congrats! You guessed the correct number!
```
