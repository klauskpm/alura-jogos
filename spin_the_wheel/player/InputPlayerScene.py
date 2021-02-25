from .exceptions import InvalidName
from .Player import Player


class InputPlayerScene:
    @staticmethod
    def input_players():
        try:
            players_count = int(input("Quantos jogadores serão? "))
        except ValueError:
            print('Você deve informar um número')
            return InputPlayerScene.input_players()

        if players_count < 1:
            print('Deve ter no mínimo 1 jogador(a)')
            return InputPlayerScene.input_players()
        players = []

        while players_count > 0:
            player_name = input('Qual o nome do jogador? ')
            try:
                players.append(Player(player_name))
                players_count -= 1
            except InvalidName:
                print('O jogador(a) deve ter um nome')
                continue

        return tuple(players)

