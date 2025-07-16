import sys
from stats import count_words, count_chars, sort_char_counts

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    :param filepath: Path to the book file.
    :return: Content of the book file as a string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {filepath} does not exist.")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""
    
def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Example path, adjust as necessary
    book_text = get_book_text(book_path)
    
    if book_text:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        word_count = count_words(book_text)
        print(f"Found {word_count} total words")        
        print("--------- Character Count -------")
        char_count = count_chars(book_text)
        sorted_char_counts = sort_char_counts(char_count)
        for c in sorted_char_counts:
            print(f"{c[0]}: {c[1]}")
        print("============= END ===============")
        # Further processing of book_text can be done here
    else:
        print("Failed to retrieve book content.")

main()