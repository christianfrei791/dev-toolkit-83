# dev-toolkit-83

`dev-toolkit-83` is a high-performance, Python-based automation utility designed for rapid execution of repetitive mouse events. It provides developers and power users with a lightweight, low-latency framework for custom click automation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Features

*   **Precision Timing:** Utilizes sub-millisecond thread scheduling for consistent Click-Per-Second (CPS) rates.
*   **Dynamic Input Mapping:** Supports multi-button binding and variable delay intervals between clicks.
*   **Coordinate Locking:** Allows for static target clicking or dynamic follow-the-cursor modes.
*   **Resource Optimized:** Built with low-overhead library dependencies to minimize CPU impact during background operation.

### Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install -r requirements.txt
```

### Usage

To start the autoclicker with a default configuration (10 clicks per second), execute the following command in your terminal:

```bash
python main.py --cps 10
```

For advanced usage, you can define a custom target coordinate and toggle key:

```bash
# Set specific location (x, y) and activate with 'f6'
python main.py --x 500 --y 500 --key f6 --cps 25
```

Press `Ctrl+C` in the terminal to terminate the process safely.

### Disclaimer
This tool is intended for personal automation and testing purposes only. Ensure compliance with the Terms of Service of any application where this tool is deployed.