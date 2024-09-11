# Face Recognition System - Detect and Recognize Faces from the Crowd

## Overview

This project is a face recognition system that uses YOLOv7 to detect and extract faces from a crowd, Facenet to extract features, and ArcMarginModel to recognize faces stored in the directory `./databases`. The system can be applied to photos, videos, and live-streams.

## Frameworks

- Pytorch
- OpenCV
- YOLOv7
- pytorch-lightning

## Algorithms

- Kalman Filter
- Watch Dog monitoring
- Optical Flow Tracker
- IOU Based Tracker
- Contractive Loss FR
- Single Shot Detector
- ESPCN Super Resolution

## Usage

1. Run the YOLOv7 model to detect and extract faces from the crowd.
2. Extract features from the faces using Facenet.
3. Use the extracted features and the ArcMarginModel to recognize the faces stored in the `./databases` directory.

## Results

The system was tested on a dataset of photos, videos, and live-streams and achieved an accuracy of X%.

## References
- YOLOv7: https://github.com/ultralytics/yolov7
- Facenet: https://github.com/davidsandberg/facenet

## Usage 
To run the main model, use the following command:

```
python run.py --source <source>
```

Where `<source>` can be either "live" for live-stream, a path to a video file or a path to an image file.

For example, if you want to run the model on a live-stream, use the following command:


# Summary of Changes

This document summarizes the changes made in the three Python files (`process.py`, `FaceRecognition.py`, and `FaceNet.py`).

## 1. `process.py`

### Modified Device Type Checks:
- Updated the code to ensure proper handling of device types (CPU/GPU). Specifically, replaced the line that incorrectly checked `self.device.type` with an explicit condition using `torch.device()`.

### Adjusted Model Loading:
- Added proper error handling around the `attempt_load()` function when loading the YOLOv7-tinyface model weights to avoid runtime errors during the model initialization process.

### Debugging and Error Messages:
- Added print statements to track the flow of execution and ensure that the model and camera were loading properly.

### Fixed Issues with the Video Stream:
- Addressed issues where OpenCV could not access the camera feed due to improper initialization of the stream. This was done by reworking the stream handling code.

---

## 2. `FaceRecognition.py`

### Fixed Model Initialization:
- Corrected an issue where `self.upsample` was being called outside the `__init__` method, causing `NameError`. Moved the `self.upsample` instantiation inside the constructor.

### Modified Input Handling:
- Added error handling in the `predict` method to ensure proper handling of image inputs, including resizing the images to the correct dimensions expected by the model.

### Error Messages and Debugging:
- Inserted debug print statements to show the image shape before and after the prediction. This helped identify where the model input/output shapes were causing issues.

### Fixed Tensor Shape Mismatches:
- Resolved issues in the prediction method related to the shape of the tensors passed to the fully connected layers by ensuring the proper flattening of the tensors before passing them into the model.

---

## 3. `FaceNet.py`

### Improved Model Architecture:
- Adjusted the fully connected layer dimensions in the `FaceNet` class to ensure compatibility with the input tensor sizes. Specifically, the input to the `fc` layer was updated to handle different image sizes by adding print statements to track the shape before the fully connected layers.

### Pretrained Model Handling:
- Ensured that the model is loaded with pre-trained weights correctly. Added a path check to ensure the pretrained weights file exists and is loaded during initialization.

### Error Handling:
- Added exception handling around the `torch.load()` function to catch and report any file loading issues with the pretrained model.

### Batch Normalization and Xavier Initialization:
- Added proper weight initialization for the convolutional and linear layers using Xavier initialization, and ensured that the batch normalization layers are correctly initialized for stability.

---

## Changes Made in All Files:

### Device Handling (CPU/GPU):
- Standardized the device handling to ensure compatibility with either CPU or GPU using `torch.device("cuda" if torch.cuda.is_available() else "cpu")` across all the files.

### Code Refactoring:
- Refactored several parts of the code to follow Python best practices, such as moving variable definitions inside constructors, ensuring proper method scoping, and improving readability by adding comments.

### Debugging Enhancements:
- Added multiple debug print statements throughout the files to trace tensor shapes, intermediate results, and to catch potential shape mismatches in tensors passed between layers of the model.

---


# Automated Weights Download and Extraction

This project includes a script that automates the process of downloading, extracting, and cleaning up weight files from a Google Drive link. This is useful for setting up a project with necessary pretrained weights.

## Instructions

To automate the process of downloading the weights and setting up your project, follow these steps:

### 1. Requirements

Ensure that you have `gdown` and `unzip` installed. You can install `gdown` using the following command:

```bash
pip install gdown
```

`unzip` is a standard utility and can be installed using your system's package manager. For example, on Ubuntu/Debian:

```bash
sudo apt-get install unzip
```

### 2. Run the Shell Script

You can automate the download, extraction, and cleanup process using the provided shell script. Save the script as `download_weights.sh` and ensure it is executable by running:

```bash
chmod +x download_weights.sh
```

Then, run the script:

```bash
./download_weights.sh
```

### 3. Dockerfile Instructions

If you prefer to include the process in a `Dockerfile`, add the following lines to your `Dockerfile`:

```dockerfile
# Set working directory
WORKDIR /app/weights

# Download weights.zip using gdown and extract it
RUN apt-get update && apt-get install -y unzip \
    && gdown 'https://drive.google.com/u/0/uc?id=1qcgXiaAgdvSmvU3St9cJsguK6067KcjM&export=download' -O weights.zip \
    && unzip weights.zip \
    && rm weights.zip
```

### 4. Shell Script

Here’s the shell script that you can use to automate the process:

```bash
#!/bin/bash

# Set working directory
cd /app/weights

# Download the weights.zip using gdown
gdown 'https://drive.google.com/u/0/uc?id=1qcgXiaAgdvSmvU3St9cJsguK6067KcjM&export=download' -O weights.zip

# Unzip the file
unzip weights.zip

# Remove the zip file after extraction
rm weights.zip

echo "Download and extraction completed."
```

Now, you're all set to automate the weights download process for your project!


## How to Run the Code:

1. Ensure that you have the required dependencies by installing them from `requirements.txt`:

   ```bash
   pip install -r requirements.txt

python3 run.py


