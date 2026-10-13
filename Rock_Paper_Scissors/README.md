<h1 align="center"> Rock Paper Scissors 🪨📄✂️</h1>

<p align="center">
  <img src="data/LOGO.jpeg" alt="Rock Paper Scissors LOGO" width="480">
</p>

<p align="center">
    A console version of the classic Rock, Paper, Scissors game, written in Python. You play against the computer, and the program keeps track of your score.
</p>

## Features

- Play against a computer that chooses randomly
- Input validation: invalid choices are rejected and you are asked again
- Score tracking: each win adds one point to your score
- Replay loop: play as many rounds as you like

## Project structure
Rock_Paper_Scissors/ 
├── data/  
│   ├── LOGO_game.jpeg
│   ├── image.jpeg   
├── src/  
│ └── game.py  
├── LICENSE  
└── README.md  


## Requirements

- Python 3.13.2 or newer
- No third-party packages. Only the Python standard library is used.

## How to run

From the project root:

```bash
cd src
python game.py
```

## Rules

| Your choice | Beats | Loses to |
|-------------|-------|----------|
| Rock | Scissors | Paper |
| Paper | Rock | Scissors |
| Scissors | Paper | Rock |

If both choices are the same, the round is a tie and no point is added.

!['Rock'](data/images.jpeg)

## Code structure

- **`RockPaperScissors`**: runs the game. It gets the player's choice, gets the computer's choice, decides the winner, and updates the score.
- **`Player`**: stores the player's name and score.
- **`main()`**: handles the start of the game and the menu.

## Concepts used

- Classes and objects
- Recursion
- Type hints and docstrings

## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.