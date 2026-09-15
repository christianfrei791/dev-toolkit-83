# dev-toolkit-83

`dev-toolkit-83` is a high-performance Python-based autoclicker designed for precision, speed, and low CPU overhead. It provides a lightweight solution for automating repetitive mouse tasks with customizable intervals and hotkey controls.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

*   **Low-Latency Execution:** Built using `pynput` for near-instantaneous event simulation.
*   **Dynamic Intervals:** Support for custom millisecond delays between clicks to mimic human behavior.
*   **Hotkey Integration:** Global listener setup to start or stop the automation sequence at any time without window focus.
*   **Multi-Button Support:** Ability to toggle between left, middle, and right mouse button automation.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install -r requirements.txt
```

## Usage

You can launch the clicker directly via the terminal. By default, the script is configured to trigger on the F6 key and stop on F7.

```bash
# Basic execution with default settings
python main.py --interval 0.5 --button left

# Execution with custom hotkeys
python main.py --start-key f9 --stop-key f10
```

### Configuration
Adjust the `config.json` file in the root directory to permanently save your preferred click patterns, coordinate locking, and delay randomization settings.

## Safety & Disclaimer
*This tool is intended for educational purposes and productivity automation. Please ensure you are in compliance with the Terms of Service of any application where you utilize this tool.*