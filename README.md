# Mice Wheel

Mice Wheel is a simple Python script that simulates random mouse movements on your screen. It can be used to prevent your computer from going idle or to keep your screen active during long periods of inactivity.

## How to Run

1. **Install dependencies:**

	You need Python 3.10 or higher. Install [uv](https://github.com/astral-sh/uv) if you don't have it:

	```bash
	brew install uv
	```

	Then install the dependencies using:

	```bash
	uv sync
	```

2. **Run the script:**

	```bash
	uv run main.py
	```

## Dependencies

- Python >= 3.10
- pyautogui

## Notes
- The script will move your mouse cursor randomly across the screen at random intervals.
- To stop the script, press `Ctrl+C` in the terminal.
