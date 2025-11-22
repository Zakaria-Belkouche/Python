

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def bark(self):
        return f"Woof! My name is {self.name}"

    def birthday(self):
        self.age += 1
        return self.age
        


Dog1 = Dog("Markus", 6)

print(Dog1.bark())

print(Dog1.birthday())

print(Dog1.birthday())

