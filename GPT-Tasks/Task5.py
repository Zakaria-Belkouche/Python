sentence = input("write out a sentance:     ")

x = sentence.split()

count = 0
words = 0

for n in x:
    for z in n:
        count += 1
    if count > 4:
        words += 1
    count = 0

print(words)
