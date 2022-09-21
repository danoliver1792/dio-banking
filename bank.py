print('-' * 25)
print('Bem-vindo ao nosso Banco!')
print('-' * 25)

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = str(input('''
                      Escolha uma opção:
                      
                      [d] Depositar;
                      [s] Sacar;
                      [e] Extrato;
                      [q] Sair
                      => '''))


    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: '))       
        #só podemos depositar valores positivos
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operacao invalida! So aceitamos valores positivos")
            
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        #temos um limite de apenas 3 operações de saque de R$ 500,00 cada
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operacao invalida! Voce nao tem saldo suficiente')
        elif excedeu_limite:
            print('operacao invalida! O valor do saque excede o limite')
        elif excedeu_saques:
            print('Operacao invalida! Numero maximo de saques atingido')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques -= 1
        else:
            print('Falha na operacao! Valor invalido')
    elif opcao == 'e':
        #no extrato teremos uma lista dos depósitos e saques do banco
        print('-' * 25)
        print('EXTRATO')
        print('-' * 25)
        print('Transacoes nao realizadas' if not extrato else extrato)
        print(f'\nsaldo: R$ {saldo:.2f}')
    elif opcao == 'q':
        break
    else:
        print('Erro! Selecione uma das opcoes')
