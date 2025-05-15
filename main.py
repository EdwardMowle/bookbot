import sys

from stats import get_num_words
from stats import get_sorted_character_count

if (len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(book):
    text = get_book_text(book)
    word_count = get_num_words(text)
    character_count = get_sorted_character_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in character_count:
        if char.isalpha() and count > 0:
            print(f"{char}: {count}")
    print("============= END ==============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main(sys.argv[1])
