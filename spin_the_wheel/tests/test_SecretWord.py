import pytest
from random import seed

from spin_the_wheel.words import SecretWord


@pytest.fixture(scope='module')
def path_to_words():
    return '../words/assets'


class Test__get_random_secret_word:
    def test_should_use_default_file_if_none_is_passed(self):
        seed(3)
        word = SecretWord._get_random_secret_word()
        assert word == 'Astro Bot'

    def test_should_get_random_word_from_selected_file(self, path_to_words):
        file = f'{path_to_words}/fruits.txt'
        seed(3)
        word = SecretWord._get_random_secret_word(file)
        assert word == 'banana'


class Test__is_letter_valid:
    def test_should_return_true_for_word_or_letter(self):
        from_upper_letter = SecretWord._is_letter_valid('A')
        from_lower_letter = SecretWord._is_letter_valid('a')
        from_number = SecretWord._is_letter_valid('1')

        assert from_upper_letter
        assert from_lower_letter
        assert from_number

    def test_should_return_false_(self):
        from_underscore = SecretWord._is_letter_valid('_')
        from_dash = SecretWord._is_letter_valid('-')
        from_exclamation = SecretWord._is_letter_valid('!')
        from_space = SecretWord._is_letter_valid(' ')

        assert not from_underscore
        assert not from_dash
        assert not from_exclamation
        assert not from_space


class Test__map_positions:
    def test_should_only_map_valid_letters(self):
        sw = SecretWord('Spider-Man 3: Venom')
        mapped_positions = sw._map_positions()

        assert len(mapped_positions['E']) == 2
        assert len(mapped_positions['S']) == 1
        assert len(mapped_positions['3']) == 1
        assert len(mapped_positions[' ']) == 0
        assert len(mapped_positions['-']) == 0
        assert len(mapped_positions[':']) == 0

    def test_should_map_letters_with_and_without_accentuation_as_the_same(self):
        sw = SecretWord('Sabão em pó')
        mapped_positions = sw._map_positions()

        print('space', mapped_positions)

        assert len(mapped_positions['A']) == 2
        assert len(mapped_positions['O']) == 2
        assert len(mapped_positions['S']) == 1
        assert len(mapped_positions['B']) == 1
