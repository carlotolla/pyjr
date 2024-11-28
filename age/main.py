"""Módulo age.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagens
Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()

class Inicia:
    def __init__(self):
        i_praia, i_mapa = "_ativo/agentes/praia.jpeg", "_ativo/agentes/pergaminho.png"
        mapa_praia = Planilha(i_praia, conta_lado=4.3)
        self.p = p = Paisagens(mapa_praia.j)
        p.norte.vai()
        self.mapa = Elemento(i_mapa, x=200, y=350, h=20, cena=p.norte, vai=self.ve_mapa)
        self.mapa.o, self.cena = 0.2 , p.norte
    def ve_mapa(self, *_):
        m= self.mapa
        m.o, m.x, m.y, m.w, m.h = 1.0, 100, 10, 400, 400
        self.icon(150, 50, "mountain-sun", "Aqui manda procurar uma caverna próxima", self.caverna)
        self.icon(350, 50, "suitcase", "Existe um baú perdido na praia")
        self.icon(150, 270, "mound", "Tem um artefato ancestral escondido em um sambaqui")
        self.icon(350, 270, "church", "Acho que vamos encontrar algo em um templo")
    def icon(self, x, y, ico, diz="", vai=lambda: None, cena=None):
        cena = cena or self.cena
        style = "font-size: 4em; color: peru;"
        icon = Elemento("_ativo/kwarwp/vazio.png", texto=diz, x=x, y=y, cena=cena, foi=vai)
        icon.elt.html = f'<i class="fa fa-{ico}" style="{style}"></i>'
    def caverna(self):
        from age.aventura import Aventura
        Aventura()
if __name__ == "__main__":
    Inicia()