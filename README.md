Schizophrenia Prediction Using 3D CNNs
This repository provides a workflow for preprocessing MRI scans from different studies and training a 3D CNN model to predict schizophrenia in patients. The project leverages MRI data from both diagnosed patients and healthy control patients, with a machine learning model trained on normalized images for improved accuracy.

Project Overview
Schizophrenia is a complex mental health disorder with significant structural brain changes detectable through MRI. This project aims to automate the classification of patients as either diagnosed with schizophrenia or healthy based on 3D MRI scans. The model development follows these primary steps:

Data loading, preprocessing, and normalization across diverse MRI datasets.
Application of a 3D Convolutional Neural Network (3D CNN) for the predictive model.
Evaluation metrics to assess model accuracy and practical utility.
For an in-depth thematic overview, refer to the Google Slides Presentation.

Repository Structure
data/: Directory where MRI datasets should be placed.
notebooks/Schizophrenia_Prediction.ipynb: Jupyter notebook with step-by-step code for data loading, preprocessing, and model training.
schizophrenia_prediction_functions.py: Python script with reusable functions for loading, sorting, renaming, and normalizing MRI scans.
models/: Directory to save trained models.
Getting Started
Prerequisites
Python 3.8+
Libraries: TensorFlow, Keras, NumPy, pandas, matplotlib, nibabel (for handling MRI scans)
To install required libraries:

bash
Code kopieren
pip install tensorflow keras numpy pandas matplotlib nibabel
Dataset Requirements
The MRI datasets should be organized as follows:

Each dataset should contain scans divided by patient folders, and scans should be in NIfTI or other MRI-compatible formats.
Ensure that patient data folders are labeled by diagnosis (e.g., 'Control' for healthy and 'Schizophrenia' for diagnosed patients) to facilitate preprocessing.
Installation
Clone the repository:
bash
Code kopieren
git clone https://github.com/JimiHenning/schizophrenia-prediction-cnn.git
cd schizophrenia-prediction-cnn
Place your MRI data into the data/ directory as specified.
Usage
1. Data Preprocessing
The Jupyter notebook and schizophrenia_prediction_functions.py script contain functions to automate:

Data Loading: Load and organize MRI data by patient and diagnosis.
Data Preprocessing: Normalize MRI scans, handle artifacts, and prepare data for model training.
Example usage of functions from schizophrenia_prediction_functions.py:

python
Code kopieren
from schizophrenia_prediction_functions import load_data, normalize_data

# Load and normalize the MRI scans
mri_data = load_data('data/')
normalized_data = normalize_data(mri_data)
2. Model Training
The Jupyter notebook (notebooks/Schizophrenia_Prediction.ipynb) contains detailed code to train the 3D CNN model:

Customize model parameters, adjust hyperparameters, and train the model.
Run the notebook to start model training.
3. Evaluation
After training, evaluate the model’s performance using metrics such as accuracy, precision, and F1-score. Results and metrics are saved in the models/ directory for review.

Repository Files Overview
notebooks/Schizophrenia_Prediction.ipynb
This notebook guides you through:

Data preprocessing and visualization.
Model architecture and training.
Performance evaluation.
schizophrenia_prediction_functions.py
A Python script with helper functions for tasks including:

Loading and sorting MRI scans.
Preprocessing and normalizing data.
Utility functions for directory handling.
Google Slides Presentation
An overview of the project, its objectives, and a brief description of each processing step. View it here.

Model Description
The 3D CNN model is designed to process 3D MRI volumes and includes several convolutional layers to capture spatial features. Given the high memory demands, the model is optimized for systems with sufficient computational resources.

Model Architecture
Input Layer: Accepts 3D MRI volumes.
Convolutional Layers: Multiple 3D convolutional layers to capture spatial brain features.
Fully Connected Layers: Dense layers for classification.
Output Layer: Binary classification for Schizophrenia (1) or Control (0).
Future Improvements
Use a larger, more normalized dataset to improve model accuracy.
Leverage transfer learning by fine-tuning pre-trained 3D CNN models.
Implement data augmentation to enhance model robustness.
Contributing
Contributions to improve the data handling, model architecture, or evaluation metrics are welcome. Please open a pull request or create an issue for major changes.

License
This project is licensed under the MIT License.

This README provides a structured overview and instructions for the repository. You can copy and paste this into a README.md file in your project root directory. Let me know if any specific adjustments are needed! ​
