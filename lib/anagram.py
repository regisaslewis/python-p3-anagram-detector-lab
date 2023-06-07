class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        w_one = sorted([l for l in self.word])
        matches_list = []
        for word in list:
            w_two = sorted([l for l in word])
            if w_one == w_two:
                matches_list.append(word)
        return matches_list