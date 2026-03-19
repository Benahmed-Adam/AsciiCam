# AsciiCam

**AsciiCam** is an ASCII Art rendering engine that transforms a video stream (webcam or video file) into a character matrix directly within your terminal. It supports color rendering and synchronized audio playback.

## Features

* **Real-time Capture:** Live streaming via webcam.
* **Video Playback:** Local file playback with synchronized audio restoration.
* **Dynamic Conversion:** Converts pixels to ASCII characters in grayscale or full color.
* **Rendering Optimization:** Utilizes differential refreshing (only modified zones are updated) for better performance.
* **Frame Rate Control:** Limits FPS to match the original source file.

## Dependencies

Before running the script, install the required libraries:

```bash
pip install pillow opencv-python numpy pygame moviepy
```

## Project Structure

* **`ascii_renderer`**: The core class managing video acquisition, ASCII conversion, and terminal output.
* **Modes**:
    * `cam`: Live capture via the system webcam.
    * `vid`: Video file playback with automated audio track extraction and playback.

## Usage

### 1. Webcam Mode

```python
from asciiRenderer import ascii_renderer

renderer = ascii_renderer("cam", couleur=True, opti=True)
renderer.run()
```

### 2. Video Mode

```python
from asciiRenderer import ascii_renderer

renderer = ascii_renderer("vid", couleur=False, opti=True)
renderer.run()
```

When using `vid` mode, the program will prompt you for the video file path (e.g., `video.mp4`).

## Parameters

* **`mode`**: `"cam"` or `"vid"`.
* **`couleur`** (bool):
    * `False` → Grayscale ASCII rendering.
    * `True` → Full-color ASCII rendering.
* **`opti`** (bool): Enables differential refreshing for performance.

Example:
```python
renderer = ascii_renderer("vid", couleur=True, opti=True)
```

## Notes

* **Terminal Size:** Rendering resolution depends on your current terminal dimensions (`os.get_terminal_size`).
* **Performance:** For the best visual results, zoom out of your terminal to increase the character "pixel" density.
* **Stability:** Avoid resizing the terminal window during rendering, as this may cause the program to crash.
* **Variability:** Output quality varies based on chosen resolution and terminal font size.
