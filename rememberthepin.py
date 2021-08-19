from english_words import english_words_set

hashTable = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


# recrusive function
# base case: is when reached end of pin, print out word
# recursive case:


def printWordsUtil(master_list, number, curr, output, pin_len):
    if curr == pin_len:
        # print("DONE WORD")
        word = "".join(output)
        # print(word)
        master_list.append(word)
        return

    # Try all 3 possible characters
    # for current digir in number[]
    # and recur for remaining digits
    for i in range(len(hashTable[number[curr]])):
        # print(output)
        output.append(hashTable[number[curr]][i])
        printWordsUtil(master_list, number, curr + 1, output, pin_len)
        output.pop()


def printWords(a_pin):
    master_list = []
    number = [int(num) for num in str(a_pin)]
    pin_len = len(number)
    printWordsUtil(master_list, number, 0, [], pin_len)
    return master_list


def realWords(list_words):
    real_words = []
    for word in list_words:
        #print(word)
        if (word in english_words_set) is True:
            print(word)
            real_words.append(word)
    print("True Words Are")
    print(real_words)


pin = 4566
all_possible_words = printWords(pin)
print(all_possible_words)

realWords(all_possible_words)
