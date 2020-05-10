class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome=None,idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos=list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__=='__main__':
    eugenio = Pessoa(nome="Eugênio")
    luciano = Pessoa(eugenio,nome="Luciano")
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = "Costa"
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(eugenio.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(eugenio.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(eugenio.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())