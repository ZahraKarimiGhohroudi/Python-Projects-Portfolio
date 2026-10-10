
# Number Guesser

A simple number guessing game written in Python. Players sign up with a username and password, choose a difficulty level, and try to guess a secret number. Each finished game is saved, and players can review their recent results.

![NumberGuesser game](data/LOGO_game.jpeg)



## Features

- Sign up and log in with a username and password
- Passwords are stored as salted PBKDF2-SHA256 hashes, never in plain text
- Three difficulty levels:
  - **Easy:** a number from 1 to 1000
  - **Medium:** a number from 1000 to 10000
  - **Hard:** a number from 1 to 100000
- Score for each game: `(5000 × level) − (guesses × 100)`
- Game history for each player

## Project structure

Number_Guesser/  
├── data/  
│   ├── LOGO_game.jpeg  
│   ├── players_info.txt  
│   └── results.txt  
├── src/   
│   ├── main.py  
│   ├── new_game.py  
│   ├── players.py  
│   └── results.py  
├── .gitignore  
├── LICENSE  
├── README.md  
└── requirements.txt  


## Requirements

- Python 3.10 or newer 
- No third-party packages are needed. The project uses only the standard library.

## How to run

From the project root:

```bash
cd Number_Gueseer/src
python main.py
```

## Username and password rules

- **Username:** 3 to 20 characters, letters, digits, and underscores only. Usernames must be unique.
- **Password:** at least 8 characters, with at least one letter and one digit.

## Notes

> `players_info.txt` and `results.txt` are created automatically when you sign up or finish a game.


## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.

