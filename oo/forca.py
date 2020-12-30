from random import randint

from jogos.helpers import map_positions, normalize, sleep, clear


class Forca:
    won: bool
    lost: bool
    tries: int
    guessed_letters: list
    mapped_word_positions: dict
    hidden_word: list

    PLACEHOLDER_LETTER = '_'

    def __init__(self):
        self._secret_word: str = ''

    def start_new_game(self):
        self.reset_states()
        self._print_opening_message()

        while(not self.won and not self.lost):
            self.next_round()

        self.end_game()

    @property
    def secret_word(self):
        return self._secret_word

    @secret_word.setter
    def secret_word(self, secret_word):
        self.mapped_word_positions = map_positions(secret_word)
        self.hidden_word = [Forca.PLACEHOLDER_LETTER for _ in secret_word]
        self._secret_word = secret_word

    def reset_states(self):
        self.won = False
        self.lost = False
        self.tries = 7
        self.guessed_letters = []
        self.set_random_secret_word()

    def set_random_secret_word(self):
        random_word = self.get_random_secret_word()
        self.secret_word = normalize(random_word)

    def get_random_secret_word(self, file_path='words.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line for line in file]

        return words[randint(0, len(words) - 1)]

    def _print_opening_message(self):
        clear()
        print('***************************')
        print("Bem vindo ao jogo da Forca!")
        print("***************************")
        sleep(0.5)
        print()
        input("Aperte enter para começar")

    def next_round(self):
        self.print_round_start_message()
        guess, guessed_before = self.input_guess()

        if (guessed_before):
            return

        self.check_guess(guess)

        self.won = Forca.PLACEHOLDER_LETTER not in self.hidden_word
        self.lost = self.tries <= 0

    def end_game(self):
        clear()
        if (self.won):
            self._print_victory_message()
        elif (self.lost):
            self._print_defeat_message()

    def print_round_start_message(self):
        clear()
        print('A palavra secreta é:')
        print(' '.join(self.hidden_word))
        print()
        print(f"Você tem {self.tries} tentativas.")
        print()
        self._draw_gallows()
        print()

    def input_guess(self):
        guess = input("Chute uma letra: ")
        guess = normalize(guess)
        guessed_before = guess in self.guessed_letters

        if (not guessed_before):
            print(f"Você chutou '{guess}'")
            self.guessed_letters.append(guess)
            sleep(0.6)
        else:
            print(f"A letra '{guess}' já foi chutada anteriormente")
            sleep(2)

        return guess, guessed_before

    def check_guess(self, guess):
        if (guess in self.mapped_word_positions):
            indexes = self.mapped_word_positions[guess]
            letter_count = len(indexes)
            print(f"Tem {letter_count} letras '{guess}'")

            for i in indexes:
                self.hidden_word[i] = guess
        else:
            print("Não foi dessa vez.")
            self.tries -= 1

        sleep(2)

    def _print_victory_message(self):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def _print_defeat_message(self):
        print('Que droga, você foi enforcado.')
        print(f"A palavra era {self.secret_word}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    def _draw_gallows(self):
        print("  _______     ")
        print(" |/      |    ")

        if (self.tries == 7):
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (self.tries == 6):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (self.tries == 5):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (self.tries == 4):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (self.tries == 3):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (self.tries == 2):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (self.tries == 1):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (self.tries == 0):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()
