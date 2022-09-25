import textwrap

def menu():
    menu = '''
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [c]\tNova conta
    [l]\tLista de contas
    [u]\tNovo usuário
    [q]\tSair
    Digite sua opção: 
    '''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('\n--- Deposito realizado com sucesso ---')
    else:
        print('\n!!! Operacao falhou! O valor informado e invalido')
        
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numeroSaques, limiteSaques):
    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaques = numeroSaques >= limiteSaques
    
    if excedeuSaldo:
        print('\n!!! Operacao falhou! Voce nao tem saldo suficiente !!!')
    elif excedeuLimite:
        print('\n!!! Operacao falhou! O valor do saque excede o limite !!!')
    elif excedeuSaques:
        print('\n!!! Operacao falhou! Numero maximo de saques excedido')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: \t\tR$ {valor:.2f}\n'
        numeroSaques += 1
        print('\nSaque realizado com sucesso!')
    else:
        print('\n!!! Operacao falhou! O valor informado e invalido !!!')
    return saldo, extrato


def exibirExtrato(saldo, /, *, extrato):
    print('Nao foram realizados movimentacoes' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')

def criarUsuario(usuarios):
    cpf = input('Informe o CPF (somente numeros): ')
    if usuarios:
        print('\n Ja existe usuario com esse CPF')
        return
    nome = input('Informe o nome completo: ')
    dataNascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereco: ')
    
    usuarios.append({'nome': nome, 'dataNascimento': dataNascimento, 'cpf': cpf, 'endereco': endereco})
    
    print('Usuario criado com sucesso')
    
    
def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None


def criarConta(agencia, numeroConta, usuarios):
    cpf = input('Digite o CPF do usuario: ')
    usuarios = filtrarUsuario(cpf, usuarios)
    if usuarios:
        print('\nConta criada com sucesso')
        return{'agencia': agencia, 'numeroConta': numeroConta, 'usuario': usuarios}
    print('\nUsuario nao encontrado, tente novamente')
    return None


def listarContas(contas):
    for conta in contas:
        linha = f'''
        agencia:\t{conta['agencia']}
        c/c:\t\t{conta['numeroConta']}
        titular:\t{conta['usuario']['nome']}
        '''
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ''
    numeroSaques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)   
        elif opcao == 's':
            valor = float(input('Digite o valor do saque: '))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeroSaques=numeroSaques,
                limiteSaques = LIMITE_SAQUES,
            ) 
        elif opcao == 'e':
            exibirExtrato(saldo, extrato=extrato)
        
        elif opcao == 'u':
            criarUsuario(usuarios)
            
        elif opcao == 'c':
            numeroConta = len(contas) + 1
            conta = criarConta(AGENCIA, numeroConta, usuarios)
            if conta:
                contas.append(contas)
        elif opcao == 'l':
            listarContas(contas)
        elif opcao == 'q':
            break
        else:
            print('Opcao invalida! Tente novamente')

