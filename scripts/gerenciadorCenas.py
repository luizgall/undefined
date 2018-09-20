import scenesModel
from animacao import Animacao

class GerenciadorCenas:
    def __init__(self, cenas, assetLoader):
        print("Iniciar gerenciador de cenas")
        self.cenaAtual = {}
        self.cenas = cenas
        self.assetLoader = assetLoader
        # self.transicao = Animacao()
    def iniciar(self):
        self.cenaAtual = self.cenas["menuPrincipal"]
        self.cenaAtual.start(self.assetLoader)
    def atualizar(self):
        retorno = self.cenaAtual.update()
        
        if retorno["terminou"]:
            if self.cenaAtual.jogador != "":
                del self.cenaAtual.jogador
            del self.cenaAtual
            del self.cenas
            self.cenas = scenesModel.scenesFactory()
            self.cenaAtual = self.cenas[retorno["proximaCena"]]
            self.cenaAtual.start()

    def transicao():
        pass


    