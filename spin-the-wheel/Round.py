from typing import Tuple

from Player import Player
from SecretWord import SecretWord
from Wheel import Wheel
from helpers import clear, sleep, normalize


class Round:
    def __init__(self, word: str, players: Tuple[Player, ...] = None):
        self._set_players(players)
        self._set_wheel()
        self._set_secret_word(word)

    def _set_players(self, players):
        if players is None:
            players = tuple([Player("Player")])
        self._players = players
        self._players_count = len(self._players)
        self._current_player_index = 0
        self._current_player = self._players[0]

    def _set_wheel(self):
        self._wheel = Wheel([100, 200, 300, 400, 500])
        self._letter_value = 0

    def _set_secret_word(self, word):
        self._secret_word = SecretWord(word)
        self._guessed_letters = []

    def run(self):
        return self._run_turn()

    def _run_turn(self):
        self._spin_the_wheel()
        self._print_round_start_message()
        guess = self._input_guess()

        if self._has_guessed_before(guess):
            return self._run_turn()

        self._check_guess(guess)

        if self._secret_word.was_guessed:
            return
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
            earned_money = self._letter_value * letter_count
            print(f"Tem {letter_count} letras '{guess}'")
            print(f"Você ganhou R${earned_money:.2f}")
            self._current_player.add_money(earned_money)
        else:
            print("Não foi dessa vez.")

        sleep(2)

    def _print_round_start_message(self):
        clear()
        print(f"{self._current_player.name} | R${self._current_player.money:.2f}")
        print(f"Nessa rodada cada letra vale R${self._letter_value:.2f}")
        print()
        print('A palavra secreta é:')
        print(' '.join(self._secret_word.get_hidden_word()))
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

    def _spin_the_wheel(self):
        self._letter_value = self._wheel.spin()
