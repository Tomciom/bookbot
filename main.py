import sys
from stats import get_char_count, sort_dict, get_num_words

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    char_dict = get_char_count(book_path)
    sorted_dict = sort_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_path)} total words")
    print("--------- Character Count -------")

    for entry in sorted_dict:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()