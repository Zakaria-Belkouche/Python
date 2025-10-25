#Zakaria Belkouche 25/10/25

print("write quit to exit the program")

acceptable = ("add", "subtract", "multiply", "divide", "quit")

while True:
    try:
        x = input("input an integer:        ")
        if x == "quit":
            print("stopping programme")
            break

        y = input("input another integer:   ")
        if y == "quit":
            print("stopping programme")
            break
        
        z = input("Select:  add     subtract    multiply    divide    quit:   ").lower()
        if z == "quit":
            print("stopping programme")
            break
    
    except Exception as e:
        print(f"Please input acceptable values...   {e}")

    if z not in acceptable:
        print("Please input correct values. Try again:          ")

    class SimpleCalculator:
        def __init__ (self, x, y):
            self.x = x
            self.y = y

        def addition(self):
            return self.x + self.y

        def subtraction(self):
            return self.x - self.y

        def multiplication(self):
            return self.x * self.y

        def division(self):
            return self.x / self.y


    try:
        calc = SimpleCalculator(int(x), int(y))

    except Exception as e:
        print("Make sure you input a valid integer")
        continue

    if z == "add":
        print(f"The answer is: {calc.addition()}")
    elif z == "subtract":
        print(f"The answer is: {calc.subtraction()}")
    elif z == "multiply":
        print(f"The answer is: {calc.multiplication()}")
    elif z == "divide":
        print(f"The answer is: {calc.division()}")

    print("Go again!")


