# Zakaria Belkouche 26/10/25

print("Type 'quit' to end your order")

toppings = set()
sides = set()
drinks = set()

while True:
    x = input("Select:  1) Burger   2) Side     3) Drink    4) Combo   :").lower()
    if x == "quit":
        break
    if x == "burger":
        print("Each topping will cost 50 cents. Type anything to exit")
        y = input("choose your toppings: 1) Onion   2) Lettuce   3) Tomato    :").lower()
        if y in ("onion", "lettuce", "tomato"):
            toppings.add(y)
        while y in ("onion", "lettuce", "tomato"):
            print("Type anything else to exit")
            y = input("any other toppings?              ").lower()
            if y in ("onion", "lettuce", "tomato"):
                toppings.add(y)

    if x == "side":
        print("Choose a side")
        z = input("1) Fries     2) Corn     3) Peas     :").lower()
        if z in ("fries", "corn", "peas"):
            sides.add(z)
        while z in ("fries", "corn", "peas"):
            print("type anything else to exit")
            z = input("any other sides?").lower()
            if z in ("fries", "corn", "peas"):
                sides.add(z)


    if x == "drink":
        print("Choose a drink. Each drink costs $1")
        d = input("1) Coke      2) Fanta     3) Pepsi     :").lower()
        if d in ("coke", "fanta", "pepsi"):
            drinks.add(d)
        while d in ("coke", "fanta", "pepsi"):
            print("Type anything else to exit")
            d = input("any other drinks?            ").lower()
            if d in ("coke", "fanta", "pepsi"):
                drinks.add(d)


if toppings:
    print(f"Your burger toppings are: {toppings}")
if sides:
    print(f"Your side selection is: {sides}")
if drinks:
    print(f"Your drink selection is: {drinks}")


# Still a work in progress... I know I'm doing this wrong and overcomplicating things. I will start over
