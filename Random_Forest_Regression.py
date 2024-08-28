# Random Forest Regression

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import Machine Learning Libraries
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
