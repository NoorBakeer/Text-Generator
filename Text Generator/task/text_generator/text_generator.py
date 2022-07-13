import random

from nltk.tokenize import WhitespaceTokenizer

file_name = input()
tokens = list()
sentence = list()
trigrams = dict()

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        lst = WhitespaceTokenizer().tokenize(line)
        tokens.extend(lst)

for x in range(len(tokens) - 2):
    head = tokens[x] + " " + tokens[x + 1]
    tail = tokens[x + 2]
    trigrams.setdefault(head, dict())
    trigrams[head].setdefault(tail,
                              0)  # storing tails along with their frequencies
    trigrams[head][tail] += 1


def get_next_word(previous_word):
    head = trigrams[previous_word]
    word = random.choices(list(head.keys()),
                          list(head.values()))
    return word[0]


def valid_first_word(word):
    if word[0].isalpha() and word[0].isupper() and not (word[-1] in ".?!"):
        return True
    return False


def complete_sentence():
    return sentence[-1][-1] in "?.!"


heads = list(trigrams.keys())


def start_chain():
    first_words = random.choice(heads).split()
    while not valid_first_word(first_words[0]):
        first_words = random.choice(heads).split()
    sentence.extend(first_words)


def generate_sentences():
    i = 0
    while i < 10:
        start_chain()
        last_words = sentence[0] + " " + sentence[1]

        while not complete_sentence():
            next_word = get_next_word(last_words)
            last_words = sentence[-1] + " " + next_word
            sentence.append(next_word)

        if len(sentence) >= 5:
            print(' '.join(sentence))
            i += 1

        sentence.clear()


generate_sentences()
