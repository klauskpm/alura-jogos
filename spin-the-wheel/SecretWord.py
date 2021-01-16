from helpers import normalize, map_positions


class SecretWord:
    __PLACEHOLDER_LETTER = '_'

    def __init__(self, word):
        self._secret_word = normalize(word)
        self._hidden_word = [SecretWord.__PLACEHOLDER_LETTER for _ in self._secret_word]
        self._letter_positions_dict = map_positions(self._secret_word)

    def get_word(self):
        return self._secret_word

    def get_hidden_word(self):
        return self._hidden_word

    def guess_letter(self, letter):
        if not self.has_letter(letter):
            return

        indexes = self._letter_positions_dict[letter]
        for i in indexes:
            self._hidden_word[i] = letter

    def has_letter(self, letter):
        return letter in self._letter_positions_dict

    def get_letter_count(self, letter):
        if not self.has_letter(letter):
            return 0

        indexes = self._letter_positions_dict[letter]
        return len(indexes)

    def has_guessed_word(self):
        return SecretWord.__PLACEHOLDER_LETTER not in self._hidden_word

