# swg-game

# Snake-Water-Gun Game

A simple Python implementation of the classic Snake-Water-Gun game.

## Game Rules
- Snake (1) beats Water (2)
- Water (2) beats Gun (3)
- Gun (3) beats Snake (1)

## Features
- Input validation to ensure only valid choices (1, 2, or 3) are accepted
- Error handling for non-integer inputs
- Multiple rounds with score tracking
- Option to continue or quit after each round
- Final score display with winner announcement

## How to Run
1. Ensure you have Python installed
2. Run the script: `python snake_water_gun.py`
3. Follow the on-screen instructions

## Game Flow
1. You'll be prompted to choose Snake (1), Water (2), or Gun (3)
2. The computer will make a random choice
3. The winner of each round is determined based on the game rules
4. Scores are tracked across rounds
5. After each round, you can choose to continue or quit
6. When quitting, the final scores and winner are displayed