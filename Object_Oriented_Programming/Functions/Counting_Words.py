# Zakaria Belkouche 25/10/25

import string

x = input("Write a string of text:      ").lower()

table = str.maketrans('', '', string.punctuation)

x_clean = x.translate(table)

x_list = list(x_clean.split())

x_set = set(x_list)

count_words = len(x_list)

count_distinct_words = len(x_set)

dict = {}

for i in x_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(f"Here is a dictionary of all words used and their occurances")
print(f"{dict}")


