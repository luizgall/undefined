import scenesModel

class GerenciadorCenas:
    def __init__(self):
        print("Iniciar gerenciador de cenas")
        self.cenaAtual = {}
        self.cenas = scenesModel.scenesFactory()
    def iniciar(self):
        self.cenaAtual = self.cenas["menuPrincipal"]
        self.cenaAtual.start()
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

    