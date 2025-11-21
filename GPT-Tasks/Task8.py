import string

sentence = input("write out a sentence:      ").lower()

table = str.maketrans("", "", string.punctuation)

clean_sentence = sentence.translate(table)

words = clean_sentence.split()

print(words)

x = lambda words: words[:3]
y = lambda words: words[-3:]
z = lambda words: words[1::2]
r = lambda words: words[::-1]
m = lambda words: words[2:-2]


print(f"the first 3 words are {x(words)}")
print(f"the last 3 words are {y(words)}")
print(f"Every second word is {z(words)}")
print(f"the sentence reversed is {r(words)}")
print(f"the middle section is {m(words)}")

