"""Módulo des.main"""
from vitollino import Cena, Jogo, Texto, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/laboratorio_bancada.jpg?disp=inline&size=G").vai()
NPC = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/ponto_de-removebg-preview.png?disp=inline&size=G", x=10, y=180, h=200, cena=a_cena)
det = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detetive_mulher.png?disp=inline&size=G", x=350, y=200, h=280, cena=a_cena)