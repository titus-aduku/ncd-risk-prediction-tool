# clinical_utils.py

def calculate_bmi(weight_kg, height_m):
    """Calculates the Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The calculated BMI value.
    """
    # Defensive check: prevent division by zero
    if height_m == 0:
        return 0
    
    bmi_result = weight_kg / (height_m * height_m)
    return bmi_result

def convert_lbs_to_kg(weight_lbs):
    """Converts a weight from pounds to kilograms.

    Args:
        weight_lbs (float): Weight in pounds (lbs).

    Returns:
        float: The equivalent weight in kilograms (kg).
    """
    kg_result = weight_lbs * 0.453592
    return kg_result

# This is the main function that runs our test code.
def main():
    """Main function to test the utility functions."""
    print("--- Running Tests for Clinical Utilities ---")

    # Test Case 1: Test calculate_bmi
    test_bmi = calculate_bmi(70, 1.75)
    print(f"Test BMI for 70kg, 1.75m: {test_bmi}")

    # Test Case 2: Test convert_lbs_to_kg
    test_kg = convert_lbs_to_kg(150)
    print(f"Test Conversion for 150lbs: {test_kg}")

# This special block ensures that the main() function is only called
# when you run this script directly (e.g., "python clinical_utils.py").
# It won't run if this file is imported by another script.
if __name__ == "__main__":
    main()