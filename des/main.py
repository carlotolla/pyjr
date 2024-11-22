"""Módulo des.continua"""
from vitollino import Cena, Texto, Jogo, Elemento, Sala
from vitollino import Cena, Jogo, Elemento
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Fazenda.jpg?disp=inline&size=G").vai()
faz = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/fzendeiro-removebg-preview.png?disp=inline&size=G", x=270, y=290, h=190, w=90, cena=a_cena)
det = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detetive_mulher.png?disp=inline&size=G", x=350, y=275, h=190, w=90, cena=a_cena)
Texto(a_cena, "oh não! ele esta jogando hormonios no rio!").vai()
iph = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/iphone-removebg-preview.png?disp=inline&size=G", x=350, y=178, h=30, w=30, cena=a_cena)