from english_words import english_words_set

hashTable = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


# recrusive function
# base case: is when reached end of pin, print out word
# recursive case:


def printWordsUtil(master_list, og_pin, str_pin, curr, output, pin_len=2):
    if curr == pin_len:
        # print("DONE WORD")
        word = "".join(output)
        # print(word)
        master_list.append(word)
        return

    # Try all 3 possible characters
    # for current digir in number[]
    # and recur for remaining digits
    for i in range(len(hashTable[str_pin[curr]])):
        # print(output)
        output.append(hashTable[str_pin[curr]][i])
        printWordsUtil(master_list, og_pin, str_pin, curr + 1, output, pin_len)
        output.pop()


def printWords(a_pin):
    master_list = []
    number = [int(num) for num in str(a_pin)]
    pin_len = len(number)
    printWordsUtil(master_list, a_pin, number, 0, [])
    return master_list


def realWords(list_words):
    real_words = []
    for word in list_words:
        # print(word)
        if (word in english_words_set) is True:
            print(word)
            real_words.append(word)
    print("True Words Are")
    print(real_words)


pin = input("Please enter your Pin: ")
all_possible_words = printWords(pin)
print(all_possible_words)

realWords(all_possible_words)
