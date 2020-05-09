class Pessoa:
    def __init__(self,*filhos, nome=None,idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos=list(filhos)

    def cumprimentar(self):
        self_ = f'Olá {id(self)}'
        return self_

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
