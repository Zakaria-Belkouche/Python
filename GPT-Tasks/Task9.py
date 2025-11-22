import string

x = input("enter a filename:     ")

with open(x, "r") as file:
    contents = file.read()

lowercase = contents.lower()

table = str.maketrans("", "", string.punctuation)

cleaned = lowercase.translate(table)

y = cleaned.split()

totalCount = 0

for n in y:
    totalCount += 1

count = {}

for word in y:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

pairs = list(count.items())
sorted_counts = sorted(pairs, key=lambda x: x[1], reverse=True)

print(f"the total number of words is {totalCount}")
print(f"the first 10 words are {y[:10]}")
print(f"the last 10 words are {y[-10:]}")
print(f"the most frequent 5 words are {sorted_counts[:5]}")
print(f"the text reversed it: {y[::-1]}")



