# We want to know the index of the vowels in a given word, for example, there are two vowels in the 
# word super (the second and fourth letters).
# So given a string "super", we should return a list of [2, 4].
# NOTE: Vowels in this context refers to English Language Vowels - a e i o u y
# NOTE: this is indexed from [1..n] (not zero indexed!)

def vowel_indices(word):
    result = []
    for index, vowel in enumerate(word):
        if vowel.lower() in 'aeiouy':
            result.append(index+1)
    return result
