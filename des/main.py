"""Módulo des.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento

def nova():
    import des.aventura
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Amazonia.jpeg?disp=inline&size=G") #.vai()
capa = Cena("https://i.imgur.com/vlF9laK.png").vai()
cti = "https://i.imgur.com/4SneSxN.jpeg"
mis = "O agente designado terá que resolver os problema do descarte indevido de medicamentos"
ct = Elemento(cti, cena=capa, x=200, y=150, w=400, h=300,texto=mis, foi=a_cena.vai)
tx = Elemento("", cena=capa, x=50, y=220, w=550, h=400,texto=mis, foi=a_cena.vai)
ttx="O CASO DOS MEDICAMENTOS MAL DESCARTADOS"
agt="https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/agentes_escola.png?disp=inline&size=G"
tx.elt.html=f'<span style="color:red;font-weight: bold;font-size:50px;font-family:times">{ttx}</span>'
ag = Elemento(agt, cena=capa, x=10, y=10, w=200, h=200,texto=mis, foi=a_cena.vai)

carfala = "A detetive deve coletar a Água onde houve a morte dos peixes"
det = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detetive_sem_fundo.png?disp=inline&size=G", x=30, y=350, cena=a_cena)
cur = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pngtree-brazilian-folklore-festival-mythical-character-red-hair-grass-skirt-kurupira-png-image_3720896-removebg-preview.png?disp=inline&size=G",  x=300, y=230, cena=a_cena)
pote = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pote_de_vidro-removebg-preview.png?disp=inline&size=G",x=100, y=300,h=70, cena=a_cena)
pote = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/galho-_kkkkkkkkkkkkkkkkkk-removebg-preview.png?disp=inline&size=G",x=100, y=250,h=60, cena=a_cena)
pote = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pngtree-strawberry-image-on-transparent-background-png-image_4562371-1727424430-removebg-preview.png?disp=inline&size=G",x=500, y=40,h=50, cena=a_cena)
car = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/12362407-adesivo-de-uma-carta-aberta-de-desenho-animado-vetor-346798243-removebg-preview.png?disp=inline&size=G", texto=carfala,x=350,y=150,h=30,cena=a_cena, foi=nova)