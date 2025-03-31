
def main():
    frankenstein_book = get_book_text("./books/frankenstein.txt")
    print(frankenstein_book)
    frankenstein_word_count = get_word_count(frankenstein_book)
    print(f"{frankenstein_word_count} words found in the document")
    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

def get_word_count(booktext):
    w = booktext.split()
    word_count = len(w)

    return word_count



main()