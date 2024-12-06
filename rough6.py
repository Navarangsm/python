a = float(input("enter a number: "))
b = float(input("enter a number: "))
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError:
        print("division by zero is not allowed")

print("rest of the code")