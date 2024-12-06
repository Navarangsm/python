def calculate_bmi(weight,height):
    return weight/((height/100)**2)
weight=float(input("enter the weight:"))
height=float(input("enter the height: "))
bmi=calculate_bmi(weight,height)
print(f"your is bmi is:{bmi}")