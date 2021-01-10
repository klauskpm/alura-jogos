from typing import Tuple

from player import Player
from helpers import clear, sleep, normalize, map_positions


class Round:
    __PLACEHOLDER_LETTER = '_'

    def __init__(self, word: str, players: Tuple[Player, ...] = None):
        if players is None:
            players = tuple([Player("Player")])
        self._players = players
        self._players_count = len(self._players)
        self._current_player_index = 0
        self._current_player = self._players[0]
        self._money_for_letter = 100

        self.__won = False
        self.__lost = False
        self.__tries = 7
        self.__hidden_word = []
        self.__guessed_letters = []
        self.__mapped_word_positions = {}
        self.__gallows_draw = [
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
        self.__set_random_secret_word(word)

    def __set_random_secret_word(self, word):
        self.__secret_word = normalize(word)
        self.__mapped_word_positions = map_positions(self.__secret_word)
        self.__hidden_word = [Round.__PLACEHOLDER_LETTER for _ in self.__secret_word]

    def run(self):
        return self._run_turn()

    def _run_turn(self):
        self.__print_round_start_message()
        guess, guessed_before = self.__input_guess()

        if (guessed_before):
            return self._run_turn()

        self.__check_guess(guess)

        self.__won = Round.__PLACEHOLDER_LETTER not in self.__hidden_word
        self.__lost = self.__tries <= 0

        if (self.__won or self.__lost):
            return self.__won
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

    def __check_guess(self, guess):
        if (guess in self.__mapped_word_positions):
            indexes = self.__mapped_word_positions[guess]
            letter_count = len(indexes)
            print(f"Tem {letter_count} letras '{guess}'")

            for i in indexes:
                self.__hidden_word[i] = guess
        else:
            print("Não foi dessa vez.")
            self.__tries -= 1

        sleep(2)

    def __print_round_start_message(self):
        clear()
        print(f"Rodada de {self._current_player.name}")
        print(f"Dinheiro: {self._current_player.money}")
        print()
        print('A palavra secreta é:')
        print(' '.join(self.__hidden_word))
        print()
        print(f"Você tem {self.__tries} tentativas.")
        print()
        self.__draw_gallows()
        print()

    def __input_guess(self):
        guess = input("Chute uma letra: ")
        guess = normalize(guess)
        guessed_before = guess in self.__guessed_letters

        if (not guessed_before):
            print(f"Você chutou '{guess}'")
            self.__guessed_letters.append(guess)
            sleep(0.6)
        else:
            print(f"A letra '{guess}' já foi chutada anteriormente")
            sleep(2)

        return guess, guessed_before

    def __draw_gallows(self):
        head_position = 2
        body_position = 3
        lower_body_position = 4
        legs_position = 5

        if (self.__tries == 6):
            self.__gallows_draw[head_position] = " |      (_)   "

        if (self.__tries == 5):
            self.__gallows_draw[body_position] = " |      \     "

        if (self.__tries == 4):
            self.__gallows_draw[body_position] = " |      \|    "

        if (self.__tries == 3):
            self.__gallows_draw[body_position] = " |      \|/   "

        if (self.__tries == 2):
            self.__gallows_draw[lower_body_position] = " |       |    "

        if (self.__tries == 1):
            self.__gallows_draw[legs_position] = " |      /     "

        if (self.__tries == 0):
            self.__gallows_draw[legs_position] = " |      / \   "

        print('\n'.join(self.__gallows_draw))
