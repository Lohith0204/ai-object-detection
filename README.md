# AI Object Detection System (YOLO-Based)

## Overview
AI Object Detection System is a Python-based computer vision application that detects and identifies multiple objects present in an image using a pre-trained YOLO (You Only Look Once) model.

The system allows users to upload an image, performs real-time object detection, draws bounding boxes with labels, and displays the final output through an interactive Streamlit interface.

This project focuses on building a modular, easy-to-understand, and beginner-friendly object detection pipeline without training a custom deep learning model from scratch.

## Features
- Upload images for object detection
- Real-time object detection using YOLO
- Bounding box visualization with class labels
- Confidence-based detections
- Clean and interactive Streamlit UI
- Modular and extensible project structure
- Beginner-friendly implementation

## Tech Stack
- Python
- Streamlit
- OpenCV
- NumPy
- YOLO (pre-trained model)

## Project Structure

```text
AI OBJECT DETECTION SYSTEM/
│
├── app.py                   # Streamlit application entry point
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── .gitignore               # Ignore files
│
├── core/
│   ├── detector.py          # YOLO object detection logic
│   └── visualization.py    # Bounding box drawing utilities
│
├── assets/
│   └── sample_image.jpg     # Sample input image
│
└── screenshots/             # Application screenshots
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-29 203115.png>)

### Image Upload
![Image Upload](<screenshots/Screenshot 2025-12-29 203337.png>)

### Try-On Image Output
![Object Detection Output](<screenshots/Screenshot 2025-12-29 203430.png>)

## How It Works
1. The user uploads an image using the Streamlit interface.
2. The image is converted into a NumPy array and decoded using OpenCV.
3. A pre-trained YOLO model processes the image to detect objects.
4. Detected objects include bounding box coordinates, class labels, and confidence scores.
5. Bounding boxes and labels are drawn on the image.
6. The final detected image is displayed instantly in the UI.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application can be used to detect objects present in an image automatically.
Users upload an image, and the system identifies multiple objects along with their locations and labels.

It is useful for:
- Computer vision demonstrations
- AI portfolio projects
- Learning object detection concepts
- Image analysis applications

## Future Improvements
- Support for live webcam detection
- Option to upload video files
- Model selection (YOLOv5, YOLOv8, etc.)
- Adjustable confidence threshold
- Improved UI styling and controls

## Learning Outcomes
This project helped me understand how real-world object detection systems work using deep learning models.
I learned how to preprocess images, integrate pre-trained YOLO models, visualize detection results, and structure an end-to-end computer vision application using Streamlit.The project strengthened my understanding of OpenCV pipelines, modular Python design, and deploying AI-powered applications.
