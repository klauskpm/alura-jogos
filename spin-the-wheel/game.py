from random import randint
from time import sleep

from player import Player
from round import Round
from helpers import sleep, clear


class Game:

    def __init__(self):
        with open('defeat_message.txt', 'r') as defeat_file:
            self.__defeat_message = [line for line in defeat_file]
            self.__defeat_message = ''.join(self.__defeat_message)

        with open('victory_message.txt', 'r') as victory_file:
            self.__victory_message = [line for line in victory_file]
            self.__victory_message = ''.join(self.__victory_message)

    def start(self):
        self.__print_opening_message()

        secret_world = self.__get_random_secret_word()
        players = (
            Player('Klaus'),
            Player('Michelle'),
            Player('Marcia')
        )
        won = Round(secret_world, players).run()

        self.__end_game(won, secret_world)

    def __end_game(self, won, secret_word):
        clear()
        if (won):
            self.__print_victory_message()
        else:
            self.__print_defeat_message(secret_word)

    def __print_victory_message(self):
        print(self.__victory_message)

    def __print_defeat_message(self, secret_word):
        params = {'secret_word': secret_word}
        print(self.__defeat_message.format(**params))

    def __get_random_secret_word(self, file_path='fruits.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line for line in file]

        return words[randint(0, len(words) - 1)]

    def __print_opening_message(self):
        clear()
        print('***************************')
        print("Bem vindo ao jogo da Forca!")
        print("***************************")
        sleep(0.5)
        print()
        input("Aperte enter para começar")
