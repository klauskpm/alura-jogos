import random

default_range_error_message = "Você precisa digitar um número entre {min} e {max}."


def validate_range(var, min_range, max_range, error_message=default_range_error_message):
    if (var < min_range or var > max_range):
        templates_values = {
            'min': min_range,
            'max': max_range
        }
        raise Exception(error_message.format(**templates_values))


def int_input(prompt, error_prompt="Você precisa escolher um número."):
    try:
        return int(input(prompt))
    except:
        print(error_prompt)
        return int_input(prompt, error_prompt)


def get_game_level():
    try:
        print("Qual o nível de dificuldade?")
        level = int_input("(1) Fácil (2) Médio (3) Difícil", "")

        if (level < 1 or level > 3):
            raise Exception("Você precisa digitar um número entre 1 e 3.")

        return level
    except Exception as e:
        print(e)
        return get_game_level()


def init_rounds(points, secret_number, retries):
    for game_round in range(1, retries + 1):
        print('Rodada: {} de {}'.format(game_round, retries))
        guess = int_input("Qual seu chute? (entre 1 e 100)")
        print('Seu chute foi ', guess)

        if (guess < 1 or guess > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        won = guess == secret_number
        greater_than_secret_number = guess > secret_number

        if (won):
            print(f"Você acertou e fez {points} pontos")
            break
        else:
            print("Você errou")
            points = points - abs(secret_number - guess)

            if greater_than_secret_number:
                print("Seu chute foi maior do que o número secreto")
            else:
                print("Seu chute foi menor do que o número secreto")


def start_game():
    secret_number = random.randint(1, 100)
    points = 100
    levels_to_retries = {
        1: 20,
        2: 10,
        3: 5
    }

    print('*********************************')
    print("Bem vindo ao jogo de Adivinhação!")
    print('*********************************')

    level = get_game_level()
    retries = levels_to_retries[level]
    init_rounds(points, secret_number, retries)


if (__name__ == "__main__"):
    start_game()