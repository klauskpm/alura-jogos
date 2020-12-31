from random import randint

from jogos.helpers import map_positions, normalize, sleep, clear


class Forca:
    __PLACEHOLDER_LETTER = '_'

    def __init__(self):
        self.__won = False
        self.__lost = False
        self.__tries = 7
        self.__guessed_letters = []
        self.__mapped_word_positions = {}
        self.__hidden_word = []
        self.__secret_word = ''
        self.__gallows_draw = []
        with open('defeat_message.txt', 'r') as defeat_file:
            self.__defeat_message = [line for line in defeat_file]
            self.__defeat_message = ''.join(self.__defeat_message)

        with open('victory_message.txt', 'r') as victory_file:
            self.__victory_message = [line for line in victory_file]
            self.__victory_message = ''.join(self.__victory_message)

    def start_new_game(self):
        self.__reset_states()
        self.__print_opening_message()

        while(not self.__won and not self.__lost):
            self.__next_round()

        self.__end_game()

    def __reset_states(self):
        self.__won = False
        self.__lost = False
        self.__tries = 7
        self.__guessed_letters = []
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
        self.__set_random_secret_word()

    def __set_random_secret_word(self):
        self.__secret_word = normalize(self.__get_random_secret_word())
        self.__mapped_word_positions = map_positions(self.__secret_word)
        self.__hidden_word = [Forca.__PLACEHOLDER_LETTER for _ in self.__secret_word]

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

    def __next_round(self):
        self.__print_round_start_message()
        guess, guessed_before = self.__input_guess()

        if (guessed_before):
            return

        self.__check_guess(guess)

        self.__won = Forca.__PLACEHOLDER_LETTER not in self.__hidden_word
        self.__lost = self.__tries <= 0

    def __end_game(self):
        clear()
        if (self.__won):
            self.__print_victory_message()
        elif (self.__lost):
            self.__print_defeat_message()

    def __print_round_start_message(self):
        clear()
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

    def __print_victory_message(self):
        print(self.__victory_message)

    def __print_defeat_message(self):
        params = {'secret_word': self.__secret_word}
        print(self.__defeat_message.format(**params))

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

f = Forca()
f.start_new_game()
