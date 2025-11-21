
print("input 3 numbers")
x = int(input("Number 1:         "))
y = int(input("Number 2:         "))
z = int(input("Number 3:         "))

def largest(x, y, z):
    c = [0]
    for n in [x, y, z]:
        if n > c[0]:
            c.clear()
            c.append(n)
    return c

print(largest(x, y, z))


