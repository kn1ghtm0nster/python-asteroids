# Python Asteroids

This is a Python implementation of the classic arcade game **Asteroids**, developed as part of the [Boot.dev](https://www.boot.dev) curriculum. The game is built using the [Pygame](https://www.pygame.org/) library and features player-controlled shooting, asteroid splitting, and collision detection.

## Features

- Player-controlled spaceship with rotation and movement.
- Shooting mechanics with cooldown timers.
- Asteroids that split into smaller pieces when hit by bullets.
- Collision detection between the player, bullets, and asteroids.

## Requirements

- Python 3.8 or higher
- Pygame library

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-asteroids.git
cd python-asteroids
```

### 2. Create a Virtual Environment

**NOTE :** It's highly recommended to use a `virtual environment` to manage the dependencies

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Run the Game

Start the game by running the `main.py` file:

```bash
python main.py
```

### Controls

- **W**: Move forward
- **S**: Move backward
- **A/D**: Rotate the spaceship
- **SPacebar**: Shoot bullets

### Notes for Windows Users

- Ensure that Python is added to your system's `PATH` installation.
- Use `python` instead of `python3` for commands (unless you use WSL)

### Notes for macOS Users

- Use `python3` for commands, as macOS typically reserves `python` for Python 2.x.
- If you encounter issues with `Pygame` installation, ensure that `SDL` dependencies are installed. You can use [Homebrew](https://brew.sh/):

```bash
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
```

### Contributing

Feel free to fork this repository and submit pull requests for new features or bug fixes.
