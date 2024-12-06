num1=float(input("enter the number:"))
num2=float(input("enter the number:"))
def calculator():
    print("1.addition\n2.substraction\n3.divison\n4.multiplication\n5.exit")
    choice = input("enter the choice:")
    if choice =='1':
        print(f"{num1+num2}")
    elif  choice =='2':
         print(f"{num1-num2}")    
    elif  choice =='3':
        if num2!=0:
             print(f"{num1/num2}")
        else:
            print("error:divison by zero not allowed")     
    elif choice =='4':
        print(f"{num1*num2}")    
    else:
        print("invalid choice")
calculator()                          