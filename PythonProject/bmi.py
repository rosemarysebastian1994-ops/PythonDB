#Write a program to find the BMI
#BMI = weight in kg/height**2 in m
#Adult BMI
#BMI        Status
#<=18.4     Underweight
#18.5-24.9  Normal
#25.0-39.9  Overweight
#>-40.0     Obese

weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in m: "))
bmi = weight/(height**2)
if bmi <= 18.4:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif 25.0 <= bmi <= 39.9:
    print("Overweight")
elif bmi >= 40:
    print("Obese")
else:
    print("Invalid input")