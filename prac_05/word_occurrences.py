def count_words(text):
    word_counts = {}
    words = text.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def main():
    text = input("Text: ")
    word_counts = count_words(text)

    max_word_length = max(len(word) for word in word_counts.keys())

    for word, count in sorted(word_counts.items()):
        print(f"{word:>{max_word_length}} : {count}")

if __name__ == "__main__":
    main()