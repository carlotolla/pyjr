"""Módulo des.main"""
from vitollino import Cena, Texto, Jogo, Elemento
from vitollino import Cena, Jogo, Elemento
Jogo(style=dict(height="450px", width="600px"), did="_jogo_").z()
a_cena = Cena("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/produto_9-2967225546.jpg?disp=inline&size=G", tela=None).vai()
saci = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/Saci-1081199002-removebg-preview.png?disp=inline&size=G", x=100, y=350, cena=a_cena)
homem = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/homem-de-negocios-com-ponto-de-interrogacao-na-cabeca-isolada-no-fundo-branco-86631204-1159827819-removebg-preview.png?disp=inline&size=G",  x=30, y=350, cena=a_cena)
gorro = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/chapeu-gorro-sete-anoes-vermelho-844051709-removebg-preview.png?disp=inline&size=G",x=300, y=380, h=15, cena=a_cena)
det = Elemento("https://activufrj.nce.ufrj.br/studio/Superpython_Jogos/detetive-removebg-preview.png?disp=inline&size=G", x=300, y=350, cena=a_cena)

