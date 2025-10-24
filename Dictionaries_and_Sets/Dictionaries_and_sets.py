x = {1, 2, 3, 4, 5, 6, 7, 8, 9}

try:
    t = int(input("pick a random integer:               ")) 

    y = input("choose an operation: add or remove or quit to stop      ").lower()

    if y not in ("add", "remove", "quit"):
        raise Exception

except Exception as e:
    print("please input a valid integer and the correct string")

else:
    while y != "quit":
        try:
            if y == "remove":
                x.remove(t)
                print(x)

            elif y == "add":
                duplicate_found = False

                for n in x:
                    if n == t:
                        print("That value already exists in the set, so will not be added")
                        duplicate_found = True
                        break
                
                if not duplicate_found:
                    x.add(t)
                    print(x)


        except KeyError as e:
            print(f"The integer {e} doesn't exist in the set, so we cannot remove it")




