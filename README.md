# Shipment Delay Prediction System

## Overview
This repository contains the code for a machine learning-based shipment delay prediction system. The project utilizes Random Forest as the predictive model, FastAPI for API development, and a simple GUI for ease of use by non-technical users.

## Table of Contents
1. [Dataset Exploration and Cleaning](#dataset-exploration-and-cleaning)
2. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
3. [Preprocessing](#preprocessing)
4. [Model Training and Evaluation](#model-training-and-evaluation)
5. [API Development](#api-development)
6. [GUI Integration](#gui-integration)
7. [Decisions Made](#decisions-made)
8. [Future Improvements](#future-improvements)

## Dataset Exploration and Cleaning

### Dataset Overview
The project began by exploring the dataset, identifying null values, and assessing relationships between features and the target variable (`Delayed`).

### Null Value Handling
There were 597 missing values in the `Vehicle_Type` column. Since it is a categorical variable, these were filled using the mode of the column, ensuring minimal bias.

### Feature Selection
- Columns like `Shipment ID`, `Shipment Date`, `Planned Delivered Date`, and `Actual Delivery Date` were excluded because they did not significantly influence the target variable.
- Key columns like `Traffic_Conditions`, `Weather_Conditions`, and `Distance (km)` were retained, as they had clear impacts on shipment delays.

## Exploratory Data Analysis (EDA)

### Visualizations
Graphical analyses revealed insights, such as a strong correlation between high/moderate traffic and shipment delays.

### Unique Value Identification
Unique values in categorical columns were noted for encoding purposes.

## Preprocessing

### Categorical Encoding
Label encoders were used to convert categorical features into numerical representations.

### Feature Selection
A final list of features was prepared based on their relevance to the prediction task.

### Data Splitting
The dataset was split into training (80%) and testing (20%) sets for model evaluation.

## Model Training and Evaluation

### Model Selection
- Logistic Regression, Decision Tree, and Random Forest models were trained.
- Models were evaluated using accuracy, precision, recall, and F1 score.

### Best Model
- Logistic Regression showed relatively lower accuracy.
- Random Forest demonstrated superior performance and was chosen as the final model due to its robustness and accuracy.

### Visualization
Performance metrics were visualized to clearly compare the models.

### Saving Model and Encoders
The trained Random Forest model and label encoders were serialized using `joblib` for easy deployment in the API.

## API Development

### Setup
- An environment was created in Anaconda, and libraries like FastAPI were installed.

### API Implementation
- `shipment_api.py` was created to implement the FastAPI application.
- Input validation was handled using Pydantic.
- A `/predict` endpoint was developed to preprocess inputs, use the Random Forest model for predictions, and return results.

### Testing API
- A client script (`api_implementation.py`) was created to send POST requests to the API with test data.
- The predictions were displayed in the terminal.

## GUI Integration

### Purpose
A small GUI was created to enhance usability for non-technical users.

### Functionality
- Users can select shipment features like origin, destination, vehicle type, weather conditions, and traffic conditions.
- The GUI interacts with the API to provide real-time predictions.

## Decisions Made

- Random Forest was chosen due to its ability to handle diverse data types and deliver high accuracy.
- FastAPI was selected for its speed and ease of creating RESTful APIs.
- The GUI was added to improve accessibility for users unfamiliar with APIs.

## Future Improvements

- Add more features to the GUI, such as detailed result explanations or interactive visualizations.
- Enhance API security with authentication mechanisms.
- Incorporate logging and monitoring for better debugging and performance tracking.

---

