# dev-toolkit-83

`dev-toolkit-83` is a high-performance, asynchronous autoclicker built with Python to automate repetitive mouse tasks with precision. Designed for efficiency, it offers low-latency execution and customizable trigger patterns for various desktop environments.

## Features

*   **Jitter-Click Emulation:** Supports randomized intervals between clicks to mimic human behavior and evade basic anti-cheat heuristics.
*   **Dynamic Hotkey Control:** Bind custom keyboard triggers to start or stop the click loop without interrupting your workflow.
*   **Asynchronous Engine:** Utilizes the `pynput` library for non-blocking execution, ensuring system stability while the background process runs.
*   **Coordinate Locking:** Optional feature to lock clicks to a specific (X, Y) pixel location or follow the current cursor position.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install -r requirements.txt
```

## Usage

To launch the autoclicker with default settings, run the primary module from your terminal:

```bash
python main.py --interval 0.1 --button left
```

### Basic Example
Once the script is running, press your assigned trigger key (default: `F6`) to toggle the clicking action. You can modify the click frequency in `config.json` to adjust the delay (in seconds) between each registered press.

*Note: Please ensure you have the necessary accessibility permissions enabled for your terminal or IDE to allow simulated mouse input.*

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.