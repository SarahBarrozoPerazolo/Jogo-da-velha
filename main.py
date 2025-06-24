from tabuleiro import criar_tabuleiro, mostrar_tabuleiro, verificar_vitoria, tabuleiro_cheio, movimento_valido, POSITIONS
from jogadores import jogada_computador

def rodada(modo, jogador1, computador):
    vitorias = {"X": 0, "O": 0, "Empate": 0} # Inicia o placar
    jogador2 = "O" if jogador1 == "X" else "X"  # Define o jogador 2 com base no símbolo escolhido por jogador 1
    jogar_mais = True # Variável para controlar se o jogo continua

    while jogar_mais:
        tabuleiro = criar_tabuleiro() # Cria um novo tabuleiro para a rodada
        jogador_atual = jogador1 # Começa com o jogador 1
        mostrar_tabuleiro(tabuleiro) # Exibe o tabuleiro inicial


        while True:
            if computador and jogador_atual == computador:
                pos = jogada_computador(tabuleiro, movimento_valido)
                print(f"\nComputador ({computador}) escolheu a posição {pos}")
            else:
                # Se for jogador humano, recebe input do usuário
                try:
                    pos = int(input(f"\nJogador {jogador_atual}, escolha uma casa (1-9): "))
                    if not movimento_valido(tabuleiro, pos):
                        print("Movimento ilegal. Tente novamente.")
                        continue # Volta pro input se for inválido
                except ValueError:
                    print("Entrada inválida. Digite um número de 1 a 9.")
                    continue

            linha, coluna = POSITIONS[pos]
            tabuleiro[linha][coluna] = jogador_atual # Atualiza o tabuleiro com a jogada do jogador atual
            mostrar_tabuleiro(tabuleiro)

            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f"\n==> Jogador {jogador_atual} venceu a rodada!")
                vitorias[jogador_atual] += 1 # Atualiza o placar
                break
            elif tabuleiro_cheio(tabuleiro):
                print("\n==> Empate!")
                vitorias["Empate"] += 1
                break

            jogador_atual = jogador1 if jogador_atual == jogador2 else jogador2 # Alterna entre os jogadores

        print(f"\nPlacar atual: X = {vitorias['X']} | O = {vitorias['O']} | Empates = {vitorias['Empate']}") # Mostra o placar parcial
        resposta = input("\nJogar outra rodada? (s = sim / n = não): ").lower() # Pergunta se o jogador quer jogar mais uma rodada
        jogar_mais = (resposta == "s") # Continua ou encerra o laço externo

    # Exibe o placar final após todas as rodadas
    print("\n=== FIM DO JOGO ===")
    print("\nPlacar final:")
    print(f"X venceu {vitorias['X']} rodada(s)")
    print(f"O venceu {vitorias['O']} rodada(s)")
    print(f"Empates: {vitorias['Empate']}")
   

def jogar():
    print("=== JOGO DA VELHA ===")
    while True:
        modo = input("\nEscolha o modo de jogo:\n1 - Contra outro jogador\n2 - Contra o computador\n> ")
        while modo not in ["1", "2"]:
            modo = input("Modo inválido. Escolha 1 ou 2: ")

        jogador1 = input("Você quer ser X ou O? ").upper()
        while jogador1 not in ["X", "O"]:
            jogador1 = input("Escolha inválida. Digite X ou O: ").upper()

        computador = ("O" if jogador1 == "X" else "X") if modo == "2" else None

        rodada(modo, jogador1, computador) # Começa uma sequência de rodadas

        novo_jogo = input("\nDeseja iniciar um novo jogo? (s = sim / n = não): ").lower()
        if novo_jogo != "s":
            print("Obrigado por jogar!")
            break


if __name__ == "__main__":
    jogar()



