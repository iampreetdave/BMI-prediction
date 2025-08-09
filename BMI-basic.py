try:
    weight = float(input("Enter your weight in kg: "))
    h = float(input("Enter your height in cm: "))
    asian = input("Are you Asian or South Asian? (yes/no): ").strip().lower()
    height=h/100
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
    else:
        bmi = weight / (height ** 2)
        print(f"Your BMI is {bmi:.2f}")

        # Asian/South Asian ranges
        if asian == "yes":
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 23:
                category = "Normal weight"
            elif 23 <= bmi < 25:
                category = "Overweight (Asian range)"
            else:
                category = "Obese (Asian range)"
        
        # Standard ranges
        else:
            if bmi < 16.5:
                category = "Severely underweight"
            elif bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            elif bmi < 35:
                category = "Obesity Class I"
            elif bmi < 40:
                category = "Obesity Class II"
            else:
                category = "Obesity Class III"
        
        print(f"Category: {category}")

except ValueError:
    print("Invalid input. Please enter numbers only.")
