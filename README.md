# dev-toolkit-83

`dev-toolkit-83` is a high-performance, asynchronous autoclicker built in Python for precision-heavy automation tasks. It leverages low-level system hooks to provide rapid-fire input emulation with minimal latency and high reliability.

## Features

*   **Jitter-Enabled Automation:** Optional randomized interval delays to emulate human behavior and avoid detection in restrictive environments.
*   **Dynamic Hotkey Control:** Bind specific start/stop toggles to any key on your peripheral, allowing for seamless integration into your existing workflow.
*   **Hardware-Level Simulation:** Utilizes `pynput` to interact directly with the OS input stack, ensuring compatibility across standard GUI applications.
*   **Headless Execution:** Designed for efficient background operations with low CPU overhead, making it ideal for continuous long-running tasks.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed, then clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install -r requirements.txt
```

## Usage

To start the autoclicker with default configurations (10ms interval, left-click), run the following command:

```bash
python main.py --interval 0.01 --button left
```

You can view all available configuration flags and parameter tuning options by executing the help command:

```bash
python main.py --help
```

*Note: Administrative or Root privileges may be required on Windows and Linux distributions respectively to capture system-wide global hotkeys.*

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.