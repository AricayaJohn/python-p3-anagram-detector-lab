# your code goes here

class Anagram:
    def __init__(self, word):
        self.word = sorted(word.lower())

    def match(self, word_list):
        matches = []

        for term in word_list:
            if sorted(term.lower()) == self.word:
                matches.append(term)

        return matches