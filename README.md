[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# dev-toolkit-83

`dev-toolkit-83` is a high-performance Python-based autoclicker designed for developers testing UI responsiveness and automating repetitive desktop workflows. Built with safety and speed in mind, it provides microsecond-precision clicking alongside instant global hotkeys to prevent runaway input loops.

## Features

* **Precision Interval Control:** Configure click delays down to 1 millisecond with optional randomized jitter to simulate human interaction.
* **Global Hotkey Listeners:** Instantly start, pause, or abort clicking loops using customizable system-wide keyboard shortcuts (Default: `F8` to toggle, `F12` to stop).
* **Targeted Execution:** Support for left, right, and middle mouse buttons bound to either fixed X/Y screen coordinates or the current cursor position.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install -r requirements.txt
```

*Note: This package requires Python 3.8+ and utilizes the `pynput` library for cross-platform input simulation.*

## Quick Start

You can run the autoclicker programmatically with the following script:

```python
from toolkit import SafeClicker

# Initialize clicker with a 0.05-