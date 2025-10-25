x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
z = x.copy()

while True:
    try: 
        y = input("choose an operation: add / remove or quit to stop:       ").lower()
        t = int(input("pick a random integer:              "))

        if y not in ("add", "remove", "quit"):
            raise Exception

    except Exception as e:
        print("Please input a valid integer and the correct string")
        continue

    if y == "quit":
        break

    else:
        try:
            if y == "remove":
                x.remove(t)
                print(f"Updated set: {x}")

            elif y == "add":
                for n in x:
                    if n == t:
                        print("Cannot add value to set as it already exists")
                x.add(t)
                print(f"The updated set is: {x}")

        except KeyError as e:
            print("cannot remove value as it does not exist in the set")


print(f"The set we started with is: {z}")
print(f"The new set is: {x}")
difference = x.symmetric_difference(z)
print(f"The difference between the two sets is: {difference}")


