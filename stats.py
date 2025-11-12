def get_book_words(book_text):
    """
    Splits the book text into individual words.

    Args:
        book_text (str): The content of the book as a single string.

    Returns:
        list: A list of words in the book.
    """

    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    """
    Counts the number of occurrences of each character in the book text.

    Args:
        book_text (str): The content of the book as a single string.

    Returns:
        dict: returns a dictionary with the count of each character.
    """
    lower_text = book_text.lower()
    book_set = set(lower_text)
    return  {char: lower_text.count(char) for char in book_set}

def sort_on(num):
    return num["count"]

def char_report(char_dict):
    """
    Generates a report of character counts from the provided dictionary.

    Args:
        char_dict (dict): A dictionary with characters as keys and their counts as values.

    Returns:
        list: Returns a sorted list of dictionaries, each containing a character and its count.
    """
    report = []
    for char, count in char_dict.items():
        if char.isalpha():
            report.append({"character": char, "count": count})
    return sorted(report, key=sort_on, reverse=True)