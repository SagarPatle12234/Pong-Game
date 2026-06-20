# Pong Simulation Environment

A Python-based Pong simulation featuring a custom environment and rule-based heuristic bots, serving as a foundational testing ground for future neural network training.

## Overview
This repository contains a custom Pong environment (`PongEnv`) and a visual simulation script (`main.py`) where two bots play against each other[cite: 1, 2]. Currently, the game utilizes a rule-based `heuristic_agent` that automatically tracks and intercepts the ball by calculating its paddle's center relative to the ball's vertical position[cite: 1, 2]. 

The main game loop continuously extracts these coordinates, renders the gameplay frame-by-frame in `"human"` mode, and resets automatically after a point is scored[cite: 1, 2]. This setup provides a fully functioning baseline environment designed to be easily adapted for training Reinforcement Learning (RL) neural networks in the future[cite: 1, 2].

## Key Features
* **Custom Environment:** Utilizes a custom `PongEnv` for rendering and stepping through the game state[cite: 1, 2].
* **Heuristic Agents:** Includes a baseline, rule-based bot that uses simple math to align its paddle (`paddle_y`) with the ball (`ball_y`)[cite: 1, 2].
* **Continuous Game Loop:** Automatically extracts coordinate observations (`obs`), updates the frame (`env.render()`), and resets the match when a goal is scored (`done`)[cite: 1, 2].
* **AI-Ready Architecture:** The codebase is structured so the heuristic agents and `"human"` render mode can be swapped out easily for training a neural network[cite: 1, 2].

## Usage

1. Clone the repository.
2. Ensure you have the necessary dependencies installed (e.g., the library your `PongEnv` utilizes).
3. Run the simulation[cite: 1, 2]:
```bash
   python main.py
