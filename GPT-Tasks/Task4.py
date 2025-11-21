x = input("input a word:            ")

y = list(x)

number = 0
vowels = ("a", "e", "i", "o", "u")


for n in y:
    if n in vowels:
        number += 1

print(number)



