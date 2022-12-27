def return_relevant_words(letters_set, key_letter, words):
    words = words.splitlines()
    words = [word.strip() for word in words if key_letter in word]
    words_sets = {word: set(word) for word in words if len(word) > 3 }
    relevant_words = []
    for word, word_set in words_sets.items():
        if word_set == letters_set or word_set.issubset(letters_set):
            relevant_words.append(word)
    return relevant_words
