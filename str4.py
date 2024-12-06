string = "Hello world from Python"
lst=list(string)
lst.reverse()
print("reversed item",lst)
result=list(dict.fromkeys(lst))
print("removed duplicate",result)
letter_count={}
for char in result:
        letter_count[char]=letter_count.get(char,0) +1
print("letter count",letter_count)        
