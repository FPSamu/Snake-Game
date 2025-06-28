# 🐍 Snake Game with Pygame

A classic Snake game built using Python and Pygame. Control the snake, collect apples, and avoid colliding with yourself!

---

## 🎮 Controls

- ⬆️ Up Arrow: Move Up  
- ⬇️ Down Arrow: Move Down  
- ⬅️ Left Arrow: Move Left  
- ➡️ Right Arrow: Move Right  
- ⎋ ESC: Exit the game

---

## 🚀 Features

- Snake body represented as linked nodes following the head.
- Apples are generated randomly on the screen.
- The snake grows longer each time it eats an apple.
- Collision detection: the game ends if the snake hits itself.
- Border wrapping: when the snake exits one side, it reappears on the opposite.

---

## 🧱 Code Structure

- `Apple`: Represents an apple with x and y position.
- `Node`: Represents a part of the snake (either head or body).
- `update_position`: Updates node position to follow the parent.
- `move_*`: Handles movement logic.
- `check_eat`: Detects apple consumption.
- `check_colision`: Detects self-collision.
- `generate_apple`: Spawns apples in empty locations.

---

## 🔧 How to Run

1. Make sure Python 3 is installed.
2. Install `pygame` if not already:
   ```bash
   pip install pygame
3. Run the game
    ```bash
    python snake.py

## 📌 To Do / Ideas
- Score tracking and high score saving
- Game over screen and restart option
- Sound effects
- Difficulty levels

## 🧑‍💻 Author
Created by Samu