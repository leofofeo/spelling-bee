from helpers import return_relevant_words
from words import words

if __name__ == "__main__":
    letters = input("Letters: ")
    key_letter = input("Key letter: ")
    letters_set = set(letters)
    
    result = return_relevant_words(letters_set, key_letter, words)
    sorted_result = sorted(result, key=len)
    for word in sorted_result:
        print(f"{word}")
