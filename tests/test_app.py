# tests/test_app.py

from app import predict_score

def test_prediction_function():
    """
    Tests the predict_score function with a known input/output.
    """
    # Arrange (Known Input)
    input_hours = 5.0
    # Expected result: (5 * 5.0) + 10 = 35.0
    expected_score = 35.0
    
    # Act (Call the function)
    actual_score = predict_score(input_hours)
    
    # Assert (Check the result)
    assert actual_score == expected_score, f"Expected {expected_score}, but got {actual_score}"

def test_zero_input():
    """
    Tests the baseline prediction.
    """
    assert predict_score(0.0) == 10.0
