"""Módulo rec.aventura"""
from vitollino import Jogo, Cena, Elemento, Texto
def sumiu():
    deusa.x=-9000
def sumiu1():
    allyne.x=-9000
def some_cldp(*_):
    cldp.x=-9000
def some_pnl(*_):
    pnl.x=-9000
def some_fc(*_):
    fc.x=-9000
def some_fug(*_):
    fug.x=-9000
def some_asp(*_):
    asp.x=-9000
def some_mcr(*_):
    mcr.x=-9000
def some_arz(*_):
    arz.x=-9000
def some_fj(*_):
    fj.x=-9000
def some_cp(*_):
    cp.x=-9000
def some_tal(*_):
    tal.x=-9000
def some_cxa(*_):
    cxa.x=-9000
def some_agua(*_):
    agua.x=-9000
def some_bca(*_):
    bca.x=-9000
def some_lcd(*_):
    lcd.x=-9000
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
cena1 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/imagem_garagem.jpeg?disp=inline&size=G")
cena2 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/foto_escola1.jpeg?disp=inline&size=G", esquerda=cena1)
cena3 = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/imagem_cozinha.jpeg?disp=inline&size=G", direita=cena1, esquerda=cena2).vai()
cena2.direita = cena1.esquerda = cena3
cena1.direita = cena2
deusa = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/deusa.png.png?disp=inline&size=Ghttps://activufrj.nce.ufrj.br/studio/Superpython_Jogos/deusa.png.png?disp=inline&size=G"
achou = "O jogador vai tem que clicar nos itens que precisam ser utilizado para a reciclagem. "
deusa = Elemento (deusa, x=345, y=180,w=300, h=280, texto=achou,foi=sumiu, cena=cena3)
allyne = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/462559384_922152369809269_3108668891184555770_n-removebg-preview.png?disp=inline&size=G"
achou = "Vocés vão ter 1 minutos pra consequir acha os itens que serve de alimentos para a reciclagem!!!"
allyne = Elemento (allyne, x=20, y=100, h=180,texto=achou,foi=sumiu1, cena=cena3)
lcd = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/liquidificador.png?disp=inline&size=G"
lcd = Elemento (lcd, x=459,y=150,w=50,h=30,vai=some_lcd,cena=cena3)
bca = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/bacia-removebg-preview.png?disp=inline&size=G"
bca = Elemento (bca, x=550,y=230,w=40,h=50,vai=some_bca,cena=cena3)
agua = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/a-removebg-preview.png?disp=inline&size=G"
agua = Elemento (agua, x=88,y=239,w=55,h=50,vai=some_agua,cena=cena3)
cxa = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/CX-PAPELAO-ABERTA-300x300-removebg-preview.png?disp=inline&size=G"
cxa = Elemento (cxa, x=100,y=200,w=55,h=40,vai=some_cxa,cena=cena3)
tal = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/D_NQ_NP_2X_682086-MLB45059838586_032021-F-removebg-preview.png?disp=inline&size=G"
tal = Elemento (tal, x=88,y=320,w=55,h=40,vai=some_tal,cena=cena3)
cp = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/copos-descartaveis-coloridos-e1448726767544_1-removebg-preview.png?disp=inline&size=G"
cp = Elemento (cp, x=529,y=399,w=60,h=30,vai=some_cp,cena=cena3)
fj = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/feijao-preto-removebg-preview.png?disp=inline&size=G"
fj = Elemento (fj, x=350,y=320,w=41,h=30,vai=some_fj,cena=cena3)
arz = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/receita-de-arroz-branco-1-removebg-preview.png?disp=inline&size=G"
arz = Elemento (arz, x=530,y=360,w=60,h=30,vai=some_arz,cena=cena3)
mcr = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/macarrao-na-chapa-removebg-preview.png?disp=inline&size=G"
mcr = Elemento (mcr, x=495,y=165,w=30,h=20,vai=some_mcr,cena=cena3)
asp = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/ASSADEIRA-PAO-removebg-preview.png?disp=inline&size=G"
asp = Elemento (asp, x=458,y=160,w=30,h=30,vai=some_asp,cena=cena3)
fug = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/21ca654867db1f69aeeaba8c5ed93a59-_1_-removebg-preview.png?disp=inline&size=G"
fug = Elemento (fug, x=88,y=200,w=35,h=30,vai=some_fug,cena=cena3)
fc = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/20160216_1935-_1_-removebg-preview.png?disp=inline&size=G"
fc = Elemento (fc, x=88,y=320,w=55,h=40,vai=some_fc,cena=cena3)
pnl = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/3eb4156f060b6a0ed3a7ff3603ca47e6_1-removebg-preview.png?disp=inline&size=G"
pnl = Elemento (pnl, x=100,y=222,w=35,h=30,vai=some_pnl,cena=cena3)
cldp = "https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/images-removebg-preview_(2).png?disp=inline&size=G"
cldp = Elemento (cldp, x=100,y=222,w=34,h=32,vai=some_cldp,cena=cena3)