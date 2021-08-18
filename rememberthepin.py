hashTable = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]



# recrusive function
# base case: is when reached end of pin, print out word
# recursive case:


def printWordsUtil(master_list, number, curr, output, pin_len):
    if curr == pin_len:
        #print("DONE WORD")
        word = "".join(output)
        print(word)
        return

    # Try all 3 possible characters
    # for current digir in number[]
    # and recur for remaining digits
    for i in range(len(hashTable[number[curr]])):
        #print(output)
        output.append(hashTable[number[curr]][i])
        printWordsUtil(master_list, number, curr + 1, output, pin_len)
        output.pop()


def printWords(pin):
    master_list = []
    number = [int(num) for num in str(pin)]
    pin_len = len(number)
    printWordsUtil(master_list, number, 0, [], pin_len)
    print(master_list)


pin = 234
printWords(pin)
