import random
import time

print('******************************************')
print('----Bem vindos ao jogo da adivinhação----')
print('******************************************')

rodada = 1
tentativas = 3

print(f'Tentativa {rodada} de {tentativas}')

time.sleep(2)
nome = input("Qual o seu nome? ")
time.sleep(1)
print (f'Seja bem vindo {nome}')
time.sleep(1)

while rodada <= tentativas:
    print(f'Tentativa {rodada} de {tentativas}')
    numero_escolhido = int(input('Escolha um numero de 1 a 10: '))
    time.sleep(1)
    print('Estou embaralhando os numeros...')
    time.sleep(2)

    num = [0,1,2,3,4,5,6,7,8,9,10]
    numero = random.choice(num)

    print('.')
    time.sleep(2)
    print('.')
    time.sleep(2)
    print('.')
    time.sleep(2)

    print(f'O numero escolhido foi {numero}')
    time.sleep(2)

    if numero_escolhido == numero :
        print('Parabéns, você escolheu o numero certo, está com sorte... Porque não joga no jogo do bicho?')

    elif  (numero_escolhido == numero + 1) or (numero_escolhido == numero - 1):
        print("Você chegou perto... Tente novamente")

    else:
        print('Você passou longe...') 
        

        rodada+=1

print('Fim do jogo!')