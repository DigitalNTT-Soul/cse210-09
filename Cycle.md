# Cycle

Cycle; noun

/ˈsī-kəl/

an interval of time during which a sequence of a recurring succession of events or phenomena is completed

"Cycle is a game about using your trail to defeat the other player in the arena."

---

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Getting Started

---

Make sure you have Python 3.10.4 or newer installed and running on your machine. Open terminal or PowerShell and
browse to the project's root folder. Start the program by running the following command.

```
pip install raylib
```

```
python3 Cycle
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hilo folder and click the "run" button.

- Players can move up, down, left and right...
  - Player one moves using the W, S, A and D keys.
  - Player two moves using the I, K, J and L keys.
- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail...
  A "game over" message is displayed in the middle of the screen.
- The cycles turn white.
- Players keep moving and turning but don't run into each other.

## Project Structure

---

```
root                          (project root folder)
+-- Cycle                     (source code for game)
  +-- game                    (specific classes)
    +-- directing
      +-- director.py         (Director class)
    +-- casting
      +-- cast.py             (Cast class)
      +-- actor.py            (Actor class)
      +-- debris.py           (Debris class)
    +-- services
      +-- keyboard_service.py (Keyboard services class)
      +-- video_service.py    (video_service class)
    +-- shared
      +-- point.py            (Point class)
      +-- color.py            (Color class)
  +-- __main__.py             (program entry point)
  +-- config.py               (config class used to store config data for various game files to access)
+-- README.md                 (general info)
```

## Required Technologies

---

Python 3.10.4

## Authors

---

- ## Dylan Ruppell (ruppelld@byui.edu) (github: DigitalNTT-Soul):
  -
  - advised on other code
- ## Austin Donovan (iskarr9g@gmail.com) (github: Iskarr):
  -
  - advised on other code
- Matt Pellét (mattpellet@byui.edu) (github: m4j0rCSE):
  - Jump command
  - advised on other code
- ## Larry Brys (bry21010@byui.edu) (github: ljbrys):
  - advised on other code
- ## Ryan Manthey (ryanscom@byui.edu) (github: ryanscom):
  - advised on other code
