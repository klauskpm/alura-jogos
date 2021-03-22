import os
from random import randrange
from re import match
from collections import defaultdict
import unidecode

from .exceptions import InvalidLetter, HasGuessedLetterBefore, NothingLeftToGuess, RequiredField

# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))


class SecretWord:
    __PLACEHOLDER_LETTER = '_'
    __VALID_LETTERS_PATTERN = '[a-zA-Z0-9]'
    __VALID_VOWELS_PATTERN = '[aeiouAEIOU]'

    def __init__(self, theme: str = None, word: str = None):
        if not word and not theme:
            raise RequiredField('Você deve passa um tema ou uma palavra')

        if not word:
            word = SecretWord._get_random_secret_word(theme)

        self._secret_word = word.strip().upper()
        self._hidden_word = self._create_hidden_word()
        self._letter_positions_dict = self._map_positions()
        self._previously_guessed_letters = []
        self.was_guessed = False

    @property
    def previously_guessed_letters(self):
        return self._previously_guessed_letters

    @staticmethod
    def _get_random_secret_word(theme):
        file_path = f'{absolute_path}/assets/{theme}.txt'

        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line for line in file]

        random_word = words[randrange(0, len(words))]
        return random_word.strip()

    @staticmethod
    def _is_letter_valid(letter: str):
        letter = SecretWord._normalize_letter(letter)
        return bool(match(SecretWord.__VALID_LETTERS_PATTERN, letter))

    @staticmethod
    def _normalize_letter(letter: str):
        letter = letter.strip()
        is_word = len(letter) > 1
        if is_word:
            letter = letter[0]

        return unidecode.unidecode(letter).upper()

    def _map_positions(self):
        positions_dict = defaultdict(list)
        normalized_word = unidecode.unidecode(self._secret_word)

        for i in range(len(normalized_word)):
            letter = normalized_word[i]
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

    def reveal_vowel(self, letter: str):
        letter = SecretWord._normalize_letter(letter)

        is_vowel = bool(match(SecretWord.__VALID_VOWELS_PATTERN, letter))
        if not is_vowel:
            raise InvalidLetter('Você deveria chutar uma vogal')

        return self.reveal_letter(letter)

    def reveal_consonant_or_number(self, letter: str):
        letter = SecretWord._normalize_letter(letter)

        is_vowel = bool(match(SecretWord.__VALID_VOWELS_PATTERN, letter))
        if is_vowel:
            raise InvalidLetter('Você deveria chutar uma consoante ou número')

        return self.reveal_letter(letter)

    def reveal_letter(self, letter: str):
        letter = SecretWord._normalize_letter(letter)

        self._check_if_word_was_guessed()
        self._check_if_letter_is_valid(letter)
        self._check_if_letter_was_guessed_before(letter)

        self._previously_guessed_letters.append(letter)

        if not self.has_letter(letter):
            return False

        indexes = self._letter_positions_dict[letter]
        for i in indexes:
            self._hidden_word[i] = self._secret_word[i]

        self._letter_positions_dict.pop(letter)
        self.was_guessed = SecretWord.__PLACEHOLDER_LETTER not in self._hidden_word

        return True

    def _check_if_letter_was_guessed_before(self, letter):
        has_guessed_letter_before = letter in self._previously_guessed_letters
        if has_guessed_letter_before:
            raise HasGuessedLetterBefore(f'A letra \'{letter}\' já foi chutada anteriormente')

    def _check_if_letter_is_valid(self, letter):
        if not self._is_letter_valid(letter):
            raise InvalidLetter(f'\'{letter}\' não é uma letra válida')

    def _check_if_word_was_guessed(self):
        if self.was_guessed:
            raise NothingLeftToGuess('Não tem mais nada para ser adivinhado')

    def has_letter(self, letter: str):
        letter = SecretWord._normalize_letter(letter)

        return letter in self._letter_positions_dict

    def get_letter_count(self, letter: str):
        letter = self._normalize_letter(letter)

        indexes = self._letter_positions_dict.get(letter, [])
        return len(indexes)
