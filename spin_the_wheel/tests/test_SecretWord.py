import pytest
from random import seed

from spin_the_wheel.words import SecretWord, InvalidLetter


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


class Test_get_word:
    def test_should_return_a_upper_cased_and_stripped_word(self):
        og_word = ' la casa de papel '
        sw = SecretWord(og_word)
        word = sw.get_word()

        assert word == og_word.upper().strip()


class Test_get_hidden_word:
    def test_should_return_the_word_as_a_list_with_valid_letters_replaced(self):
        og_word = 'Spider-Man 3: Venom'
        sw = SecretWord(og_word)
        hidden_word = sw.get_hidden_word()

        assert ' '.join(hidden_word) == '_ _ _ _ _ _ - _ _ _   _ :   _ _ _ _ _'


class Test_has_letter:
    def test_should_return_true_if_has_letter(self):
        og_word = 'abc def hij'
        sw = SecretWord(og_word)

        assert sw.has_letter('A')
        assert sw.has_letter('B')
        assert sw.has_letter('D')

    def test_should_return_false_if_doesnt_have_letter(self):
        og_word = 'abc def hij'
        sw = SecretWord(og_word)

        assert not sw.has_letter('K')
        assert not sw.has_letter('R')
        assert not sw.has_letter('M')

    def test_should_not_care_about_case_sensitive(self):
        og_word = 'abc def hij'
        sw = SecretWord(og_word)

        assert sw.has_letter('a')
        assert sw.has_letter('b')
        assert sw.has_letter('c')

    def test_should_raise_error_if_try_to_search_invalid_character(self):
        with pytest.raises(InvalidLetter):
            og_word = 'abc def hij'
            sw = SecretWord(og_word)

            assert sw.has_letter('-')