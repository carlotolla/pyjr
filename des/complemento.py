"""Módulo des.continua"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento
def nova():
    import des.termina
def medicamento():
    remedio.y = 180
    ddm.texto = "correta"
    lixeiras.texto = "incorreta"
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/farmacia.jpg?disp=inline&size=G")
b_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/farmacia_bairro.jpg?disp=inline&size=G").vai()
dett = "A detetive foi chamada pela ANVISA para investigar o descarte indevido de medicamentos"
lixo = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/saco_lixo-removebg-preview.png?disp=inline&size=G", x=30, y=350, h=80, w=65, cena=b_cena)
lixeiras = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/lixeiras-removebg-preview.png?disp=inline&size=G", x=310, y=170, h=350, w=170, cena=a_cena)
det = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detetive_mulher.png?disp=inline&size=G", texto=dett, x=390, y=170, h=280, cena=b_cena, foi=a_cena.vai)
ddm = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/ddm-removebg-preview.png?disp=inline&size=G", x=94, y=270, h=180, w=160, cena=a_cena, foi=nova)
remedio = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/remedio-removebg-preview.png?disp=inline&size=G"
talco = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/talco-removebg-preview.png?disp=inline&size=G", x=250, y=70, h=140, w=160, cena=a_cena)
caixadl = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/caixa_de_luva-removebg-preview.png?disp=inline&size=G", x=390, y=70, h=140, w=160, cena=a_cena)
aparel = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/caixa_ortondontica-removebg-preview.png?disp=inline&size=G", x=10, y=70, h=140, w=160, cena=a_cena)
texto = Texto(a_cena, "descarte o medicamento na lixeira correta").vai()
achou = "parabens voce achou o medicamento correto, agora ache a lixeira correta"
remedio = Elemento (remedio, x=160, y=80, texto=achou, cena=a_cena, foi=medicamento)
b_cena.direita = a_cena.esquerda
b_cena.direita = a_cena
a_cena.esquerda = b_cena