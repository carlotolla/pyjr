"""Módulo des.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento, Texto
def prox():
    b_cena.vai()
    tx.vai()
    
def cena():
    objetos = "escolha um objeto da mesa - A-TERMOSTATO,PEIXE,AQUARIO,LUMINARIA,RAÇÃO_AGUA. B-DETERGENTE,ALGA,ERLENMEYER. C-ALCOOL,TUBO DE ENSAIO,MICROSCOPIO"
    objeto = input(objetos)
    while objeto not in "aA":
        objeto = input(objetos)
    input("você acertou")
    import des.extra
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/laboratorio_bancada.jpg?disp=inline&size=G").vai()
b_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pizo_branco.jpg?disp=inline&size=G")
npc = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/ponto_de-removebg-preview.png?disp=inline&size=G", x=10, y=180, h=200, cena=a_cena)
det = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detetive_mulher.png?disp=inline&size=G", x=350, y=200, h=280, cena=a_cena)
mes = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Mesa-em-inox-removebg-preview.png?disp=inline&size=G", x=50, y=20, h=500, w=500, cena=b_cena)
Texto(a_cena, "Monte o experimento, para um casal de peixes utilizando a agua já tratada. ", foi=prox).vai()
tx = Texto(b_cena, "Monte o experimento, para um casal de peixes utilizando a agua já tratada. ", foi=cena)
mesa = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Mesa-em-inox-removebg-preview.png?disp=inline&size=G")
ace = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/aceleradores-removebg-preview.png?disp=inline&size=G", x=130, y=90, h=100, w=100, cena=b_cena)
ped = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pedra-removebg-preview.png?disp=inline&size=G", x=400, y=156, h=50, w=50, cena=b_cena)
ter = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/termostato-removebg-preview.png?disp=inline&size=G", x=250, y=156, h=50, w=50, cena=b_cena)
raç = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/racao_de_peixe-removebg-preview.png?disp=inline&size=G", x=300, y=156, h=50, w=50, cena=b_cena)
pot = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pote_de_rosca-removebg-preview.png?disp=inline&size=G", x=340, y=156, h=50, w=50, cena=b_cena)
eler = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/erlenmeyer-removebg-preview.png?disp=inline&size=G", x=380, y=156, h=65, w=50, cena=b_cena)
alga = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/algas-removebg-preview.png?disp=inline&size=G", x=150, y=170, h=40, w=50, cena=b_cena)
alco = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/alcool-removebg-preview.png?disp=inline&size=G", x=460, y=140, h=60, w=60, cena=b_cena)
aqua = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/D_NQ_NP_873825-MLB47285123070_082021-W-removebg-preview.png?disp=inline&size=G", x=100, y=150, h=40, w=60, cena=b_cena)
Tubo = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/tubo_de_ensaio-removebg-preview.png?disp=inline&size=G", x=420, y=140, h=65, w=50, cena=b_cena)
peixe = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/peixe_saco-removebg-preview.png?disp=inline&size=G",x=100, y=170, h=40, w=60, cena=b_cena)
mic = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/microscopio-removebg-preview.png?disp=inline&size=G",x=190, y=170, h=40, w=60, cena=b_cena)
der = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detergente-removebg-preview.png?disp=inline&size=G",x=220, y=170, h=40, w=60, cena=b_cena)
lum = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/luminaria-removebg-preview.png?disp=inline&size=G",x=435, y=190, h=40, w=60, cena=b_cena)
# a_cena.direita = b_cena.esquerda
# a_cena.direita = b_cena