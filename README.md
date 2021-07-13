## Simula Banco

O "Simula Banco" utiliza uma classe Conta exclusivamente para treino da linguagem usando
orientação a objetos (classe, métodos, métodos "privados", getters, setters, etc.

Caso queira aprimorar para seus estudos, fique a vontade.

Obrigado.
*******************************************************************************************************
Orientação a objetos (básico):

Exemplo de classe com funções, retirado do arquivo "conta.py":

    class Conta:
        def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print('Conta {} de {}, possui saldo de {} Reais e limite de {} Reais'.format(numero, titular, saldo, limite))

        def extrato(self):
        print('Saldo de {} do titular {}'.format(self.saldo, self.titular))

        def deposita(self, valor):
        self.saldo += valor

        def saca(self, valor):
        self.saldo -= valor

Onde:
- __init__ = função construtora
- (classe Conta) = objeto
- (conta) = referência
    - ex.: conta = Conta(123, 'Fulano', 50.0, 1000.0), conta2 = Conta(321, 'Cicrano', 20.0, 100.0)
- (numero, titular, saldo, limite) = veriáveis, atributos, parâmetros, propriedades
- (extrato, deposito, saca) = método, função (construtora)
    - ex.: conta.extrato() -> "a referência conta 'fala': procura uma função na classe Conta de nome extrato()"
  
