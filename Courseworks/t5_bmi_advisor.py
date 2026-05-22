# BODY MASS INDEX (BMI) ADVISOR

# Get user details
name = input("Hello! Enter your your name: ")

try:
    weight = float(input("Enter your weight (Kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than zero.")

    else:
        # BMI formula
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            advisory = "Increase nutritional intake and consult a health specialist."

        elif bmi < 25:
            category = "Normal"
            advisory = "Maintain a balance diet."

        elif bmi < 30:
            category = "Overweight"
            advisory = "Exercise regularly and monitor your diet."
        
        else:
            category = "Obese"
            advisory = "Seek medical guidance and adopt a healther lifestyle."

        #Output
        print(
            f"Name: {name} | "
            f"BMI:  {bmi:.1f} | "
            f"Category: {category} | "
            f"Advisory: {advisory}"
        )

except ValueError:
    print("Error: Please enter valid numeric values")