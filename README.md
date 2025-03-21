# PulmoPredict: Pneumonia Prediction using Medical Image Modality

## Overview
PulmoPredict is a state-of-the-art, computer-aided diagnostic system designed to detect pneumonia from chest X-ray images. By leveraging advanced deep learning techniques and a modern tech stack, PulmoPredict computes accurate probability values, supporting radiologists in early and precise diagnosis. The project features a robust backend powered by Flask, a dynamic frontend built with React, and a deep learning model based on VGG16 using Keras and TensorFlow2. Optional model optimization with ONNX and prototyping via Colab Notebooks further enhance its capabilities.

## Features
- **Automated Image Processing:**  
  Pre-process chest X-ray images using OpenCV-Python for improved analysis.
- **Deep Learning Detection:**  
  A fine-tuned VGG16 model (built with Keras and TensorFlow2) was used to detect pneumonia and predict probability values.
- **Modern User Interface:**  
  A responsive frontend built with React, Material-UI, and Reactstrap for a sleek, user-friendly experience.
- **Backend Services:**  
  Flask-based API for handling image uploads, prediction requests, and model serving.
- **Model Optimization:**  
  Optional conversion of models to ONNX format for improved deployment efficiency.
- **Experimentation & Prototyping:**  
  Used Colab Notebooks for training, fine-tuning, and testing the model.

## Technologies Used
- **Frontend:**  
  - React  
  - Material-UI  
  - Reactstrap
- **Backend:**  
  - Flask
- **Deep Learning:**  
  - Keras  
  - TensorFlow2  
  - VGG16 (Pre-trained and fine-tuned)
- **Image Processing:**  
  - OpenCV-Python
- **Model Deployment & Optimization:**  
  - ONNX
- **Prototyping:**  
  - Google Colab Notebook
