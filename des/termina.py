"""Módulo des.continua"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/super.png?disp=inline&size=G").vai()
lix = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/lixeira-removebg-preview.png?disp=inline&size=G", x=100, y=350, h=80, w=65, cena=a_cena)
med = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Hidroxicloroquina_-_Portal-removebg-preview.png?disp=inline&size=G", x=40, y=400, h=50, w=50, cena=a_cena)
deti = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pngtree-investigator-clipart-cartoon-detective-woman-in-a-trenchcoat-vector-png-image_6803063-removebg-preview.png?disp=inline&size=G"
det = Elemento (deti,  x=230, y=340, h=80, w=65, cena=a_cena)
# pex = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/mulher_estranha-removebg-preview.png?disp=inline&size=G", x=320, y=0, h=30, w=40, cena=a_cena)
pexi = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/mulher_estranha-removebg-preview.png?disp=inline&size=G"
achou = "Parabéns voce encontrou ela"
shop = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/shopping.jpg?disp=inline&size=G"
b_cena=Cena(shop)
pex = Elemento (pexi, x=20, y=380, h=30, w=40,  texto=achou, cena=a_cena, foi=b_cena.vai)
texto = Texto(a_cena, "encontre a mulher estranha").vai()
# pex = Elemento (pex , x=320, y=0,  texto=achou, cena=a_cena)
ganhou = "A detetive ganhou 20.000,00 por resolver os casos"
dets = Elemento (deti, x=20, y=300, h=130, w=140,  texto=ganhou, cena=b_cena)
# texto = Texto(a_cena, "encontre a mulher estranha").vai()
