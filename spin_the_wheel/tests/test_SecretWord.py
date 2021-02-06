from random import seed

from spin_the_wheel.words import SecretWord


class Test__get_random_secret_word:
    def test_should_use_default_file_if_none_is_passed(self):
        seed(3)
        word = SecretWord._get_random_secret_word()
        assert word == 'Astro Bot'
