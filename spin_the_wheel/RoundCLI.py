from spin_the_wheel.player import Player

from helpers import clear


class RoundCLI:
    @staticmethod
    def print_start_message(hidden_word, guessed_letters, current_player: Player):
        clear()
        print('A palavra secreta é:')
        print(' '.join(hidden_word))
        print()
        if len(guessed_letters) > 0:
            print('Letras que já foram chutadas:')
            print(f'[ {", ".join(guessed_letters)} ]')
            print()
        print(f"Turno: {current_player.name} | R${current_player.money:.2f}")
        print()
