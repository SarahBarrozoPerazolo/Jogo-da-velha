POSITIONS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2), 
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
}

def criar_tabuleiro():
    return [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]] 

def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for i, linha in enumerate(tabuleiro):
        nova_linha = [
            c if c in ["X", "O"] else " "  
            for c in linha
        ]
        print(" " + " | ".join(nova_linha)) 
        if i < 2:
            print("---+---+---")  
      
def verificar_vitoria(tab, simbolo):
    for i in range(3):
        if all(tab[i][j] == simbolo for j in range(3)) or all(tab[j][i] == simbolo for j in range(3)): 
            return True 
        
    if all(tab[i][i] == simbolo for i in range(3)) or all(tab[i][2 - i] == simbolo for i in range(3)):
        return True
    return False 

def tabuleiro_cheio(tab):
    return all(c in ["X", "O"] for linha in tab for c in linha)


def movimento_valido(tab, escolha):
    return escolha in POSITIONS and tab[POSITIONS[escolha][0]][POSITIONS[escolha][1]] not in ["X", "O"] 
