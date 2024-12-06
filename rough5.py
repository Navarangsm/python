from functools import reduce


n=[1,2,3,4,5,6,8,7]

evens=list(filter(lambda n: n%2==0 ,n))

double = list(map(lambda n : n*2,evens))

sum = reduce(lambda a,b : a*b,double)
 
print(evens)
print(double)
print(sum)