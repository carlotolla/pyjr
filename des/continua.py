"""Módulo des.continua"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
b_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/farmacia.jpg?disp=inline&size=G")
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/farmaciaex.jpg?disp=inline&size=G").vai()
b_cena.esquerda = b_cena.direita
a_cena.direita = a_cena.esquerda