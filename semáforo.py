tabuleiro = ["", "", "",
             "", "", "",
             "", "", ""]
jogador_atual = "V"

def exibir_tabuleiro():
    print(tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("--+---+--")
    print(tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("--+---+--")
    print(tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])

def verificar_fim_de_jogo():
    # Verificar linhas horizontais
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] and tabuleiro[i] != "":
            return True
    # Verificar linhas verticais
    for i in range(0, 3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] and tabuleiro[i] != "":
            return True
    # Verificar diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0] != "":
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[2] != "":
        return True
    return False

while not verificar_fim_de_jogo() and "" in tabuleiro:
    exibir_tabuleiro()
    celula = int(input("Digite a célula para colocar o sinal (de 1 a 9): ")) - 1
    if tabuleiro[celula] == "":
        tabuleiro[celula] = jogador_atual
        if jogador_atual == "V":
            jogador_atual = "A"
        elif jogador_atual == "A":
            jogador_atual = "V"
    else:
        print("Célula ocupada. Escolha outra.")
if verificar_fim_de_jogo():
    exibir_tabuleiro()
    print("Jogador " + jogador_atual + " venceu!")
else:
    exibir_tabuleiro()
    print("Empate.")
