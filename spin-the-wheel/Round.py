from typing import Tuple

from Player import Player
from SecretWord import SecretWord
from helpers import clear, sleep, normalize


class Round:
    _LETTER_VALUE = 100

    def __init__(self, word: str, players: Tuple[Player, ...] = None):
        if players is None:
            players = tuple([Player("Player")])
        self._players = players
        self._players_count = len(self._players)
        self._current_player_index = 0
        self._current_player = self._players[0]

        self._guessed_word = False
        self._was_hanged = False
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
        self._secret_word = SecretWord(word)

    def run(self):
        return self._run_turn()

    def _run_turn(self):
        self._print_round_start_message()
        guess = self._input_guess()

        if self._has_guessed_before(guess):
            return self._run_turn()

        self._check_guess(guess)

        self._guessed_word = self._secret_word.has_guessed_word()
        self._was_hanged = self._tries <= 0

        if (self._guessed_word or self._was_hanged):
            return self._guessed_word
        else:
            return self._next_turn()

    def _next_turn(self):
        self._select_next_player()
        return self._run_turn()

    def _select_next_player(self):
        next_player_index = self._current_player_index + 1
        if (next_player_index >= self._players_count):
            next_player_index = 0

        self._current_player_index = next_player_index
        self._current_player = self._players[next_player_index]

    def _check_guess(self, guess):
        letter_count = self._secret_word.get_letter_count(guess)
        if letter_count > 0:
            self._secret_word.guess_letter(guess)
            earned_money = Round._LETTER_VALUE * letter_count
            print(f"Tem {letter_count} letras '{guess}'")
            print(f"Você ganhou R${earned_money:.2f}")
            self._current_player.add_money(earned_money)
        else:
            print("Não foi dessa vez.")
            self._tries -= 1

        sleep(2)

    def _print_round_start_message(self):
        clear()
        print(f"Rodada de {self._current_player.name}")
        print(f"(R${self._current_player.money:.2f})")
        print()
        print('A palavra secreta é:')
        print(' '.join(self._secret_word.get_hidden_word()))
        print()
        print(f"Você tem {self._tries} tentativas.")
        print()
        self._draw_gallows()
        print()

    def _input_guess(self):
        guess = input("Chute uma letra: ")
        guess = normalize(guess)

        return guess

    def _has_guessed_before(self, guess):
        guessed_before = guess in self._guessed_letters

        if (not guessed_before):
            print(f"Você chutou '{guess}'")
            self._guessed_letters.append(guess)
            sleep(0.6)
        else:
            print(f"A letra '{guess}' já foi chutada anteriormente")
            sleep(2)

        return guessed_before

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
