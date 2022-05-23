from random import randint
from time import sleep

#funções para analise das respostas
def pedra():
    if com == 1:
        print('Você jogoou pedra!')
        print('O computador jogou Pedra ')
        print('Empatamos')
    if com == 2:
        print('Você jogoou pedra!')
        print('O computador jogou Papel')
        print('Você perdeu')
    if com == 3:
        print('Você jogoou pedra!')
        print('O computador jogou Tesoura')
        print('Você ganhou')

def papel():

    if com == 1:
        print('Você jogoou papel!')
        print('O computador jogou Preda')
        print('Você ganhou')
    if com == 2:
        print('Você jogoou papel!')
        print('O computador jogou Papel')
        print('Empatamos')
    if com == 3:
        print('Você jogoou papel!')
        print('O computador jogou Tesoura')
        print('Você perdeu')

def tesoura():

    if com == 1:
        print('Você jogoou papel!')
        print('O computador jogou Pedra')
        return print('Você perdeu')
    if com == 2:
        print('Você jogoou papel!')
        print('O computador jogou Papel ')
        return print('Você ganhou')
    if com == 3:
        print('Você jogoou papel!')
        print('O computador jogou Tesoura ')
        return print('Empatamos')

#laço de continuação do programa
while True:
    print('-='*11)
    print('PEDRA = 1\nPAPEL = 2\nTESOURA = 3')
    com = randint(1,3)
    jogador = (input('Qual deseja jogar? '))
    
    if jogador == '1' or jogador == '2' or jogador == '3':
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        sleep(2)
    

    if jogador == '1':
        pedra()
    
    if jogador == '2':
        papel()
    
    if jogador == '3':
        tesoura()

    if jogador == 'sair':
        print('saindo')
        print('-='*11)
        break

    if jogador != '1' and jogador != '2' and jogador != '3':
        print('nao entendi')
