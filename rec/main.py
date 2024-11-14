"""Módulo rec.continua"""
from vitollino import Jogo, Cena, Elemento, Texto
def sumiu():
    pae.x=-9000
def some_lixo(*_):
    lix.x=-9000
def some_lixo2(*_):
    lixo2.x=-9000
def some_lixo3(*_):
    lixo3.x=-9000
def some_lixo4(*_):
    lixo4.x=-9000
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/WhatsApp_Image_2024-06-11_at_10.13.28.jpeg?disp=inline&size=G")
cena2 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/imagem_patio1.jpeg?disp=inline&size=G", esquerda=cena1)
cena3 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/imagem_garagem.jpeg?disp=inline&size=G", direita=cena1, esquerda=cena2).vai()
cena2.direita = cena1.esquerda = cena3
cena1.direita = cena2
ds = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/deusa.png.png?disp=inline&size=G"
achou = " O jogador vai ter que clicar no cesto apenas o que serve de alimento para o urubu em 3 minutos!!!"
pae = Elemento (ds, x=400, y=180, w=300, h=280, texto=achou,foi=sumiu, cena=cena3)
alu = "https://activufrj.nce.ufrj.br/file/Superpython_Jogos/kisspng-goddess-athena-greek-mythology-deity-greek-goddess-5b218def68fee7.7693559515289256794301.jpg?disp=inline"
alu = Elemento (alu, x=250, y=200, h=180, cena=cena2)
lixo = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/lixo-organico-aglobal-4.jpg?disp=inline&size=G"
lix = Elemento(lixo, x=250, y=180, vai=some_lixo, cena=cena3)
lixo2 = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/GI_Market_food_waste.jpg?disp=inline&size=G"
lixo2 = Elemento(lixo2, x=380,y=180, vai=some_lixo2,cena=cena3)
lixo3 ="https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/76e1dfd7342ac1cd5b129ad03d41d153.jpg?disp=inline&size=G"
lixo3 = Elemento(lixo3, x=400,y=75, vai=some_lixo3,cena=cena3)
lixo4 ="https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/O-que-e-Lixo-Organico-Exemplos-e-Utilidades-1024x576.jpg?disp=inline&size=G"
lixo4 = Elemento(lixo4, x=250,y=75, vai=some_lixo4,cena=cena3)

