# split text into individual words
words = text.split()

from typing import List, Tuple

# imperative approach (for loop)
def word_lengths_imperative(words: List[str]) -> List[Tuple[str, int]]:  # 1 Punkt
    result = []
    for word in words:
        result.append((word, len(word)))
    return result

print("Word lengths (imperative):")
print(word_lengths_imperative(words)[:10])

# functional approach (map)
def word_lengths_functional(words: List[str]) -> List[Tuple[str, int]]:  # 1 Punkt
    return list(map(lambda word: (word, len(word)), words))

print("\nWord lengths (functional):")
print(word_lengths_functional(words)[:10])

# list comprehension
def word_lengths_list_comprehension(words: List[str]) -> List[Tuple[str, int]]:  # 1 Punkt
    return [(word, len(word)) for word in words]

print("\nWord lengths (list comprehension):")
print(word_lengths_list_comprehension(words)[:10])