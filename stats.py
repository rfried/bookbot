   
def count_words(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: The number of words in the text.
    """
    return len(text.split())

def count_chars(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: The number of words in the text.
    """
    char_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_char_counts(char_dict):
    """
    Sorts the character counts in descending order.
    
    :param char_dict: Dictionary of character counts.
    :return: Sorted list of tuples (character, count).
    """
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)