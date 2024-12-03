"""Módulo age.termina"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagens
from random import randint as rd

Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
AG = "_ativo/agentes/"

class AventuraTermina:
    def __init__(self):
        self.conta = 0
        self.i_pt = "granito globe graus gnomon".split()
        self.i_no = "s_tubarao s_passaro chave s_pexe".split()
        self.partes = [AG+f"{img}.png" for img in self.i_pt]
        self.lixo = [AG+f"{img}.png" for img in self.i_no]
        imagem_da_praia = AG+"praia.jpeg"
        mapa_praia = Planilha(imagem_da_praia, conta_lado=4.3)
        pg = Paisagens(mapa_praia.j[4:])
        self.p = p = pg.norte
        p.vai()
    def vai(self):
        self.tudo = [Elemento(img, x=rd(10, 600), y=rd(200, 400),
        cena=self.p, vai=lambda *_, pt=parte: self.foi(pt))
        for parte, img in enumerate(self.partes)]
        self.tudo += [Elemento(img, x=rd(10, 600), y=rd(200, 400),
        cena=self.p, vai=self.noe)
        for img in self.lixo]
    def not_(self, x=0, *_):
        self.conta = 0
        for coisa in self.tudo:
            coisa.x = rd(10, 600) - x
            coisa.y = rd(200, 400)
        if x == -4000:
            Elemento(AG+"relogio.png",x=300, y=300, cena=self.p)
    def noe(self, *_):
        Texto(self.p, "droga, isso não faz parte", foi=self.not_).vai()
    def foi(self, parte):
        self.conta += 1
        # parte +=1
        print(self.tudo[parte].img)
        self.tudo[parte].x=0
        self.tudo[parte].y=400
        if self.conta == 4:
            Texto(self.p, "Conseguimos montar!", foi=lambda: self.not_(x=-4000)).vai()

AventuraTermina().vai()