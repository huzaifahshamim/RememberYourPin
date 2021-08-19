# keep 63% of pins for 4 digit pin
import functools

hashTable = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def read_txt(file):
    list_words = []
    file1 = open(file, 'r')
    while True:
        word = file1.readline()
        if not word:
            break
        list_words.append(word.strip())


def construct_markov_chain(word_list, char_count):
    markov_chain = {}
    for word in word_list:
        if len(word) <= char_count:
            continue
        for i in range(0, len(word) - char_count):
            start_state = word[i:i + char_count]
            transition_state = word[i + char_count]
            if start_state not in markov_chain:
                markov_chain[start_state] = {}
            if transition_state not in markov_chain[start_state].keys():
                markov_chain[start_state][transition_state] = 1
            else:
                markov_chain[start_state][transition_state] += 1
    return markov_chain


all_words = read_txt("all_words.txt")


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


word_list = []
read_txt("all_words.txt", word_list)

# print(word_list)
# print(len(word_list))
# updated_word_list = filter_out_list(0, 2, word_list)
# print(updated_word_list)
# updated_word_list2 = filter_out_list(1, 3, updated_word_list)
# print(updated_word_list2)
# updated_word_list3 = filter_out_list(2, 5, updated_word_list2)
# print(updated_word_list3)
# updated_word_list4 = filter_out_list(3, 2, updated_word_list3)
# print(updated_word_list4)