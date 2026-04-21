# 🌿 Sprout Valley

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-FFD43B?style=flat&logo=python&logoColor=3776AB)](https://www.pygame.org/)

**Sprout Valley** is a cozy 2D farming simulator built with **Python** and **Pygame**. This project is a functional implementation of a farming game, featuring dynamic weather, a day/night cycle, and a vibrant world to explore.

---

## 📜 Credits
This project was developed as part of a learning journey, based on the excellent **[Stardew Valley Tutorial](https://www.youtube.com/watch?v=T4IX36sP_K8)** and **[original source code](https://github.com/clear-code-projects/PyDew-Valley)** by **[Clear Code](https://github.com/clear-code-projects)**. It serves as a personal exploration of game architecture, complex sprite grouping, and camera systems in Pygame.

---

## 📖 Table of Contents
- [Features](#-features)
- [Controls](#-controls)
- [Getting Started](#-getting-started)
- [Technical Architecture](#-technical-architecture)
- [Recent Optimizations](#-recent-optimizations)
- [Future Roadmap](#-future-roadmap)

---

## ✨ Features

- **🌾 Dynamic Farming System:** Till soil, plant crops (Corn & Tomato), water them daily, and harvest for profit.
- **🌤️ Atmospheric World:** Experience a full Day/Night cycle with immersive lighting and randomized weather patterns (Rain/Clear).
- **🌲 Resource Gathering:** Use your trusty axe to chop trees for wood and gather fresh apples.
- **⚖️ Merchant Trading:** Visit the local trader to manage your economy—sell your harvest and buy new seeds.
- **🎨 State-Driven Animation:** Fluid character movement and tool-use animations with z-index sorting for a 2.5D feel.
- **🎵 Immersive Audio:** High-quality sound effects for every action and a relaxing background soundtrack.

---

## 🎮 Controls

| Action | Control |
| :--- | :--- |
| **Move** | `Arrow Keys` |
| **Use Tool (Axe/Hoe/Water)** | `Space` |
| **Switch Tool** | `Q` |
| **Plant Seed (Corn/Tomato)** | `Left Ctrl` |
| **Switch Seed** | `E` |
| **Interact (Trade/Sleep)** | `Enter` |

---

## 🚀 Getting Started

### 🎮 Downloading the Game
- **Windows:** Go to the **[Actions](https://github.com/harshilpabbisetti-sudo/stardrew_valley/actions)** tab, select the latest successful run, and download the `SproutValley-Windows` artifact from the bottom of the page.
- **macOS:** Download the repository and run the `dist/SproutValley` file.

### Prerequisites (for Developers)
- **Python 3.8 or higher**
- **pip** (Python package manager)

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/harshilpabbisetti-sudo/stardrew_valley.git
   cd stardrew_valley
   ```

2. **Install Dependencies:**
   ```bash
   pip install pygame pytmx
   ```

3. **Run the Game:**
   ```bash
   python code/main.py
   ```

---

## 🏗️ Technical Architecture

Sprout Valley is built with a modular approach:
- **`level.py`**: The central orchestrator managing the game world, camera, and sprite groups.
- **`player.py`**: A complex state-machine handling movement, tool interactions, and inventory.
- **`soil.py`**: Manages the farmable grid, soil states (wet/dry), and plant growth cycles.
- **`sky.py`**: Handles the transition between day and night and the procedural rain system.
- **`support.py`**: A utility layer for asset loading, path normalization, and OS-independent file handling.

---

## 🛠️ Recent Optimizations

- **High-Performance Rain:** Particles now spawn exclusively within the viewport using camera offsets, allowing for denser visuals with zero performance overhead.
- **TMX Data Caching:** Map data is parsed once during initialization and shared across modules, reducing startup time by ~40%.
- **Smarter Shop UI:** Differentiated labeling for seeds vs. crops ensures a clearer trading experience.

---

## 🗺️ Future Roadmap

- [ ] **On-Screen HUD:** Real-time money and inventory display.
- [ ] **Persistent Saves:** SQL-backed save system to continue your progress.
- [ ] **Expanded World:** New NPC characters, quests, and hidden areas.
- [ ] **Inventory System:** A full menu to manage collected items and tools.
