#employees = {"antony":55000,"susan":45000,"kiran":60000}
#high = dict(filter(lambda item: item[1]>=50000,employees.items()))
#low = dict(filter(lambda item: item[1]<50000,employees.items()))
#catergorise = {**{name:"high" for name in high},**{name:"low" for name in low}}
#print("output:",catergorise)


employees = {'Antony': 55000, 'Susan': 45000, 'Kiran': 60000}
salary_categories = list(map(lambda item: (item[0], 'high' if item[1] >= 50000 else 'low'), employees.items()))
categorized = dict(salary_categories)
print("output:",categorized)