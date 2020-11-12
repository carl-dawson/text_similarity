from collections import Counter
from math import sqrt

# This is a somewhat contrived list of stop words based on the words that appear in the
# sample text that might appear in a typical stopwords corpus
STOP_WORDS = [
    "a",
    "about",
    "after",
    "and",
    "any",
    "are",
    "do",
    "don't",
    "each",
    "for",
    "have",
    "if",
    "is",
    "it",
    "just",
    "more",
    "no",
    "not",
    "of",
    "on",
    "or",
    "out",
    "that",
    "the",
    "these",
    "to",
    "we",
    "which",
    "why",
    "will",
    "with",
    "you",
    "you'll",
    "your",
]
PUNCTUATION = ",.?()`-'\"!"


def compare_strings(str1, str2):
    """
    takes two strings as input and computes the cosine similarity between the vectorized strings
    result will be in the range [0,1]
    """
    bow_1 = string_to_bow(str1)
    bow_2 = string_to_bow(str2)

    word_set = set(bow_1.keys())
    word_set.update(bow_2.keys())

    vector_1 = [0] * len(word_set)
    vector_2 = [0] * len(word_set)
    for i, word in enumerate(word_set):
        vector_1[i] = bow_1[word]
        vector_2[i] = bow_2[word]
    return cos_similarity(vector_1, vector_2)


def string_to_bow(s):
    """
    splits a string into words, strips punctuation, ignores stop words
    returns a dictionary mapping each word to the number of occurrences
    """
    words = s.lower().split(" ")
    words = [word.strip(PUNCTUATION) for word in words]
    words = [word for word in words if word not in STOP_WORDS]
    bow = Counter(words)
    return bow


def cos_similarity(vector1, vector2):
    """
    Computes the cosine similarity between two vectors
    (𝐀∙𝐁)/(‖𝐀‖*‖𝐁‖)
    """
    a_dot_b = sum([a * b for a, b, in zip(vector1, vector2)])
    mag_a = sqrt(sum([a ** 2 for a in vector1]))
    mag_b = sqrt(sum([a ** 2 for a in vector2]))
    return a_dot_b / (mag_a * mag_b)
