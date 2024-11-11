
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


## Data Overview and Handling
We were given four separate datasets:
- A dataset with general client information, including age, gender, account balance, and tenure.
- A dataset detailing which client IDs belonged to either the test or control group.
- A dataset containing all the logged online behavior of each client visit.

### Data Cleaning
We cleaned the dataset by:
- Removing null values and duplicates.
- Excluding client IDs that were not part of the experiment.
- Recasting some data types.
- Removing certain outliers for better visualization.

We merged the data on client IDs, created a control and test dataframe for analysis, and later developed a comprehensive dataframe containing everything for use in Tableau.

## Exploratory Data Analysis (EDA)
- **Age Distribution**: We have a bimodal distribution, with most clients being either between 30-35 or 50-55 years old. The mean and median age are both around 47 years, indicating that most clients tend to be above middle age.
- **Gender Distribution**: There is a relatively even gender distribution among male, female, and unknown, each comprising about a third of the clients.
- **Tenure**: Most users tend to have been clients for around 6 years, with a tenure mean of 12 and a median of 11 years, indicating that over 50% are longstanding users with more than 11 years of tenure.
- **Account Balance**: The account balance distribution is heavily positively skewed. After removing extreme outliers, the mean sits at 147,446 while the median is significantly lower at 63,334. Gender-wise, the distribution is relatively even, although extreme outliers belonged mostly to men. Individuals with unknown gender have a significantly lower mean and median.
- **Longevity**: Men and women appear to be similarly longstanding customers, while those with unknown gender tend to be relatively new customers, likely because longstanding customers have more interactions with staff where their gender might be recorded.

## KPI and Performance Metrics
To evaluate the new design’s performance, we looked at three main KPIs:
1. **Completion Rate**: Percentage of clients reaching “confirm” per visit.
2. **Error Rate**: Each time a client took a step backward compared to the total number of actions.
3. **Time Spent per Step**: The average time a client spent on each step.

We also calculated the error ratio for each step to identify optimization opportunities.

### Overall Performance
- The new design performed better, especially in the key KPI of completion rate, with some caveats:
  - The error rate in the new UI was overall slightly higher than in the old design.
  - Step one of the new online process seems to have been a downgrade, with clients taking longer and making more errors compared to the classic interface.
  
When these flaws are addressed, the new UI could be a definitive improvement.

## Hypothesis Testing
- **Null Hypothesis (H0)**: The updated design did not improve the completion rate.
- **Alternative Hypothesis (H1)**: The updated design led to a higher completion rate.
- **Significance Level (α)**: 0.05

Using a proportions z-test, we could reject the null hypothesis. The increase in completion rate exceeded the 5% threshold set by Vanguard, justifying the new design from a cost perspective.

## Experiment Evaluation
We evaluated the experiment for adequate size, structure, and randomization to identify any relevant biases:
- Is the average age of clients engaging with the new process the same as those engaging with the old process?
- Is the average client tenure (time with Vanguard) the same for clients engaging with the new process compared to the old process?
- Are there gender differences affecting client engagement with the new or old process?

Both samples were sufficiently large and similar (test group: 176,699 rows / control group: 140,536 rows), leading us to conclude that the timeframe for data gathering was adequate. 

While the differences were statistically significant according to their p-values, the Cohen's values were small enough to suggest the differences are minimal in terms of effect size. In conclusion, the raw data between the control and test groups is overall randomly distributed with minimal bias.

## Conclusion
The new design is an overall success, particularly among older clients. Improvements should be made specifically to step 1. The experiment was well-structured and exhibited little bias, making the implementation cost-effective. 

We recommend that Vanguard address these minor issues before proceeding with the full implementation of the new UI.









### Dataset Requirements

Organize MRI datasets as follows:

- Each dataset should contain scans in patient scans in NIfTI format sorted by study.
- Label study subfolders by diagnosis (e.g., 'control' for healthy, 'schiz' for diagnosed) for preprocessing.

### 1. Data Preprocessing

The Jupyter notebook and `schizophrenia_prediction_functions.py` script provide functions for:
- **Metadata Preparation**: Organize MRI metadata by patient and diagnosis and study.
- **Data Loading**: Organize MRI data by patient and diagnosis.
- **Data Preprocessing**: Normalize MRI scans, handle artifacts, and prepare data for training.

### 2. Model Training

The `Schizophrenia_Prediction.ipynb` notebook contains code for:
- Model customization and hyperparameter adjustment.
- Running model training.

### 3. Evaluation

Evaluate model performance using metrics like accuracy, precision, and F1-score.

## Repository Files Overview

### `notebooks/Schizophrenia_Prediction.ipynb`

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

- Larger, more normalized dataset for better accuracy.
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

This version is formatted for easier reading and better structure in Markdown files on GitHub or other markdown editors. Let me know if you'd like further customization!
