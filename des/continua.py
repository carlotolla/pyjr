"""Módulo des.continua"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/farmacia.jpg?disp=inline&size=G")
b_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/farmaciaex.jpg?disp=inline&size=G").vai()
lixo = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/saco_lixo-removebg-preview.png?disp=inline&size=G", x=30, y=350, h=80, w=65, cena=b_cena)
lixeiras = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/lixeiras-removebg-preview.png?disp=inline&size=G", x=310, y=170, h=350, w=170, cena=b_cena)
b_cena.direita = a_cena.esquerda
b_cena.direita = a_cena
a_cena.esquerda = b_cena