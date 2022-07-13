import random

from nltk.tokenize import WhitespaceTokenizer

file_name = input()
tokens = list()
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        lst = WhitespaceTokenizer().tokenize(line)
        tokens.extend(lst)

trigrams = dict()
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


sentence = list()


def valid_first_word(word):
    if word[0].isalpha() and word[0].isupper() and not (
            word.endswith('.') or word.endswith('!') or
            word.endswith('?')):
        return True
    return False


def valid_sentence():
    if len(sentence) < 5 and (
            sentence[-1].endswith('.') or sentence[-1].endswith('!') or
            sentence[
                -1].endswith('?')):
        return False
    return True


def complete_sentence():
    if sentence[-1].endswith('.') or sentence[-1].endswith('!') or sentence[
        -1].endswith('?') and len(sentence) >= 5:
        return True
    return False


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
        previous_words = sentence[0] + " " + sentence[1]

        while not complete_sentence():
            if not valid_sentence():
                break
            next_word = get_next_word(previous_words)
            previous_words = sentence[-1] + " " + next_word
            sentence.append(next_word)

        if valid_sentence():
            print(' '.join(sentence))
            i += 1

        sentence.clear()


generate_sentences()
