from spin_the_wheel.player import Player

from helpers import clear, normalize, sleep
from words import SecretWord


class RoundCLI:
    @staticmethod
    def print_start_message(secret_word: SecretWord, current_player: Player):
        hidden_word = secret_word.get_hidden_word()
        guessed_letters = secret_word.previously_guessed_letters

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

    @staticmethod
    def print_letter_value_message(letter_value):
        print(f"Nessa rodada cada letra vale R${letter_value:.2f}")
        print()

    @staticmethod
    def input_guess():
        guess = input("Chute uma letra ou número: ")
        guess = normalize(guess)

        return guess

    @staticmethod
    def print_guessed_correctly_message(letter_count, guess, earned_money):
        print(f"Tem {letter_count} letras '{guess}'")
        sleep(0.5)
        print(f"Você ganhou R${earned_money:.2f}")
        sleep(0.5)

    @staticmethod
    def print_end_turn_message(keep_playing):
        if keep_playing:
            print("Continue jogando")
        else:
            print("Não foi dessa vez.")
        sleep(2)
