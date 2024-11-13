"""Módulo rec.continua"""
from vitollino import Jogo, Cena, Elemento, Texto
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/foto_escola1.jpeg?disp=inline&size=G")
cena2 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/imagem_patio1.jpeg?disp=inline&size=G", esquerda=cena1)
cena3 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/imagem_garagem.jpeg?disp=inline&size=G", direita=cena1, esquerda=cena2).vai()
cena2.direita = cena1.esquerda = cena3
cena1.direita = cena2
ds  ="https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/deusa.png.png?disp=inline&size=G"
achou = " O jogador vai ter que clicar no cesto apenas o que serve de alimento para o urubu em 3 minutos!!! "
pa = Elemento (ds, x=480, y=250, h=180, texto=achou, cena=cena3)
alu = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/aluno1.png?disp=inline&size=G"
alu = Elemento (alu, x=250, y=200, h=0, cena=cena2)
texto = Texto(cena2, "precisamos de algo reciclavel para termirnarmos nosso trabalho! procure pela escola").vai()