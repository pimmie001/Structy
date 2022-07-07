def substitute_synonyms(sentence, synonyms):
    list_of_words = sentence.split(' ')

    arrays = _substitute_synonyms(list_of_words, synonyms)

    final_result = []
    for array in arrays:
        final_result.append(' '.join(array))
    return [ ' '.join(subarray) for subarray in arrays ]



def _substitute_synonyms(words, synonyms):
    if len(words) == 0:
        return [[]]

    first = words[0]
    remainder = words[1:]

    subarrays = _substitute_synonyms(remainder, synonyms)

    result = []
    if first in synonyms:
        for synonym in synonyms[first]:
            result += [ [synonym, *subarray] for subarray in subarrays]
        return result

    return [ [first, *subarray] for subarray in subarrays ] 
