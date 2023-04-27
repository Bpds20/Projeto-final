tabuleiro = ["", "", "", "",
             "", "", "", "",
             "", "", "", ""]
jogador_atual = "O"
def exibir_tabuleiro():
    print(tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2] + " | " + tabuleiro[3])
    print("--+---+--")
    print(tabuleiro[4] + " | " + tabuleiro[5] + " | " + tabuleiro[6] + " | " + tabuleiro[7])
    print("--+---+--")
    print(tabuleiro[8] + " | " + tabuleiro[9] + " | " + tabuleiro[10] + " | " + tabuleiro[11])
def verificar_fim_de_jogo():
    # Verificar linhas horizontais
    for i in range(0, 11, 4):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] and tabuleiro[i] != "":
            return True
    # Verificar linhas verticais
    for i in range(0, 4):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] and tabuleiro[i] != "":
            return True
    # Verificar diagonais
    if tabuleiro[0] == tabuleiro[5] == tabuleiro[9] and tabuleiro[0] != "":
        return True
    if tabuleiro[3] == tabuleiro[5] == tabuleiro[7] and tabuleiro[3] != "":
        return True
    return False
while not verificar_fim_de_jogo() and "" in tabuleiro:
    exibir_tabuleiro()
    celula = int(input("Digite a célula para colocar o sinal (de 1 a 12): ")) - 1
    if tabuleiro[celula] == "":
        tabuleiro[celula] = jogador_atual
        if jogador_atual == "O":
            jogador_atual = "X"
        elif jogador_atual == "X":
            jogador_atual = "O"
    else:
        print("Célula ocupada. Escolha outra.")
if verificar_fim_de_jogo():
    exibir_tabuleiro()
    print("Jogador " + jogador_atual + " venceu!")
else:
    exibir_tabuleiro()
    print("Empate.")