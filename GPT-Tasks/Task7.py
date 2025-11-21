import string

sentence = input("write out a sentence, or even a paragraph:     ").lower()

table = str.maketrans("", "", string.punctuation)

cleaned_sentence = sentence.translate(table)

words = cleaned_sentence.split()

counts = {}

for n in words:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

pairs = list(counts.items())

sorted_counts = sorted(pairs, key=lambda x: x[1], reverse=True)

print(sorted_counts)


