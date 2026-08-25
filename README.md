# dev-toolkit-83

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

dev-toolkit-83 is a Python autoclicker built for developers who need reliable mouse automation during UI testing and repetitive workflows. It offers precise timing control with minimal setup and supports both scripted and interactive use.

## Features
- Millisecond-precise click intervals with optional human-like jitter
- Configurable left, right, and middle mouse button support
- Global hotkeys for starting, pausing, and stopping without window focus
- Session logging with click count and duration tracking

## Installation

```bash
git clone https://github.com/Developer/dev-toolkit-83.git
cd dev-toolkit-83
pip install pynput
```

## Usage

Run from the command line:

```bash
python autoclicker.py --interval 0.1 --clicks 500 --button left
```

Use programmatically:

```python
from autoclicker import AutoClicker

clicker = AutoClicker(interval=0.05, button="left")
clicker.start()
```