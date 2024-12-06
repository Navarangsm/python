def calculator():
    num1=float(input("enter the 1st number:"))
    num2=float(input("enter the 2nd number:"))
    print("select operation") 
    print("1.addition\n2.substraction\n3.divison\n4.multiplication\n5.exi")    
    operation = int(input("enter the choice:"))
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
for i in range(6):        
    result = calculator()
    print("output:",result)
    