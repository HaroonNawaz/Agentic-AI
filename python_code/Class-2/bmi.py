print ("BMI Calculator")

weight = int(input("What is your weight in KG? "))
height = int(input("what is your height in cm "))

height_in_cm = height/100
bmi = round(weight / (height_in_cm**2),1)

if bmi >= 40:
    print(f"Your weight is {weight}, BMI is {bmi} and you are Obese!!!")
elif bmi >= 25:
    print(f"Your weight is {weight}, BMI is {bmi} and you are Overweight")
elif bmi >=18.5:
    print(f"Your weight is {weight}, BMI is {bmi}, Congrats You are so much healthy")
else:
    print(f"Your weight is {weight}, BMI is {bmi}, you are underweight")

    