import os
from random import randrange
from re import match
from collections import defaultdict

from spin_the_wheel.helpers import normalize

# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))


class SecretWord:
    __PLACEHOLDER_LETTER = '_'
    __VALID_LETTERS_PATTERN = '[a-zA-Z0-9]'
    __DEFAULT_FILE_PATH = f'{absolute_path}/assets/video_games.txt'

    def __init__(self, word: str = None):
        if not word:
            word = SecretWord._get_random_secret_word()

        self._secret_word = normalize(word)
        self._hidden_word = self._create_hidden_word()
        self._letter_positions_dict = self._map_positions(self._secret_word)
        self.was_guessed = False

    @staticmethod
    def _get_random_secret_word(file_path=None):
        if not file_path:
            file_path = SecretWord.__DEFAULT_FILE_PATH

        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line for line in file]

        random_word = words[randrange(0, len(words))]
        return random_word.strip()

    @staticmethod
    def _is_letter_valid(letter):
        return match(SecretWord.__VALID_LETTERS_PATTERN, letter)

    def _map_positions(self, word):
        positions_dict = defaultdict(list)

        for i in range(len(word)):
            letter = word[i]
            if self._is_letter_valid(letter):
                positions_dict[letter].append(i)

        return positions_dict

    def _create_hidden_word(self):
        hidden_word = []
        for letter in self._secret_word:
            if self._is_letter_valid(letter):
                hidden_word.append(SecretWord.__PLACEHOLDER_LETTER)
            else:
                hidden_word.append(letter)
        return hidden_word

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

        self.was_guessed = SecretWord.__PLACEHOLDER_LETTER not in self._hidden_word

    def has_letter(self, letter):
        return letter in self._letter_positions_dict

    def get_letter_count(self, letter):
        if not self.has_letter(letter):
            return 0

        indexes = self._letter_positions_dict[letter]
        return len(indexes)

