username = input("enter the name:")
if username.isalnum() and 6 <= len(username) <=15:
    print(" valid user name")
else:
    print("invalid username")
    
