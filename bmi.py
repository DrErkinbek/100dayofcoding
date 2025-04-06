height = int(input("Enter your height in cm"))
weight = int(input("Enter your weight in kg"))
bmi = weight / (height**2)

if bmi >= 25:
	print("overweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
elif bmi < 18.5:
    print("underweight")

print(int(bmi))
print(round(bmi, 2))