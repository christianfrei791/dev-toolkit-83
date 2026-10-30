[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# dev-toolkit-83

`dev-toolkit-83` is a lightweight, high-precision Python automation utility designed for rapid UI testing and input simulation. Built on non-blocking asynchronous threads, it delivers consistent high-frequency clicking without freezing application interfaces or causing input lag.

## Features

- **Sub-Millisecond Precision:** Utilizes high-resolution system performance counters to deliver accurate click intervals up to 200 CPS.
- **Global Hotkey Listeners:** Toggle automated actions instantly across operating system contexts using configurable hotkeys (default `F8`).
- **Humanized Input Simulation:** Optional micro-jitter algorithms introduce randomized variance to click timing and coordinates.
- **Coordinate Locking