name = "YK"
height_m = 2.2
weight_kg = 80
bmi = weight_kg / (height_m ** 2)

print("USER %s with %.2f BMI is" %(name ,bmi))

if bmi >= 30:
   print("Obesity")
elif bmi >= 25:
   print("Overweight")
elif bmi >= 18.5:
   print("Healthy Weight")
else:
   print("Underweight")