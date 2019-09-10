class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28): #tudo dentro dos parenteses são os parâmetros
        self.idade = idade #self.idade é um atributo
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self): #método é diferente de uma função pois está dentro de uma classe e sempre está atrelado a um objeto
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rumbels = Pessoa(nome='Rumbelsperger')
    querido = Pessoa(rumbels, nome='Querido') #atributo complexo, rumbelsperger depende do querido
    print(Pessoa.cumprimentar(querido))
    print(id(querido))
    print(querido.cumprimentar())
    print(querido.nome)
    print(querido.idade)
    for filho in querido.filhos:
        print(filho.nome)
    querido.sobrenome = 'Ferreira' #Aqui estou incluindo um atributo dinâmico
    del querido.filhos #Aqui estou REMOVENDO um atributo dinamicamente
    print(querido.sobrenome)
    print(querido.__dict__) #os atributps de instância ficam armazenados no "__dict__"
    print(rumbels.__dict__)
