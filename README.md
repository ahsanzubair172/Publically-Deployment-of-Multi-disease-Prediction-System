# Multi-Disease Prediction System

## Overview

The **Multi-Disease Prediction System** is a machine learning-based web application that predicts the likelihood of three diseases:

- **Diabetes**
- **Heart Disease**
- **Parkinson's Disease**

The application is built using **Streamlit** and integrates **machine learning models** trained on relevant datasets to provide predictions based on user input.

## Features

- User-friendly **web interface** built with Streamlit.
- Supports **three disease predictions** with different machine learning models.
- Uses **pre-trained models** loaded via `pickle`.
- Provides **instant predictions** based on user input.
- Implements **structured forms** for easy data entry.

## Tech Stack

- **Python**
- **Streamlit** (for UI)
- **Machine Learning Models** (Decision Trees, Logistic Regression, KNN etc.)
- **Pickle** (for model loading)
- **Streamlit Option Menu** (for navigation)

## Installation

### Prerequisites

Ensure you have Python installed (preferably Python 3.8+).

### Steps to Set Up

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/multi-disease-prediction.git
   cd multi-disease-prediction
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   streamlit run app.py
   ```

## How to Use

### 1. Select Disease Type

Navigate to the **sidebar** and select the disease you want to predict:

- Diabetes
- Heart Disease
- Parkinson’s Disease

### 2. Enter Required Information

Each disease prediction page contains input fields for relevant medical details. Enter values based on the following:

#### Diabetes Prediction Inputs:

- **Gender** (0 = Female, 1 = Male, 2 = Other)
- **Age**
- **Hypertension** (0 = No, 1 = Yes)
- **Heart Disease** (0 = No, 1 = Yes)
- **Smoking History** (0 = No, 1 = Yes)
- **BMI**
- **HemoglobinA1c Level**
- **Blood Glucose Level**

#### Enter input like this for other modals 

### 3. Get Prediction

After entering the details, click the **Predict Result** button.

- If the prediction result is `0`, the model predicts that you **do not** have the disease.
- If the prediction result is `1`, the model suggests **potential disease presence**, and users are advised to **consult a doctor** for further examination.

## File Structure

```
Multi-Disease-Prediction/
│── models/
│   ├── diabetes_model.pkl
│   ├── heart_model.pkl
│   ├── parkinsons_model.pkl
│── app.py
│── requirements.txt
│── README.md
```

## Future Enhancements

- **Expand Disease Coverage:** Add models for more diseases.
- **Improve UI/UX:** Enhance the web interface with more interactive elements.
- **Deploy on Cloud:** Make the app publicly accessible using cloud platforms like AWS/GCP/Heroku.
- **Data Visualization:** Provide graphical insights on health trends.

## Conclusion

This project demonstrates how **machine learning** can assist in preliminary health predictions. However, it is not a replacement for professional medical diagnosis. Always consult a **qualified healthcare provider** for accurate assessments.

---

### 🚀 Enjoy using the Multi-Disease Prediction System! 🎯

