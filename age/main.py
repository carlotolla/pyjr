"""Módulo age.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagem
from jogos import Sequencia
ESCONDE = -4000
j = Jogo(style=dict(height="500px", width="650px"), did="_jogo_")


class UmaGarrafa:
    def __init__(self):
        imagem_da_praia = "_ativo/agentes/praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        self.p = p = Paisagem(mapa_praia.j[0]).vai()

        self.garrafa = Elemento(img="/_ativo/agentes/carta_garrafa.png", w=30, h=10,
                                x=100, y=300, cena=p, o=0.5, vai=self.acha_garrafa)
        self.garrafa.o = 0.3  # deixa a garrafa transparente
        self.carta = Elemento(img="/_ativo/agentes/carta_velha.jpg", w=250, h=400,
                              x=ESCONDE, y=50, cena=p, texto="Mas o que está escrito aqui?",
                              foi=self.aparece_agente)
        self.agente = Elemento(img="/_ativo/maria.png", w=250, h=400,
                               x=ESCONDE, y=50, cena=p, texto="Deixa que eu vou decifrar",
                               foi=self.o_bilhete)
        texto_bilhete = "Tem um bilhete junto da carta, mas ele está em tiras!"
        self.bilhete = Texto(p, texto_bilhete, foi=self.montar)

    def o_bilhete(self, *_):
        self.carta.x = ESCONDE  # esconde a carta
        self.agente.vai = self.bilhete.vai

    def acha_garrafa(self, *_):
        self.carta.x = 100  # tras a carta para a cena
        self.garrafa.vai = self.nada_faz

    def nada_faz(self, *_):
        pass

    def aparece_agente(self, *_):
        # escreva aqui algo semelhante a acha_garrafa
        self.agente.x = 350
        pass

    def montar(self):
        montou = Texto(self.p, "É a Canção do Exílio do Gonçalves Dias! Mas tem algo atrás!",
                       foi=self.o_diagrama)
        img = "_ativo/agentes/exilio.png"
        poema = Sequencia(j, img, self.p, w=250, h=250, x=10, y=10, dw=2, dh=2,
                          venceu=montou, dim=(10, 180, 2))
        '''Monta o jogo da Sequência , para ordenar um conjunto de tiras'''

    def o_diagrama(self):
        dia = "É o diagrama de um relógio de sol! Temos que achar as peças!"
        mapa = Elemento("_ativo/agentes/diagrama_sol.png", texto=dia,
                        x=4, y=160, w=290, h=290, cena=self.p)
        self.agente.vai = self.nada_faz
        
def main():
    UmaGarrafa

if __name__ == "__main__":
    UmaGarrafa()