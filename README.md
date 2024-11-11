
# schizophrenia-prediction-cnn

## Presentation:

- [Presentation](https://docs.google.com/presentation/d/1WSHAT3Yc5fbAgA5XTn4BtV-cnNzOG3IDVC3L0c8aZhk/edit?usp=sharing)

# SCHIZOPHRENIA PREDICTION USING A 3D CNN MODEL APPROACH

This repository contains code and resources for preprocessing MRI scans from different studies and training a 3D CNN model to predict schizophrenia in patients. The project leverages MRI data from both diagnosed patients and healthy control patients, with a machine learning model trained on normalized images for improved accuracy.

## Project Overview

Schizophrenia is a complex mental health disorder with subtle but distinct structural brain changes detectable through MRI. This project automates the classification of patients as either diagnosed with schizophrenia or healthy based on MRI scans. The model development follows these primary steps:

1. **Data Loading & Preprocessing**: Normalization across diverse MRI datasets.
2. **3D CNN Model Application**: Predictive model training.
3. **Evaluation Metrics**: Accuracy assessment and model utility.

For a thematic overview, refer to the [Google Slides Presentation](https://docs.google.com/presentation/d/1WSHAT3Yc5fbAgA5XTn4BtV-cnNzOG3IDVC3L0c8aZhk/edit#slide=id.p).

## Installation

To get started with this project, ensure you have the following libraries installed in your Python environment:

- `pandas` - For data manipulation and analysis
- `numpy` - For numerical operations
- `scipy` - For statistical tests
- `matplotlib` - For data visualization
- `seaborn` - For statistical data visualization
- `scikit-learn` - For training and testing split
- `nibabel` - To read and manipulate .nii or .nii.gz MRI files
- `tensorflow` - To create and compile machine learning models

Further tools and libraries:
- `CUDA` - For GPU usage with tensorflow
- `cuDNN` - For GPU usage in deep learning models
- `FSL` - For brain extraction and alignment tools (https://fsl.fmrib.ox.ac.uk/fsl/docs/#/structural/bet)

## Data Sources

The datasets used in this project include:

[https://fcon_1000.projects.nitrc.org/indi/retro/cobre.html]  -> Needs NITRC Request and Approval
[https://openneuro.org/datasets/ds005073/versions/1.0.0]
[https://openneuro.org/datasets/ds004837/versions/1.0.0]
[https://openneuro.org/datasets/ds004302/versions/1.0.1]
[https://openneuro.org/datasets/ds004873/versions/2.0.3]


### Dataset Requirements

Organize MRI datasets as follows:

- Each dataset should contain scans in patient scans in NIfTI format sorted by study.
- Label study subfolders by diagnosis (e.g., 'control' for healthy, 'schiz' for diagnosed) for preprocessing.

### 1. Data Preprocessing

The Jupyter notebook and `schizophrenia_prediction_functions.py` script provide functions for:
- **Metadata Preparation**: Organize MRI metadata by patient and diagnosis and study.
- **Data Loading**: Organize MRI data by patient and diagnosis.
- **Data Preprocessing**: Normalize MRI scans, handle artifacts, and prepare data for training.


## 2. Exploratory Data Analysis (EDA)
- **Age Distribution**: For such a small sample size a relatively even age distribution between diagnosed and control group after removing all patients over 55 years of age to remove age-related atrophy as a confounding variable. Further selection would have reduced the sample size too much.
- **Gender Distribution**: Relatively even distribution between control and diagnosed groups, similar sample size concerns limited further selection.
- **Handedness**: Only right-handed patients where selected for training the model.

### 2. Model Training

The `Schizophrenia_Prediction_final.ipynb` notebook contains code for:
- Model customization and hyperparameter adjustment.
- Running model training.

### 3. Evaluation

Evaluate model performance using metrics like accuracy, precision, and F1-score.

## Repository Files Overview

### `schizophrenia_prediction_final.ipynb`

Guides through:
- **Data Preprocessing & Visualization**
- **Model Architecture & Training**
- **Performance Evaluation**

### `schizophrenia_prediction_functions.py`

Python script with helper functions for:
- Loading and sorting MRI scans.
- Preprocessing and normalization.
- Directory handling utilities.

## Model Description

The 3D CNN model processes 3D MRI volumes and includes convolutional layers for capturing spatial features. It’s optimized for systems with sufficient computational resources.

### Model Architecture

- **Input Layer**: Accepts 3D MRI volumes.
- **Convolutional Layers**: Capture spatial features.
- **Fully Connected Layers**: Dense layers for classification.
- **Output Layer**: Binary classification (Schizophrenia or Control).

## Future Improvements

- Significantly larger, more normalized dataset for better accuracy.
- Leveraging more computational power for higher complexity models.
- Use of transfer learning with pre-trained 3D CNNs.
- Data augmentation for enhanced robustness.

## Contributing

Contributions are welcome to improve data handling, model architecture, or evaluation metrics. Open a pull request or create an issue for major changes.

## License

This project is licensed under the MIT License.

FSL BET TOOL: 
S.M. Smith. Fast robust automated brain extraction. Human Brain Mapping, 17(3):143-155, November 2002

FLIRT TOOL: 
Jenkinson, M., Bannister, P., Brady, J. M. and Smith, S. M. Improved Optimisation for the Robust and Accurate Linear Registration and Motion Correction of Brain Images. NeuroImage, 17(2), 825-841, 2002.
Jenkinson, M. and Smith, S. M. A Global Optimisation Method for Robust Affine Registration of Brain Images. Medical Image Analysis, 5(2), 143-156, 2001.
Greve, D.N. and Fischl, B. Accurate and robust brain image alignment using boundary-based registration. NeuroImage, 48(1):63-72, 2009.

---

