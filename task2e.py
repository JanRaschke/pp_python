from typing import List, Tuple

def longest_words(words: List[str], n: int) -> List[Tuple[str, int]]:  # 1 Punkt
    word_lengths = word_lengths_list_comprehension(words)
    unique_word_lengths = list(set(word_lengths))

    sorted_words = sorted(unique_word_lengths, key=lambda x: x[1], reverse=True)
    
    return sorted_words[:n]

n = 10
print(f"{n} longest words:")
print(longest_words(words, n))