from typing import Tuple

from player import Player
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
        self._print_turn_start_message()
        self._spin_the_wheel()
        sleep(0.6)
        self._print_turn_start_message()
        self._print_letter_value_message()
        has_guessed_letter = self._do_guess()
        self._check_round(has_guessed_letter)

    def _print_turn_start_message(self):
        clear()
        print('A palavra secreta é:')
        print(' '.join(self._secret_word.get_hidden_word()))
        print()
        print(f"Turno: {self._current_player.name} | R${self._current_player.money:.2f}")
        print()

    def _spin_the_wheel(self):
        print(
            'Com que força (número) você quer jogar?\n'
            '1 - Fraco\n'
            '2 - Médio\n'
            '3 - Forte'
        )
        strength = int(input(''))
        self._letter_value = self._wheel.spin(strength)

    def _print_letter_value_message(self):
        print(f"Nessa rodada cada letra vale R${self._letter_value:.2f}")
        print()

    def _do_guess(self):
        guess = input("Chute uma letra: ")
        guess = normalize(guess)

        if self._has_guessed_before(guess):
            return self._run_turn()

        return self._check_guess(guess)

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

    def _check_guess(self, guess):
        letter_count = self._secret_word.get_letter_count(guess)
        if letter_count > 0:
            self._secret_word.guess_letter(guess)
            earned_money = self._letter_value * letter_count
            print(f"Tem {letter_count} letras '{guess}'")
            sleep(0.5)
            print(f"Você ganhou R${earned_money:.2f}")
            sleep(0.5)
            self._current_player.add_money(earned_money)
            sleep(0.5)
            print("Continue jogando")
            sleep(2)
            return True
        else:
            print("Não foi dessa vez.")
            sleep(2)
            return False

    def _check_round(self, has_guessed_letter):
        if has_guessed_letter and self._secret_word.was_guessed:
            return True
        elif has_guessed_letter:
            return self._continue_turn()
        else:
            return self._next_turn()

    def _continue_turn(self):
        return self._run_turn()

    def _next_turn(self):
        self._select_next_player()
        return self._run_turn()

    def _select_next_player(self):
        next_player_index = self._current_player_index + 1
        if (next_player_index >= self._players_count):
            next_player_index = 0

        self._current_player_index = next_player_index
        self._current_player = self._players[next_player_index]
