# Completed on: 23/10/25

size = input("Choose a cup size: 1) S   2) M    3) L    :")

coffee = input("choose a coffee: 1) brewed  2) expresso  3) cold brew   :")

flavour = input("Choose a syrup flavour: 1) hazeulnut  2) vanilla  3) caramel   4) none  :")

if size.lower() in ("s"):
    x = 2

if size.lower() in ("m"):
    x = 3

if size.lower() in ("l"):
    x = 4

if coffee.lower() in ("brewed"):
    y = 0

if coffee.lower() in ("expresso"):
    y = 0.5

if coffee.lower() in ("cold brew"):
    y = 1

if flavour.lower() in ("none"):
    z = 0
else:
    z = 0.5

def price(x, y, z):
    return x + y + z

price = price(x, y, z)

def priceTip(x, y, z):
    total = (x+y+z)+(((x + y + z)/100)*15)
    return round(total, 2)

price_tip = priceTip(x, y, z)

print(f"You have ordered a {size} {coffee} with {flavour}")
print(f"The total price without a tip is: {price}")
print(f"The total price with a tip is: {price_tip}")


