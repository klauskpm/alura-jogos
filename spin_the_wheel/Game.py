from random import randrange
from time import sleep

from player import InputPlayerScene
from Round import Round
from helpers import sleep, clear


class Game:

    def __init__(self):
        with open('drawings/victory_message.txt', 'r') as victory_file:
            self._victory_message = [line for line in victory_file]
            self._victory_message = ''.join(self._victory_message)

    def start(self):
        self._print_opening_message()

        secret_world = self._get_random_secret_word()
        players = InputPlayerScene.input_players()
        Round(secret_world, players).run()

        self._end_game(players)

    def _end_game(self, players):
        clear()
        self._print_victory_message(players)

    def _print_top_five_ranking(self, players):
        players_count = len(players)
        if (players_count <= 1):
            return

        ranked_players = sorted(players, key=lambda player: player.money, reverse=True)
        max_rank = min(players_count, 5)
        for i in range(max_rank):
            rank = i + 1
            player = ranked_players[i]
            print(f"#{rank} - {player.name} com R${player.money:.2f}")

        print()
        print()

    def _print_victory_message(self, players):
        self._print_top_five_ranking(players)
        print(self._victory_message)

    def _get_random_secret_word(self, file_path='words/fruits.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line for line in file]

        return words[randrange(0, len(words))]

    def _print_opening_message(self):
        clear()
        print('***************************')
        print("Bem vindo ao jogo da Forca!")
        print("***************************")
        sleep(0.5)
        print()
        input("Aperte enter para começar")
