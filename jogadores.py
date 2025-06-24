import random
from tabuleiro import POSITIONS

# Função que simula a jogada do computador
# Ela escolhe aleatoriamente uma posição válida no tabuleiro
def jogada_computador(tab, movimento_valido):
    escolhas_possiveis = [pos for pos in range(1, 10) if movimento_valido(tab, pos)]
    return random.choice(escolhas_possiveis) 

