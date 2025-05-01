import sys
from stats import get_word_count, get_char_frequency, get_sorted_char_frequency

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: The path {filepath} is a directory, not a file.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file at {filepath}.")
        print(f"Details: {e}")
        sys.exit(1)

def main():
    if not sys.argv or len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Example: python3 main.py books/frankenstein.txt")
        sys.exit(1)
    
    print("============ BOOKBOT ============")

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_freq = get_char_frequency(text)
    sorted_char_freq = get_sorted_char_frequency(char_freq)
    for i in sorted_char_freq:
        print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")

main()
