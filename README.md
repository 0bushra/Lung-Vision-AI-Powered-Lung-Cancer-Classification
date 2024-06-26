# Lung-Vision-AI-Powered-Lung-Cancer-Classification

Lung Vision is a state-of-the-art tool designed to classify histopathological lung images into three distinct categories: Lung Squamous Cell Carcinoma, Lung Adenocarcinoma, and Lung Benign Tissue. Utilizing deep learning algorithms and a dataset of 15,000 images, this project aims to enhance the diagnostic accuracy and speed in the detection of lung cancer, leveraging technological advancements to significantly improve patient outcomes. The dataset used in this project is sourced from Kaggle:https://www.kaggle.com/datasets/andrewmvd/lung-and-colon-cancer-histopathological-images

<p align="center">
  <img src="https://github.com/0bushra/Lung-Vision-AI-Powered-Lung-Cancer-Classification/assets/103776716/73cc31cf-eefb-43b6-8b37-1d0002e429fc" width="200">
  <img src="https://github.com/0bushra/Lung-Vision-AI-Powered-Lung-Cancer-Classification/assets/103776716/76139a15-c27c-4b72-b877-88f922827c59" width="200">
  <img src="https://github.com/0bushra/Lung-Vision-AI-Powered-Lung-Cancer-Classification/assets/103776716/1c3a0221-7bf2-4622-98bd-66ff3011fe9d" width="200">
</p>
<table align="center" style="font-size: 14px; text-align: center; width: 100%;">
  <tr>
    <td><em>Lung Adenocarcinoma</em></td>
    <td><em>Lung Benign Tissue</em></td>
    <td><em>Lung Squamous Cell Carcinoma</em></td>
  </tr>
</table>






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
1. **Clone the repository:**

   Clone the Lung Vision repository to your local machine by running:

   ```bash
   git clone https://github.com/yourgithubusername/lung-vision.git
   cd lung-vision
2. **Set up a virtual environment**
   For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
3. **Install the required packages:**
    ```bash
     pip install -r requirements.txt

4. **Set up the environment variables:**
 Create a .env file in the project root directory and add the following:
   ```bash
   MONGO_URI=your_mongodb_connection_string
   FLASK_APP=app.py
   FLASK_ENV=development
Replace your_mongodb_connection_string with your actual MongoDB connection string.

5. **Run the application:**
   ```bash
    python app.py



