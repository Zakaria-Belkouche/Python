import string

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""

s_lower = s.lower()

tbl = str.maketrans('', '', string.punctuation)

s_clean = s_lower.translate(tbl)

words = list(s_clean.split())

count = len(words)

print(words)

print(count)

set_words = set(words)

set_count = len(set_words)

print(set_count)

dict = {}

for i in words:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)



