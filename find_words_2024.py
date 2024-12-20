# julknäcket 2024 - FRA
from itertools  import product

# The columns with letters given by the assignement
columns = [
    ['s','a','k','b','u'],
    ['s','i','a','k','t'],
    ['l','r','o','e','t'],
    ['a','l','n','k','r'],
]

# print(columns)

# Generera alla lösningar av bokstäver, go lambda
possible_words = ["".join(word) for word in product(*columns)]

# Print and check
# print(possible_words) # Unsorted combiantions from columns
# print(len(possible_words))  # Cardinality of posibilitys(5**4)

# Sort the word, I just whant to look at them in order
sorted_words = sorted(possible_words)
# print(sorted_words)

# read words from list, set all to lower 
with open ("swe_wordlist.txt", encoding="utf-8") as f:
    swedish_words =set(word.strip().lower() for word in f)

# check for matching words
valid_words = sorted (word for word in possible_words if word in swedish_words)

# Print the words that av valid
for word in valid_words:
    print(word)