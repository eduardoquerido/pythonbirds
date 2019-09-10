class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28): #tudo dentro dos parenteses são os parâmetros
        self.idade = idade #self.idade é um atributo
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self): #método é diferente de uma função pois está dentro de uma classe e sempre está atrelado a um objeto
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rumbelsperger = Pessoa(nome='Rumbelsperger')
    querido = Pessoa(rumbelsperger, nome='Querido') #atributo complexo, rumbelsperger depende do querido
    print(Pessoa.cumprimentar(querido))
    print(id(querido))
    print(querido.cumprimentar())
    print(querido.nome)
    print(querido.idade)
    for filho in querido.filhos:
        print(filho.nome)
    querido.sobrenome = 'Ferreira' #atributo dinâmico
    print(querido.sobrenome)