"""Módulo des.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/laboratorio_bancada.jpg?disp=inline&size=G").vai()
b_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pizo_branco.jpg?disp=inline&size=G")
npc = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/ponto_de-removebg-preview.png?disp=inline&size=G", x=10, y=180, h=200, cena=a_cena)
det = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detetive_mulher.png?disp=inline&size=G", x=350, y=200, h=280, cena=a_cena)
Texto(a_cena, "Monte o experimento, para um casal de peixes utilizando a agua já tratada. ").vai()
mesa = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Mesa-em-inox-removebg-preview.png?disp=inline&size=G", x=180, y=130, h=400, w=350, cena=b_cena)

a_cena.direita = b_cena.esquerda
a_cena.direita = b_cena