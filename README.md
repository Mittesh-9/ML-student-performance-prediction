# Student Performance Prediction

This repository contains a machine learning project that predicts students' academic performance based on various features such as gender, parental level of education, and more.

## Project Overview

The main goal of this project is to build a predictive model that estimates a student's final grade or academic performance using features derived from their personal and academic background.

### Key Features:
- **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling features.
- **Feature Engineering**: Selection of the most impactful features for the model.
- **Model Training**: Several machine learning algorithms were explored, and the best-performing model was saved for making predictions.
- **Evaluation**: The model is evaluated based on accuracy, precision, recall, and F1 score to measure its performance.

## Notebooks

The main workflow of the project is divided into Jupyter notebooks:

### `data_preprocessing_and_model_training.ipynb`:
- This notebook handles data preprocessing steps like cleaning, encoding, and feature selection.
- It trains various machine learning models and evaluates them based on their performance metrics.
- The final trained model is saved for future predictions.

## Dataset

The dataset contains various features related to students’ academic and personal lives. It includes attributes such as:
- **Gender**
- **Parental level of education**
- **Test preparation course**
- **Attendance**
- **Grades**

The dataset was preprocessed to ensure it was clean and suitable for machine learning tasks, with missing values imputed and categorical features encoded.

## Technologies Used

- **Python**: The main programming language used in the project.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **scikit-learn**: For building and evaluating machine learning models.
- **joblib**: For saving the trained machine learning models.
