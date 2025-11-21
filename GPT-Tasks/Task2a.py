# same thing but as a Lambda. 

y = int(input("input a number:       "))

func = lambda: "even" if y%2 == 0 else "odd"

print(func())

