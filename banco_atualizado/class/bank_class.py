from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
        
    def realizarTransacao(self, conta, transacao):
        transacao.resgistrar(conta)
        
        
    def adicionarConta(self, conta):
        self.contas.append(conta)
        
        
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
        
class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()
        
        @classmethod
        def novaConta(cls, cliente, numero):
            return cls(numero, cliente)
        
        
        @property
        def saldo(self):
            return self._saldo
        
        
        @property
        def numero(self):
            return self._numero
        
        
        @property
        def agencia(self):
            return self._agencia
        
        
        @property
        def cliente(self):
            return self._cliente
        
        
        @property
        def historico(self):
            return self._historico
        
        
        def sacar(self, valor):
            saldo = self.saldo
            excedeuSaldo = valor > saldo
            if excedeuSaldo:
                print('Operacao invalida! Saldo insuficiente')
            elif valor > 0:
                self._saldo -= valor
                print('Saque realizado com sucesso!')
            else:
                print('Erro! Valor informado invalido')
            return False
        
        
        def depositar(self, valor):
            if valor > 0:
                self._saldo += valor
                print('Deposito realizado com sucesso')
            else:
                print('Erro! Valor informado invalido')
            return True
        
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limiteSaque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limiteSaque = limiteSaque
        
    
    def sacar(self, valor):
        numeroSaques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )
        
        excedeuLimite = valor > self.limite
        excedeuSaques = numeroSaques >= self.limiteSaque
        
        if excedeuLimite:
            print('Operacao invalida! O valor do saque excede o lmite')
        elif excedeuSaques:
            print('Operacao invalida! Numero maximo de saques excedido')
        else:
            return super().sacar(valor)
        return False
    
        
    def __str__(self):
        return f'''
        agencia:\t{self.agencia}
        C/C:\t\t{self.numero}
        titular:\t{self.cliente.nome}
    '''
    
    
class Historico:
    def __init__(self):
        self.transacoes = []
        
        
    @property
    def transacoes(self):
        return self._transacoes
    
    
    def adcionarTransacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%s'),
            }
        )
        
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    
    @abstractclassmethod
    def registrar(self, conta):
        pass
    
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
        
    @property
    def valor(self):
        return self._valor
    
    
    def registrar(self, conta):
        sucessoTransacao = conta.sacar(self.valor)
        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)
            
            
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
        
    @property
    def valor(self):
        return self._valor
    
    
    def registrar(self, conta):
        sucessoTransacao = conta.depositar(self.valor)
        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)
            

