"""Módulo age.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagem
ESCONDE = -4000
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()

class UmaGarrafa:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        p = Paisagem(mapa_praia.j[0])
        p.vai()

        self.garrafa = Elemento(img="/_ativo/agentes/carta_garrafa.png", w=30, h=10,
             x=100, y=300, cena=p, o=0.5, vai=self.acha_garrafa)
        self.garrafa.o = 0.3 #deixa a garrafa transparente
        self.carta = Elemento(img="/_ativo/agentes/carta_velha.jpg", w=250, h=400,
             x=ESCONDE, y=50, cena=p, texto="Mas o que está escrito aqui?", foi=self.aparece_kayke)
        self.kayke = Elemento(img="/_ativo/agentes/kayke.png", w=250, h=400,
             x=ESCONDE, y=50, cena=p, texto="Deixa que eu vou decifrar")

    def acha_garrafa(self, *_):
        self.carta.x = 100 # tras a carta para a cena
        self.garrafa.vai = self.nada_faz

    def nada_faz(self, *_):
        pass

    def aparece_kayke(self, *_):
        # escreva aqui algo semelhante a acha_garrafa
        self.kayke.x = 350
        pass
    
def main():
    UmaGarrafa()
    
if __name__ == "__main__":
    main()
