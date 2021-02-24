from .Player import Player


class InputPlayerScene:
    @staticmethod
    def input_players():
        players_count = int(input("Quantos jogadores serão?"))
        players = []
        while players_count > 0:
            player_name = input('Qual o nome do jogador?')
            players.append(Player(player_name))
            players_count -= 1

        return tuple(players)

