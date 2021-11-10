import api
from view import View
from modelo import manipulaBanco


class Controle:
    def inicio(self):
        comercios, usuarios, transacoes, localizacoes, avaliacoes = api.main()
        manipulaBanco.inserirDados(comercios, usuarios)
        manipulaBanco.inserirDados2(transacoes, localizacoes, avaliacoes)

    def __init__(self):
        self.view = View()

# DELETAR ANTES DE EXECUTAR

if __name__ == "__main__":
    main = Controle()
    main.inicio()