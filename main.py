import sys
from stats import get_word_count, get_char_count, get_dict_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    frankenstein_book = get_book_text(filepath)
    # print(frankenstein_book)
    frankenstein_word_count = get_word_count(frankenstein_book)
    # print(f"{frankenstein_word_count} words found in the document")
    frankenstein_char_count = get_char_count(frankenstein_book)
    # print(frankenstein_char_count)
    frankenstein_book_report = get_dict_report(frankenstein_char_count)
    # print(frankenstein_book_report)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")
    for char_dict in frankenstein_book_report:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
        print()
    print("============= END ===============")



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

main()