def lexical_order(word_1, word_2, alphabet):
    order = {}
    for i in range(len(alphabet)):
        order[alphabet[i]] = i


    for i in range(min(len(word_1), len(word_2))):
        letter1 = word_1[i]
        letter2 = word_2[i]

        if letter1 == letter2:
            return lexical_order(word_1[1:], word_2[1:], alphabet)
        elif order[letter1] > order[letter2]:
            return False
        return True

    return len(word_1) <= len(word_2)