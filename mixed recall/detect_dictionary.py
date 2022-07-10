from lexical_order import lexical_order

def detect_dictionary(dictionary, alphabet):
    for i in range(len(dictionary)-1):
        word1 = dictionary[i]
        word2 = dictionary[i+1]
        if not lexical_order(word1, word2, alphabet):
            return False
    return True