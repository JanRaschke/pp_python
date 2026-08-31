from typing import List, Tuple

def find_most_frequent_words(text: str, n: int, min_len: int = 1) -> List[Tuple[str, int]]:
    text = text.lower()
    
    for char in '.,;:!?()[]{}"\'-':
        text = text.replace(char, ' ')
        
    words = text.split()
    counts = {}
    
    for word in words:
        if len(word) >= min_len:
            counts[word] = counts.get(word, 0) + 1
            
    sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_words[:n]

print("Most frequent words:")
print(find_most_frequent_words(text, n=10, min_len=4))