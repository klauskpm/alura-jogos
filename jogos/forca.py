import time
from random import randint
from sys import argv

from helpers import map_positions, normalize, clear

PLACEHOLDER_LETTER = '_'
DEBUG_MODE = 'debug' in argv[1:]


def start_game():
    secret_word = get_word()
    print_game_start_message()
    init_rounds(secret_word)


def get_word():
    with open('words.txt', 'r', encoding="utf-8") as file:
        words = [normalize(line) for line in file]

    return words[randint(0, len(words) - 1)]


def print_game_start_message():
    clear()
    print('***************************')
    print("Bem vindo ao jogo da Forca!")
    print("***************************")
    sleep(0.5)
    print()
    input("Aperte enter para começar")


def init_rounds(word):
    won = False
    hanged = False

    tries = 7
    guessed_letters = []
    word = normalize(word)
    mapped_word_positions = map_positions(word)
    hidden_word = [PLACEHOLDER_LETTER for _ in word]

    while (not won and not hanged):
        print_round_start_message(hidden_word, tries)
        guess, guessed_letters, guessed_before = input_guess(guessed_letters)

        if (guessed_before):
            continue

        tries, hidden_word = check_guess(guess, hidden_word, mapped_word_positions, tries)

        won = PLACEHOLDER_LETTER not in hidden_word
        hanged = tries <= 0

    clear()
    if (won):
        print_victory_message()
    elif (hanged):
        print_defeat_message(word)


def print_round_start_message(hidden_word, tries):
    clear()
    print('A palavra secreta é:')
    print(' '.join(hidden_word))
    print()
    print(f"Você tem {tries} tentativas.")
    print()
    draw_gallows(tries)
    print()


def input_guess(guessed_letters):
    guess = input("Chute uma letra: ")
    guess = normalize(guess)
    guessed_before = guess in guessed_letters
    gl_copy = guessed_letters.copy()

    if (not guessed_before):
        print(f"Você chutou '{guess}'")
        gl_copy.append(guess)
        sleep(0.6)
    else:
        print(f"A letra '{guess}' já foi chutada anteriormente")
        sleep(2)

    return guess, gl_copy, guessed_before


def check_guess(guess, hidden_word, mapped_word_positions, tries):
    hw_copy = hidden_word.copy()

    if (guess in mapped_word_positions):
        indexes = mapped_word_positions[guess]
        letter_count = len(indexes)
        print(f"Tem {letter_count} letras '{guess}'")

        for i in indexes:
            hw_copy[i] = guess
    else:
        print("Não foi dessa vez.")
        tries -= 1

    sleep(2)

    return tries, hw_copy


def print_victory_message():
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


def print_defeat_message(secret_word):
    print('Que droga, você foi enforcado.')
    print("A palavra era {}".format(secret_word))
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


def draw_gallows(tries):
    print("  _______     ")
    print(" |/      |    ")

    if (tries == 7):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tries == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tries == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tries == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tries == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tries == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tries == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tries == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def sleep(seconds):
    if (not DEBUG_MODE):
        time.sleep(seconds)


if (__name__ == "__main__"):
    start_game()
