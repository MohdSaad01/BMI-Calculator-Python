print("Welcome to the Body Mass Index calculator.")

age=int(input("Enter your Age."))

gender=(input("Enter your gender."))

height=float(input("Enter your height in meter."))

weight=float(input("Enter your weight in kg."))

Bmi = weight / (height ** 2)
bmi=round(Bmi,2)
print(f"Your BMI is:{bmi}")

if bmi < 18.5:
    print("You are Underweight!")
elif bmi == 18.5:
    print("You are of Normal Weight!")
elif bmi < 25:
    print("You are of Normal Weight!")
else:
    print("You are Overweight!")