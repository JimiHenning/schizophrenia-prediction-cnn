Schizophrenia Prediction Using 3D CNNs
This repository provides a workflow for preprocessing MRI scans from different studies and training a 3D CNN model to predict schizophrenia in patients. The project leverages MRI data from both diagnosed patients and healthy control patients, with a machine learning model trained on normalized images for improved accuracy.

Project Overview
Schizophrenia is a complex mental health disorder with significant structural brain changes detectable through MRI. This project automates the classification of patients as either diagnosed with schizophrenia or healthy based on 3D MRI scans. The model development follows these primary steps:

Data Loading & Preprocessing: Normalization across diverse MRI datasets.
3D CNN Model Application: Predictive model training.
Evaluation Metrics: Accuracy assessment and model utility.
For a thematic overview, refer to the Google Slides Presentation.

Repository Structure
data/: Directory for MRI datasets.
notebooks/Schizophrenia_Prediction.ipynb: Jupyter notebook for data loading, preprocessing, and model training.
schizophrenia_prediction_functions.py: Python script with reusable functions for data preparation.
models/: Directory to save trained models.
Getting Started
Prerequisites
Python 3.8+
Required libraries: TensorFlow, Keras, NumPy, pandas, matplotlib, nibabel
Install libraries with:

bash
Code kopieren
pip install tensorflow keras numpy pandas matplotlib nibabel
Dataset Requirements
Organize MRI datasets as follows:

Each dataset should contain scans in subfolders for each patient, in formats like NIfTI.
Label folders by diagnosis (e.g., 'Control' for healthy, 'Schizophrenia' for diagnosed) for preprocessing.
Installation
Clone the repository:
bash
Code kopieren
git clone https://github.com/JimiHenning/schizophrenia-prediction-cnn.git
cd schizophrenia-prediction-cnn
Place MRI data into the data/ directory.
Usage
1. Data Preprocessing
The Jupyter notebook and schizophrenia_prediction_functions.py script provide functions for:

Data Loading: Organize MRI data by patient and diagnosis.
Data Preprocessing: Normalize MRI scans, handle artifacts, and prepare data for training.
Example:

python
Code kopieren
from schizophrenia_prediction_functions import load_data, normalize_data

# Load and normalize MRI scans
mri_data = load_data('data/')
normalized_data = normalize_data(mri_data)
2. Model Training
The Schizophrenia_Prediction.ipynb notebook contains code for:

Model customization and hyperparameter adjustment.
Running model training.
3. Evaluation
Evaluate model performance using metrics like accuracy, precision, and F1-score. Metrics are saved in models/ for review.

Repository Files Overview
notebooks/Schizophrenia_Prediction.ipynb
Guides through:

Data Preprocessing & Visualization
Model Architecture & Training
Performance Evaluation
schizophrenia_prediction_functions.py
Python script with helper functions for:

Loading and sorting MRI scans.
Preprocessing and normalization.
Directory handling utilities.
Google Slides Presentation
An overview of project objectives and a description of each processing step. View Presentation.

Model Description
The 3D CNN model processes 3D MRI volumes and includes convolutional layers for capturing spatial features. It’s optimized for systems with sufficient computational resources.

Model Architecture
Input Layer: Accepts 3D MRI volumes.
Convolutional Layers: Capture spatial features.
Fully Connected Layers: Dense layers for classification.
Output Layer: Binary classification (Schizophrenia or Control).
Future Improvements
Larger, more normalized dataset for better accuracy.
Use of transfer learning with pre-trained 3D CNNs.
Data augmentation for enhanced robustness.
Contributing
Contributions are welcome to improve data handling, model architecture, or evaluation metrics. Open a pull request or create an issue for major changes.

License
This project is licensed under the MIT License.

This version is formatted for easier reading and better structure in Markdown files on GitHub or other markdown editors. Let me know if you'd like further customization!
