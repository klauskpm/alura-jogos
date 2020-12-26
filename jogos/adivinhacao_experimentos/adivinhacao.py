def guess_number():
    print('*********************************')
    print("Bem vindo ao jogo de Adivinhação!")
    print('*********************************')

    secret_number = 42
    retries = 3
    game_round = 1
    won = False

    try:
        while game_round <= retries and won is False:
            print('Rodada: {} de {}'.format(game_round, retries))
            guess = int(input("Qual seu chute?"))
            game_round += 1

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
