# CV Practice - OpenCV Image Processing

This project demonstrates basic image processing techniques using OpenCV in Python. It provides hands-on practice with fundamental computer vision operations including:

## Features

- **Image Loading & Display**: Load an image from file and display it using OpenCV's GUI window
- **Image Cropping & Resizing** (commented out): Crop regions of interest and resize images by specific pixel dimensions or scale percentages
- **Image Filtering** (commented out): Apply Sobel edge detection (X/Y gradients) and color space conversion (BGR to HSV, BGR to Grayscale)
- **Image Rotation** (commented out): Rotate images around their center point using affine transformation
- **Image Flipping** (commented out): Flip images horizontally or vertically
- **Gaussian Blur**: Apply Gaussian blur with configurable kernel size for image smoothing

## Requirements

- Python 3.x
- OpenCV library (`opencv-python`)

## Installation

Install the required dependency:

```bash
pip install opencv-python
```

## Usage

Place a test image named `test.png` in the same directory as the script, then run:

```bash
python CV_Practice.py
```

The script will:
1. Load `test.png` from the current directory
2. Display the original image
3. Apply Gaussian blur and display the result
4. Wait for a key press to close all windows

## File Structure

- `CV_Practice.py` — Main Python script with OpenCV image processing examples
- `test.png` — Sample input image for processing
- `README.md` — Project documentation

## Notes

- Most advanced operations (cropping, resizing, Sobel, HSV/Gray conversion, rotation, flipping) are currently commented out in the source code. Uncomment the relevant sections to experiment with them.
- The Gaussian blur kernel size `(9, 9)` must be an odd number and can be adjusted for different blurring effects.