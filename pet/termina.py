"""Módulo pet.termina"""
from vitollino import Sala, Elemento, Texto, Jogo
from vitollino import Roteiro, Ator, Fala, A

Jogo(style=dict(height="500px", width="650px"), did="_jogo_").z()
cenas = "japones relogio mirante tomjobim".split()
jardim = Sala(*[f"/_ativo/jardim/{cena}.jpg" for cena in cenas])
cena = jardim.oeste.vai()
local = "/_ativo/jardim/"
personagens = ("narciso", 450), ("ossanha", 250), ("tetis", 50)
narciso, ossanha, tetis = [Elemento(f"{local}{nome}.png", x=x, y=200, h=300, w=200, cena=cena)
                           for nome, x in personagens]
elenco = (Ator(tetis, "Tetis", 0.4, A.e), Ator(ossanha, "Ossanha", 0.4, A.m),
          Ator(narciso, "Narciso", 0.4, A.d))
falas = [
    Fala(tetis, "Olá, Ossanha você por aqui?", narciso, None),
    Fala(narciso, "Tetis, voce devia falar primeiro comigo", ossanha, None),
    Fala(ossanha, "Rapaz, você se acha o centro do mundo!", narciso, None),
    Fala(narciso, "Do Universo, que eu realmente sou!", tetis, None),
    Fala(tetis, "Eita, não pode ter mais de um deus que dá briga!", tetis, None),
]
Roteiro(cena, falas, elenco)