import functools
hashTable = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def right_word(pin_and_letters, a_word):
    pin_iter = pin_and_letters[0]
    letters = pin_and_letters[1]
    mod_aword = a_word[pin_iter:]
    if any(mod_aword.startswith(letter) for letter in letters):
        return True
    else:
        return False


def filter_out_list(pin_iter, number, all_words):
    func = functools.partial(right_word, [pin_iter, hashTable[number]])
    return list(filter(func, all_words))
