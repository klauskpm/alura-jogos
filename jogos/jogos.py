import adivinhacao
import forca

print('**********************************')
print("********Escolha o seu jogo********")
print('**********************************')

def int_input(prompt, error_prompt="Você precisa escolher um número."):
    try:
        return int(input(prompt))
    except:
        print(error_prompt)
        return int_input(prompt, error_prompt)

print("(1) Forca (2) Adivinhação")

jogo = int_input("Qual o jogo?")

if (jogo == 1):
    forca.start_game()
elif (jogo == 2):
    adivinhacao.start_game()