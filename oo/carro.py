"""
Você deve criar uma classse carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direçção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda


    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> #Testando Direção
    >>> direcao=Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

"""
class Carro:
    def __init__(self, direcao, motor) :
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


NORTE='Norte'
LESTE= 'Leste'
SUL='Sul'
OESTE='Oeste'

class Direcao:
    rotacao_a_direita_dtc = {
        NORTE: LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE #utilizando um dicionário, o método girar_a_direita fica muito mais simples
                                                        #ao invés de utilizar muitos if elifs e else
    }

    rotacao_a_esquerda_dtc = {
        NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE
    }

    def __init__(self):
        self.valor= NORTE

    def girar_a_direita(self):
        self.valor=self.rotacao_a_direita_dtc[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dtc[self.valor]
