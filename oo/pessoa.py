class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rumbels = Pessoa(nome='Rumbelsperger')
    querido = Pessoa(rumbels, nome='Querido')
    print(Pessoa.cumprimentar(querido))
    print(id(querido))
    print(querido.cumprimentar())
    print(querido.nome)
    print(querido.idade)
    for filho in querido.filhos:
        print(filho.nome)