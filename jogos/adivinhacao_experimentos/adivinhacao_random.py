import random


def guess_number():
    secret_number = random.randint(1, 100)
    retries = 3

    print('*********************************')
    print("Bem vindo ao jogo de Adivinhação!")
    print('*********************************')

    try:
        for game_round in range(1, retries + 1):
            print('Rodada: {} de {}'.format(game_round, retries))
            guess = int(input("Qual seu chute? (entre 1 e 100)"))
            print('Seu chute foi ', guess)

            if (guess < 1 or guess > 100):
                print("Você deve digitar um número entre 1 e 100!")
                continue

            won = guess == secret_number
            greater_than_secret_number = guess > secret_number
            if won:
                print("Você acertou")
                break
            else:
                print("Você errou")
                if greater_than_secret_number:
                    print("Seu chute foi maior do que o número secreto")
                else:
                    print("Seu chute foi menor do que o número secreto")
    except:
        print("Você precisa escolher um número.")
        guess_number()


guess_number()
