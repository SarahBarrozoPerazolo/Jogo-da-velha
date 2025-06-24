# Dicionário que associa cada número a uma coordenada do tabuleiro 3x3
POSITIONS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2), 
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
}


# Cria e retorna o tabuleiro inicial do jogo da velha
def criar_tabuleiro():
    return [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]] # Cada célula contém um número, representando as posições disponíveis


# Exibe o tabuleiro no terminal
def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for i, linha in enumerate(tabuleiro):
        nova_linha = [
            c if c in ["X", "O"] else " "  # esconde os números ainda não usados
            for c in linha
        ]
        print(" " + " | ".join(nova_linha)) # Exibe a linha com barras separando as casas
        if i < 2:
            print("---+---+---")  # Adiciona linhas separadoras entre as linhas 1-2 e 2-3
      

# Verifica todas as linhas, colunas e as duas diagonais para ver se o jogador com o símbolo X ou O venceu
def verificar_vitoria(tab, simbolo):
    for i in range(3):
        if all(tab[i][j] == simbolo for j in range(3)) or all(tab[j][i] == simbolo for j in range(3)): # Verifica linha e coluna 
            return True # Se todas as casas de uma linha ou coluna contiverem o mesmo símbolo, retorna True
        
    if all(tab[i][i] == simbolo for i in range(3)) or all(tab[i][2 - i] == simbolo for i in range(3)): # Verifica as diagonais
        return True
    return False # Nenhuma condição de vitória foi atendida


# Verifica se o tabuleiro está completamente preenchido
def tabuleiro_cheio(tab):
    return all(c in ["X", "O"] for linha in tab for c in linha)


# Verifica se uma jogada é válida
def movimento_valido(tab, escolha):
    return escolha in POSITIONS and tab[POSITIONS[escolha][0]][POSITIONS[escolha][1]] not in ["X", "O"] # A posição deve existir no dicionário POSITIONS e a casa correspondente ainda não deve estar ocupada
