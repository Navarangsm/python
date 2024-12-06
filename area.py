class rectangle:
    def __init__(self,length,width):
        self.lenght=length
        self.width=width
    def area(self):
        print (self.lenght*self.width)
a=rectangle(5,10)
b=rectangle(20,30) 
c=rectangle(30,20)   
a.area() 
b.area()  
c.area()      
