import json

hashTable = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def read_txt(file):
    list_words = []
    file1 = open(file, 'r')
    while True:
        word = file1.readline()
        if not word:
            break
        list_words.append(word.strip())
    return list_words


def construct_markov_chain(word_list, char_count=2):
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


def save_markov(markov_chain_dict):
    markov_file = open("markov_dict.json", "w")
    json.dump(markov_chain_dict, markov_file)
    markov_file.close()


def call_markov():
    markov_file = open("markov_dict.json", "r")
    markov_dict = json.load(markov_file)
    return markov_dict


all_words = read_txt("all_words.txt")
mark_chain = construct_markov_chain(all_words, 2)
save_markov(mark_chain)

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
