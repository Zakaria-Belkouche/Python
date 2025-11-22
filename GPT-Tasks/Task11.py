class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"Woof! I'm {self.name}")

    def birthday(self):
        self.age += 1
        return self.age

    def info(self):
        print(f"Name: {self.name}, age: {self.age}, breed: {self.breed}")

class Owner:
    def __init__(self, name):
        self.name = name
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)

    def print_dogs(self):
        print(f"{self.name} owns these dogs: {self.dogs}")

#    def oldest_dog(self):
#        for n in 

dog1 = Dog("mark", 3, "pitbull")
dog2 = Dog("luke", 5, "poodle")
dog3 = Dog("lucy", 4, "Belgian Malinoua")
dog4 = Dog("Chris", 6, "German Shepeard")
dog5 = Dog("Danny", 2, "Bully")

owner1 = Owner("Harry")

owner1.add_dog(dog1)
owner1.add_dog(dog2)
owner1.add_dog(dog3)

print(owner1.print_dogs())

