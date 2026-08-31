def read_file(filepath: str) -> str:  # 0,5 Punkte
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

text = read_file(filepath)

def count_word_occurrences(text: str, word: str) -> int:  # 0,5 Punkte
    return text.count(word)

word = "Informatik"
print(f"The word \"{word}\" occurs {count_word_occurrences(text, word)} times.")