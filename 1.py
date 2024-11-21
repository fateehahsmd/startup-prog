# 1. BMI logic using if/else statements
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:  # BMI >= 30
        return "Obese"

# Example usage
print(bmi_category(22))  # Output: Normal