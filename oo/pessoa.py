#Obs: Sempre que for criar um atributo, deve-se perguntar se esse atributo é ou não comum para todos os objetos de uma classe
#caso sim, então esse atributo deve ser um atributo de classe, caso contrário, então, deve ser um atributo de instância


class Pessoa:
    olhos = 2 #Isso é um atributo "default" ou padrão, que no caso é comum para todos os outros objetos
                #Também conhecido como atributo de classe

    def __init__(self, *filhos, nome=None, idade=28):  # tudo dentro dos parenteses são os parâmetros
        # MÉTODO: def nome_método(parâmetros_método):
        self.idade = idade  # self.idade é um atributo de instância
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(
            self):  # método é diferente de uma função pois está dentro de uma classe e sempre está atrelado a um objeto
        return f'Olá {id(self)}'

    @staticmethod #Isso é um decorator
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls): #o cls está se referindo a classe desse código, no caso, a classe Pessoa
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa): #A classe Pessoa é a característica PAI da classe Homem
    pass


class Mutante(Pessoa): #A classe Pessoa é a característica PAI da classe Homem
    olhos = 3 #Sobrescrita de atributo, esse atributo sobrepoe o atributo já definido na classe Pai, no caso dessa a classe Pessoa



if __name__ == '__main__':
    rumbels = Homem(nome='Rumbelsperger') #Alterando a classe, por Homem ser uma classe que herda da classe Pessoa, o código continua funcionando
    dudu = Mutante(nome='Rumbelsperger') #Alterando a classe, por Homem ser uma classe que herda da classe Pessoa, o código continua funcionando
    querido = Pessoa(rumbels, nome='Querido')  # atributo complexo, rumbelsperger depende do querido
    print(Pessoa.cumprimentar(querido))
    print(id(querido))
    print(querido.cumprimentar())
    print(querido.nome)
    print(querido.idade)
    for filho in querido.filhos:
        print(filho.nome)
    querido.sobrenome = 'Ferreira'  # Aqui estou incluindo um atributo dinâmico
    del querido.filhos  # Aqui estou REMOVENDO um atributo dinamicamente
    print(querido.sobrenome)
    #rumbels.olhos = 1 #quando eu altero um atributo de classe de um objeto ele passa a fazer parte do __dict__ desse objeto
    print(querido.__dict__)  # os atributps de instância ficam armazenados no "__dict__"
    print(rumbels.__dict__) #Aqui será incluso o atributo olhos = 1, pois foi alterado  e virou um atributo de instância

    print(Pessoa.olhos) #O atributo de classe, se chama assim pois ele pode ser acessado através da própria classe
    print(querido.olhos)
    print(rumbels.olhos)#O atributo de classe também podem ser acessados via objetos, já que os abjetos fazem parte da classe


    print(id(Pessoa.olhos), id(rumbels.olhos), id(querido.olhos)) #imprimindo o id desse atributo, seja com a classe ou com
                                                                  #os objetos, iremos obter o mesmo resultado, pois ele é padrão
    print(Pessoa.metodo_estatico(), querido.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), querido.nome_e_atributos_de_classe())

    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa)) #Retornará True
    print(isinstance(pessoa, Homem)) #Retornará False
    print(isinstance(rumbels, Pessoa)) #Retornará True, pq homem herda de Pessoa
    print(isinstance(rumbels, Homem)) #Retornará True pois rumbels foi atribuito a classe Homem
    print(rumbels.olhos)
    print(dudu.olhos)