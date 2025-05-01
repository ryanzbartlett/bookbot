from typing import Dict, List

def get_word_count(text: str) -> int:
    """
    Count the number of words in a given text.
    """
    if not text:
        return 0

    return len(text.split())

def get_char_frequency(text: str) -> Dict[str, int]:
    """
    Count the frequency of each (case-insensitive) character in the text.
    """
    if not text:
        return {}

    count_dict = {}

    for char in text:
        char = char.lower()
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1

    return count_dict

def get_sorted_char_frequency(char_freq: Dict[str, int]) -> List[Dict[str, int]]:
    """
    Sort the character frequency dictionary by character in alphabetical order.
    """
    if not char_freq:
        return []

    char_list = []

    for char in char_freq:
        if not char.isalpha():
            continue
        char_list.append({
            "char": char,
            "num": char_freq[char]
        })

    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
