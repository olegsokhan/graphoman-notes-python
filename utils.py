class WordUtils:

    openAndCloseBrackets = [
        ['"', '"'],
        ['(', ')'],
        ['[', ']'],
        ['{', '}'],
        ['<', '>'],
        ['\'', '\'']
    ]

    specialCharacters = "!?.,;:"

    def __init__(self):
        self.uniqueWords = []

    def add_word_if_not_exists(self, word):
        if not self.is_word_exists_in_array(word):
            self.uniqueWords.append(word)

    def is_word_exists_in_array(self, word):
        for i in range(0, len(self.uniqueWords)):
            if self.uniqueWords[i] == word:
                return True
        return False

    def get_unique_words_with_filters_off(self, text):
        words = text.lower().split(" ")
        for i in range(0, len(words)):
            if len(words[i]) > 0:
                self.add_word_if_not_exists(words[i])
        return self.uniqueWords

    def get_unique_words_with_filters_on(self, text):
        words = text.lower().split(" ")
        for i in range(0, len(words)):
            word_length = len(words[i])
            if word_length > 1:
                for j in range(0, len(self.specialCharacters)):
                    if words[i][word_length - 1] == self.specialCharacters[j]:
                        words[i] = words[i][:-1]
                        word_length = word_length - 1
                        break
            if word_length > 2:
                word_in_brackets = False
                for j in range(0, len(self.openAndCloseBrackets)):
                    if self.openAndCloseBrackets[j][0] == words[i][0] \
                            and self.openAndCloseBrackets[j][1] == words[i][word_length - 1]:
                        word_in_brackets = True
                        self.add_word_if_not_exists(words[i][1:-1])
                        break
                if not word_in_brackets:
                    self.add_word_if_not_exists(words[i])
            elif word_length == 1:
                self.add_word_if_not_exists(words[i])
        return self.uniqueWords
