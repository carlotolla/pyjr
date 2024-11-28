"""Módulo age.aventura"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Mapa, Paisagens, Posiciona
j = Jogo(style=dict(height="500px", width="650px"), did="_jogo_")

class Aventura:
    def __init__(self):
        self.da = da = "_ativo/agentes/"
        i_c, self.i_p, i_p = "_cenas/cavernas.jpg", da+"pergaminho.png", da+"praia.jpeg"
        c = Mapa(i_c, conta_lado=4.3)
        self.c0, self.c1, self.c2 = c.salas[0], c.salas[1], c.salas[2]
        p = Mapa(i_p, conta_lado=4.3)
        self.p0, self.p1, self.p2 = p.salas[0], p.salas[1], p.salas[2]
        self.caverna()

    def caverna(self, *_):
        self.c0.norte.vai()
        diz = "No bilhete dizia que temos que encontrar o desenho de um homem"
        Texto(self.c0.norte, diz).vai()
        self.mapa = Elemento(self.i_p, x=60, y=218, h=60, w=50, o=0.3,
                            cena=self.c2.leste, vai=self.ve_mapa)

    def ve_mapa(self, *_):
        from jogos import Swap
        cena = self.c1.norte
        cena.vai()
        i_imagem = "_ativo/agentes/rupestre.jpg"
        t = Texto(cena, "Temos que encontrar umas aves próximas do mar", foi=self.aves)
        Swap(j, i_imagem, cena, 400, 400, 10, 10, 3, 3, venceu=t)
        m= self.mapa

    def aves(self):
        def anel(x=20, y=20, s=400, o=1):
            m.o, m.x, m.y, m.w, m.h = o, x, y, s, s

        i_a, i_s, i_g = self.da+"aves.png", self.da+"sinal.png", self.da+"graus.png"
        self.i_s, a, b = i_s, self.p1.leste, self.p1.sul
        self.p0.norte.vai()
        siga = "Siga as pegadas, você vai atintir a sua 'META'"
        pt = "Achamos uma parte do relógio de sol"
        m = Elemento(i_g, h=20, w=20, x=-1000, y=337, o=0.2, texto=pt, foi=anel, cena=b)
        Elemento(i_a, x=493, y=219, cena=a, texto=siga, foi=lambda:anel(512,337,20,0.2))
        self.sinal("PRAIA ➤➤➤", self.p1.norte, self.praia)
        self.sinal("SAMBA\nQUI➤➤", self.p1.oeste, self.sambaqui)
        self.sinal("CAVER\nNA➤➤", self.p2.norte, self.caverna)
        self.sinal("Templo ➤➤➤➤", self.p2.norte, self.caverna)
    def sinal(self, texto, cena, vai):
        pr = Elemento(self.i_s, x=10, y=319, cena=cena, vai=vai)
        style = "font-size: 1.5em; color: saddlebrown; margin:6px; pointer-events: none;"
        pr.elt.html = f'<h6 style="{style}">{texto}</h1>'
    def sambaqui(self, *_):
        self.p2.norte.vai()
        return
        from age.aventura import Aventura
        Aventura()
    def sambaqui(self, *_):
        self.p2.norte.vai()
        return
        from age.aventura import Aventura
        Aventura()

    def praia(self, *_):
        self.p2.norte.vai()
        return
        from age.aventura import Aventura
        Aventura()
if __name__ == "__main__":
    Aventura()         