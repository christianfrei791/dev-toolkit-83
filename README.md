# dev-toolkit-83

`dev-toolkit-83` is a high-performance, Python-based autoclicker designed for task automation and precision testing. It utilizes low-level input libraries to ensure minimal latency and reliable execution across desktop environments.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## Features

*   **Configurable CPS:** Fine-tune your clicks per second with millisecond-level accuracy.
*   **Smart Hotkeys:** Start, pause, and stop automation instantly using customizable keyboard triggers.
*   **Dynamic Targeting:** Supports both fixed-coordinate clicking and follow-cursor modes.
*   **Low Resource Footprint:** Optimized core logic ensures zero interference with background system processes.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install -r requirements.txt
```

## Usage

To launch the autoclicker with default settings, execute the main script from your terminal:

```bash
python main.py --cps 10 --hotkey F8
```

### Basic Example
Once running, the application will enter a standby state. Press the assigned **hotkey** to toggle clicking mode. Use `Ctrl+C` in the terminal to safely terminate the process and release system input control.

## Disclaimer
This tool is intended for personal automation and testing purposes only. Please ensure you comply with the Terms of Service of any third-party software before utilizing automated input tools.

## License
Distributed under the MIT License. See `LICENSE` for more information.