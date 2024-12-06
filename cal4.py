num1=float(input("enter the 1st number:"))
num2=float(input("enter the 2nd number:"))
print("select operation") 
print("1.addition\n2.substraction\n3.divison\n4.multiplication\n5.exit")
operation = int(input("enter the choice:"))
def calculator(num1,num2,operation):
    if operation ==1:
        return(f"{num1+num2}")
    elif  operation ==2:
         return(f"{num1-num2}")    
    elif  operation ==3:
        if num2!=0:
             return(f"{num1/num2}")
        else:
            return("error:divison by zero not allowed")     
    elif operation ==4:
        return(f"{num1*num2}")
    elif operation==5:
        return("exit")           
    else:
        return("invalid choice")
result = calculator(num1,num2,operation)
print("result:",result)