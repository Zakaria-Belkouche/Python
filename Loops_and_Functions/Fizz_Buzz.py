# Zakaria Belkouche 23/10/25

n = int(input("how many fizzes and buzz's do you want??? :    "))

for i in range(0, n):
    if i % 3 == 0 and i % 5 != 0:
        print("fizz")
    
    elif i % 5 == 0 and i % 3 != 0:
        print("buzz")

    elif i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")

    else:
        print(i)


print("TRADITION!!")





