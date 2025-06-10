# Web AR Butterfly Experience

A marker-based Web AR application that displays a 3D butterfly model when scanning a specific marker.

## Setup Instructions

1. Make sure you have Python installed on your computer
2. Place your marker image as `marker.jpg` in the `src/assets/markers/` folder
3. Place your 3D model as `butterfly_blendeer.glb` in the `src/assets/models/` folder
4. Run the server:
   ```
   python server.py
   ```
5. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Click the "Start AR" button to begin
2. Allow camera access when prompted
3. Point your camera at the marker
4. The 3D butterfly model should appear on top of the marker

## Requirements

- A modern web browser (Chrome, Firefox, Safari)
- Camera access
- The marker image
- The 3D model file

## Notes

- Make sure you're in a well-lit environment for better marker detection
- Keep the marker steady and in view of the camera
- The marker should be printed and placed on a flat surface 