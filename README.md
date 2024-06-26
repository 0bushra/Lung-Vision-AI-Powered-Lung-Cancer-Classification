# Lung-Vision-AI-Powered-Lung-Cancer-Classification

Lung Vision is a state-of-the-art tool designed to classify histopathological lung images into three distinct categories: Lung Squamous Cell Carcinoma, Lung Adenocarcinoma, and Lung Benign Tissue. Utilizing deep learning algorithms and a dataset of 15,000 images, this project aims to enhance the diagnostic accuracy and speed in the detection of lung cancer, leveraging technological advancements to significantly improve patient outcomes.

# Project Overview
Lung cancer remains one of the most common and lethal types of cancer worldwide. Early detection is crucial for successful treatment outcomes. Lung Vision addresses this need by providing an AI-driven tool that classifies lung tissue samples with high accuracy, aiding pathologists and medical researchers in their diagnostic processes.


The Lung Vision project utilizes a Convolutional Neural Network (CNN) designed to classify histopathological images into three categories of lung tissues: Lung Squamous Cell Carcinoma, Lung Adenocarcinoma, and Lung Benign Tissue. The CNN architecture is tailored to process standardized images of 224x224 pixels using multiple convolutional and pooling layers to extract and learn from visual features, followed by fully connected layers that drive the classification. Training the model involves crucial steps such as data preprocessing, batch processing with 64 images per batch for efficiency, and data augmentation to enhance model generalization. The model is optimized using the Adam optimizer and evaluates performance through cross-entropy loss.

The training includes using a validation set to tune parameters and control overfitting, with a separate testing set to evaluate generalization to new data. The final trained model is deployed using Flask within a Docker container to ensure reliability across different systems, providing a user-friendly web interface for uploading images and receiving diagnostic predictions. This project not only highlights advanced AI in medical diagnostics but also ensures robust performance and practical usability in clinical settings.

# Technologies Used
- Flask: Serves the backend framework to create a user-friendly web interface for uploading and classifying images.
- Docker: Ensures the application is easily deployable and consistent across all platforms.
- MongoDB: Manages and stores image metadata and user data, providing scalability and flexibility in data handling.

# Installation
Ensure that you have the following installed:

- Git
- Docker
Clone the Repository
First, clone the repository to your local machine:
git clone https://github.com/yourgithubusername/lung-vision.git
