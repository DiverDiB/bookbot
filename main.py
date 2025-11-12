from stats import get_book_words, get_char_count, char_report
import sys

def get_book_text(file_path):
    """
    Reads the content of a book from a text file.

    Args:
        file_path (str): The path to the text file containing the book.

    Returns:
        str: The content of the book as a single string.
    """

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(f"Reading book from {book_path}...")
    book_text = get_book_text(book_path)

    word_count = get_book_words(book_text)

    char_dict = get_char_count(book_text)

    report = char_report(char_dict)
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words\n")
    print("--------- Character Count --------")
    for item in report:
        print(f"{item['character']}: {item['count']}")
    return


if __name__ == "__main__":
    main()