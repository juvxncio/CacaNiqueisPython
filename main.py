# Caça-Níqueis
import random

def linha_giro():
    simbolos = ['⭐', '🍉', '🍋', '🔔', '🍒']

    return [random.choice(simbolos) for _ in range(3)]

def print_giro(giro):
    print('**************')
    print(' | '.join(giro))
    print('**************')

def get_pagamento(giro, aposta):
    if giro[0] == giro[1] == giro[2]:
        if giro[0] == '🍒':
            return aposta * 3
        elif giro[0] == '🍉':
            return aposta * 4
        elif giro[0] == '🍋':
           return aposta * 5
        elif giro[0] == '🔔':
            return aposta * 10
        elif giro[0] == '⭐':
            return aposta * 20
    return 0

def main():
    saldo = 100

    print('*********************************')
    print('Bem-vindo ao Caça-Níqueis Python!')
    print('Símbolos: ⭐ 🍉 🍋 🔔 🍒')
    print('*********************************')

    while saldo > 0:
        print(f'Saldo atual: R${saldo}')

        aposta = input('Selecione um valor para apostar:')

        if not aposta.isdigit():
            print('Digite um número válido')
            continue

        aposta = int(aposta)

        if aposta > saldo:
            print('Saldo insuficiente')

        if aposta <= 0:
            print('A aposta deve ser maior que R$0')

        saldo -= aposta

        giro = linha_giro()
        print('Girando...\n')
        print_giro(giro)

        pagamento = get_pagamento(giro, aposta)

        if pagamento > 0:
            print(f'Parabéns, você ganhou R${pagamento}! 😁')
        else:
            print('Desculpe, você não ganhou nada nessa rodada 🙁')

        saldo += pagamento

        jogar_novamente = input('Você deseja girar de novo? (S/N):').upper()

        if jogar_novamente != 'S':
            break

    print('*********************************************')
    print(f'Fim de jogo! Seu saldo final é de: R${saldo}')
    print('*********************************************')

if __name__ == '__main__':
    main()