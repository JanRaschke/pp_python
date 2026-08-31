import re
from typing import List

def get_words(text: str) -> List[str]:  # 2 Punkte
    return re.findall(r'\w+', text)

words2 = get_words(text)
n = 10

print(f"{n} longest words (improved):")
print(longest_words(words2, n))