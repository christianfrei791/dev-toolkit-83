# dev-toolkit-83

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

`dev-toolkit-83` is a lightweight, high-precision Python autoclicker designed for automated GUI testing, workflow simulation, and repetitive cursor tasks. Built with multi-threading support, it delivers customizable click intervals and global hotkey controls without causing desktop input lag.

## Features

* **Precision Timing Engine:** Configurable sub-millisecond delay options for high-frequency or exact-interval click loops.
* **Global Hotkey Listeners:** Toggle execution or instantly abort scripts system-wide using custom key combinations (`F8` by default).
* **Multi-Target Sequencing:** Define and cycle through specific screen coordinates across multiple display setups.
* **Randomized Human Micro-Delays:** Optional Gaussian jitter distribution to simulate natural human clicking behavior during automated test suites.

## Installation

Ensure you have Python 3.8+ installed, then clone the repository and install dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install pynput pyautogui
pip install -e .
```

## Quick Start

Run `dev-toolkit-83` directly from your terminal or import it as a module in your Python scripts.

### Command Line Interface

```bash
python -m dev_toolkit_83 --interval 0.05 --button left --hotkey f8
```

### Python API Example

```python
from dev_toolkit_83 import AutoClicker, MouseButton

# Initialize clicker with a 50ms interval on the left mouse button
clicker = AutoClicker(interval=0.05, button=MouseButton.LEFT)

# Bind toggle switch to F8 key
clicker.bind_hotkey("f8")

# Start listening for inputs in a non-blocking thread
clicker.listen()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.