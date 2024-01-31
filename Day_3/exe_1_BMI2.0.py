print("Wecome To The BMI Tester!")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(weight) / float(height) ** 2 

BMI_Final = round(BMI, 2)
# print(BMI_Final)
if BMI_Final < 18.5:
    print("{} You are Underweight.".format(BMI_Final))
elif BMI_Final < 25:
    print("{} You have a normal weight.".format(BMI_Final))
elif BMI_Final < 30:
    print("{} You are Overweight.".format(BMI_Final))
elif BMI_Final < 35:
    print("{} You are obese.".format(BMI_Final))
else:
    print("{} you are clinically obese.".format(BMI_Final))
