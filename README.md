# Face Detection using Viola–Jones Algorithm (OpenCV)

This project implements real-time face detection using the Viola–Jones algorithm with Haar Cascade classifiers in OpenCV. It captures live video from a webcam, processes each frame in grayscale, and detects human faces by scanning Haar-like features. Detected faces are highlighted with bounding boxes in real time.

The project focuses on classical computer vision techniques and serves as an introductory implementation of object detection without deep learning. Haar cascades are computationally efficient but sensitive to lighting conditions, face orientation, and occlusions, making this project useful for understanding both their strengths and limitations.

## Features
- Real-time face detection using webcam input  
- Viola–Jones algorithm with Haar Cascade classifiers  
- Fast execution on CPU-only systems  
- Simple and beginner-friendly OpenCV implementation  

## Tech Stack
- Python  
- OpenCV  
- Haar Cascade Classifier  

## Use Cases
- Academic and learning projects  
- Introductory computer vision demonstrations  
- Low-resource or CPU-only environments  

## Limitations
- Performance drops under poor lighting conditions  
- Less accurate for rotated or partially occluded faces  
- Not as robust as modern deep learning–based detectors  

## How It Works
1. Captures video frames from the webcam  
2. Converts each frame to grayscale  
3. Applies Haar Cascade classifier to detect faces  
4. Draws bounding boxes around detected faces  

## Future Improvements
- Replace Haar cascades with DNN-based face detection  
- Improve robustness under varying lighting conditions  
- Add face tracking for smoother detection  

