from random import randint

from jogos.helpers import map_positions, normalize, sleep, clear


class Forca:
    _won: bool
    _lost: bool
    _tries: int
    _guessed_letters: list
    _mapped_word_positions: dict
    _hidden_word: list

    PLACEHOLDER_LETTER = '_'

    def __init__(self):
        self._secret_word: str = ''
        self._gallows_draw: list = []
        with open('defeat_message.txt', 'r') as defeat_file:
            self._defeat_message = [line for line in defeat_file]
            self._defeat_message = ''.join(self._defeat_message)

        with open('victory_message.txt', 'r') as victory_file:
            self._victory_message = [line for line in victory_file]
            self._victory_message = ''.join(self._victory_message)



    def start_new_game(self):
        self._reset_states()
        self._print_opening_message()

        while(not self._won and not self._lost):
            self._next_round()

        self._end_game()

    @property
    def secret_word(self):
        return self._secret_word

    @secret_word.setter
    def secret_word(self, secret_word):
        secret_word = normalize(secret_word)
        self._mapped_word_positions = map_positions(secret_word)
        self._hidden_word = [Forca.PLACEHOLDER_LETTER for _ in secret_word]
        self._secret_word = secret_word

    def _reset_states(self):
        self._won = False
        self._lost = False
        self._tries = 7
        self._guessed_letters = []
        self._gallows_draw = [
            "  _______     ",
            " |/      |    ",
            " |            ",
            " |            ",
            " |            ",
            " |            ",
            " |            ",
            "_|___         ",
            ""
        ]
        self.set_random_secret_word()

    def set_random_secret_word(self):
        self.secret_word = self.get_random_secret_word()

    def get_random_secret_word(self, file_path='fruits.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line for line in file]

        return words[randint(0, len(words) - 1)]

    def _print_opening_message(self):
        clear()
        print('***************************')
        print("Bem vindo ao jogo da Forca!")
        print("***************************")
        sleep(0.5)
        print()
        input("Aperte enter para começar")

    def _next_round(self):
        self.print_round_start_message()
        guess, guessed_before = self.input_guess()

        if (guessed_before):
            return

        self.check_guess(guess)

        self._won = Forca.PLACEHOLDER_LETTER not in self._hidden_word
        self._lost = self._tries <= 0

    def _end_game(self):
        clear()
        if (self._won):
            self._print_victory_message()
        elif (self._lost):
            self._print_defeat_message()

    def print_round_start_message(self):
        clear()
        print('A palavra secreta é:')
        print(' '.join(self._hidden_word))
        print()
        print(f"Você tem {self._tries} tentativas.")
        print()
        self._draw_gallows()
        print()

    def input_guess(self):
        guess = input("Chute uma letra: ")
        guess = normalize(guess)
        guessed_before = guess in self._guessed_letters

        if (not guessed_before):
            print(f"Você chutou '{guess}'")
            self._guessed_letters.append(guess)
            sleep(0.6)
        else:
            print(f"A letra '{guess}' já foi chutada anteriormente")
            sleep(2)

        return guess, guessed_before

    def check_guess(self, guess):
        if (guess in self._mapped_word_positions):
            indexes = self._mapped_word_positions[guess]
            letter_count = len(indexes)
            print(f"Tem {letter_count} letras '{guess}'")

            for i in indexes:
                self._hidden_word[i] = guess
        else:
            print("Não foi dessa vez.")
            self._tries -= 1

        sleep(2)

    def _print_victory_message(self):
        print(self._victory_message)

    def _print_defeat_message(self):
        params = {'secret_word': self.secret_word}
        print(self._defeat_message.format(**params))

    def _draw_gallows(self):
        head_position = 2
        body_position = 3
        lower_body_position = 4
        legs_position = 5

        if (self._tries == 6):
            self._gallows_draw[head_position] = " |      (_)   "

        if (self._tries == 5):
            self._gallows_draw[body_position] = " |      \     "

        if (self._tries == 4):
            self._gallows_draw[body_position] = " |      \|    "

        if (self._tries == 3):
            self._gallows_draw[body_position] = " |      \|/   "

        if (self._tries == 2):
            self._gallows_draw[lower_body_position] = " |       |    "

        if (self._tries == 1):
            self._gallows_draw[legs_position] = " |      /     "

        if (self._tries == 0):
            self._gallows_draw[legs_position] = " |      / \   "

        print('\n'.join(self._gallows_draw))

f = Forca()
f.start_new_game()