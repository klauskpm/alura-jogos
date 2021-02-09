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
