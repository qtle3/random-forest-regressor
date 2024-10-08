# Salary Prediction using Random Forest Regression

This project demonstrates the use of **Random Forest Regression** to predict the salary of an employee based on their position level. The script leverages a dataset containing position levels and corresponding salaries, and trains a Random Forest model to make predictions for various position levels.

## Detailed Summary

The script begins by loading the `Position_Salaries.csv` dataset, which includes employee position levels and their respective salaries. A **Random Forest Regressor** model is then trained on this dataset. Random Forest is an ensemble learning method that builds multiple decision trees and averages their predictions to provide a more robust and accurate estimate.

The script performs the following steps:

1. **Data Loading:**
   - Loads the dataset and extracts the independent variable (position levels) and the dependent variable (salaries).

2. **Model Training:**
   - Trains a **Random Forest Regression model** using 10 decision trees (`n_estimators=10`) on the entire dataset. The random forest algorithm is particularly effective in capturing complex relationships in the data by averaging the outputs of multiple trees to reduce variance and prevent overfitting.

3. **Prediction:**
   - Predicts the salary for specific position levels (6.5, 2.5, and 9) using the trained Random Forest model. The model’s predictions are based on the average output of the individual decision trees in the forest.

4. **Output:**
   - The predicted salaries for the given position levels are printed, allowing for a direct comparison between the model’s predictions and expected salary values.

## Key Concepts Covered

- **Random Forest Regression:** An ensemble learning method that constructs multiple decision trees during training and outputs the average of their predictions, leading to improved accuracy and robustness in prediction tasks.
- **Ensemble Learning:** Combines multiple models (in this case, decision trees) to improve the overall performance compared to individual models.
- **Prediction:** Demonstrates how the Random Forest model can be used to predict the salary for different position levels by averaging the outputs of the trees.
- **Model Training and Evaluation:** The script trains the Random Forest model on the full dataset and evaluates its performance by making predictions on new data points.

## How to Run

1. **Install required dependencies:**
   ```bash
   pip install numpy pandas matplotlib scikit-learn
   python random_forest_regression.py
