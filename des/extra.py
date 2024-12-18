"""Módulo des.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from cenario import Planilha, Paisagem
def nova():
    import des.complemento
a_cena=Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Fazenda.jpg?disp=inline&size=G").vai()
faz = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/fzendeiro-removebg-preview.png?disp=inline&size=G", x=60, y=350, h=100, w=65, cena=a_cena)
det = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/pngtree-investigator-clipart-cartoon-detective-woman-in-a-trenchcoat-vector-png-image_6803063-removebg-preview.png?disp=inline&size=G", x=110, y=350, h=100, w=65, cena=a_cena)
cel = Elemento ("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/iphone-removebg-preview.png?disp=inline&size=G", x=570, y=100, h=10, w=10, cena=a_cena)
achou = "parabens voce fez sua denuncia com sucesso"
aa = "procure meu celular para fazer a denuncia"
cel = Elemento (cel , x=570, y=100,  texto=achou, cena=a_cena, foi=nova)
det = Elemento (det , x=110, y=350,  texto=aa, cena=a_cena)
texto = Texto(a_cena, "oh não! o fazendeiro esta jogando hormonios no rio!").vai()