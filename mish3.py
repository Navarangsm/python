customers = ["rahul","antony","salman","arun","kiran"]
a = list(filter(lambda customer: customer.startswith("a"),customers))
print(a)