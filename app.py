# app.py

import pandas as pd

# 1. Define a model/prediction function
def predict_score(hours_studied: float) -> float:
    """
    A simple linear model: score = 5 * hours_studied + 10
    (Represents a trained ML model for predicting test score based on study hours)
    """
    # Simulate a small data transformation step (using pandas just to require it)
    data = pd.Series([hours_studied])
    
    # Simple prediction logic
    predicted_score = (5 * data.iloc[0]) + 10
    
    # Ensure the result is a standard float
    return float(predicted_score)

# 2. An entry point (optional, but good practice)
if __name__ == "__main__":
    test_hours = 4.0
    result = predict_score(test_hours)
    print(f"Predicted score for {test_hours} hours: {result}")
