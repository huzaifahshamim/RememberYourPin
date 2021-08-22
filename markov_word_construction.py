import functools
import random

from markov_chain import call_markov
from rememberthepin import *

hashTable = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def word_construction(list_substr, markov_chain, pin):
    i = 0
    new_words = []
    og_len_substr = len(list_substr[0])  # current length of substrings in list_ubstr
    while len(list_substr) != 0:
        print("iter is", i)
        print("list substr", list_substr)
        print("pin", pin)
        curr_substr = list_substr[i % len(list_substr)]  # grab a substring
        print("the current substring", curr_substr)
        if len(curr_substr) == len(pin):  # if substring is the same length as the pin
            print("CORRECT LENGTH")
            new_words.append(curr_substr)
            list_substr.remove(curr_substr)
            print("created words so far", new_words)
        else:
            curr_pin = int(pin[len(curr_substr)])  # check the next pin that needs to be added to that substring
            print("pin needed ot be added", curr_pin)
            letters_of_pin = hashTable[curr_pin]  # get possible letters of next pin
            print("possible letters to add on", letters_of_pin)
            start_substr_substr = len(curr_substr) - og_len_substr  # get start point of substring of substring
            end_substr_substr = len(curr_substr)  # get endpoint of substring of substring
            substr_substr = curr_substr[start_substr_substr:end_substr_substr]  # grab substring of subtring
            print("substring we are adding onto is", substr_substr)
            if substr_substr in markov_chain.keys() and \
                    len(set(letters_of_pin).intersection(markov_chain[substr_substr])) != 0:
                next_let_poss = set(letters_of_pin).intersection(markov_chain[substr_substr])  # whats the nxt letter
                print("next possible letters for this substring are", markov_chain[substr_substr])
                print("given pin, next possible letters for this substrings are", next_let_poss)
                next_letter = grab_next_state(substr_substr, markov_chain, curr_pin)  # helper to find next letter
                new_substr = add_next_state(curr_substr, next_letter)  # helper to add next letter
                list_substr[i % len(list_substr)] = new_substr
            else:
                print("NOT IN and removed", curr_substr)
                list_substr.remove(curr_substr)
        print(list_substr)
        i += 1
        print('-------------------------------------------------------------')


def grab_next_state(substr, markov_chain, pin_to_add):
    """
    Given a substring, a markov dict, and the pin to add,
    grab the next letter that needs to be added to the substring
    :param substr: Substring we are adding on to
    :param markov_chain: Dictionary where key is substring, and value is possible next letters
    :param pin_to_add: the pin whose letter needs to be added
    :return: the letter we plan on adding to substr
    """
    letters_for_next_state = list(hashTable[pin_to_add])
    transition_state_dict = markov_chain[substr]
    mod_transition_state = {}
    for letter in letters_for_next_state:
        if letter in transition_state_dict.keys():
            mod_transition_state[letter] = transition_state_dict[letter]
    print("modded transition state", mod_transition_state)
    sum_trstate = sum(mod_transition_state.values())
    rnd = random.random() * sum_trstate
    for next_letter, weight in mod_transition_state.items():
        rnd -= weight
        if rnd <= 0:
            return next_letter


def add_next_state(curr_substr, next_letter):
    substr_lst = list(curr_substr)
    substr_lst.append(next_letter)
    return "".join(substr_lst)


pin = input("Please enter your Pin: ")
substring = printWords(pin)
print(substring)
markov_dict = call_markov()
print(markov_dict)
word_construction(substring, markov_dict, pin)