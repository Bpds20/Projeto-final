import random

# definindo as constantes
GREEN = 'G'
YELLOW = 'Y'
RED = 'R'
#definie tabuleiro
BOARD_ROWS = 3
BOARD_COLS = 4
tabuleiro = ["", "", "", "",
             "", "", "", "",
             "", "", "", ""]
# definindo as variáveis globais
board = [[None for j in range(BOARD_COLS)] for i in range(BOARD_ROWS)]
players = [GREEN, YELLOW]
current_player = None
game_over = False

# definindo as funções
def print_board():
    print('   1  2  3  4')
    for i in range(BOARD_ROWS):
        row = '{}|'.format(i+1)
        for j in range(BOARD_COLS):
            if board[i][j]:
                row += ' {} |'.format(board[i][j])
            else:
                row += '   |'
        print(row)

def get_player_choice():
    while True:
        try:
            row = int(input('Escolha a linha (1-{}): '.format(BOARD_ROWS)))
            col = int(input('Escolha a coluna (1-{}): '.format(BOARD_COLS)))
            if row < 1 or row > BOARD_ROWS or col < 1 or col > BOARD_COLS:
                raise ValueError()
            if board[row-1][col-1]:
                print('Posição ocupada. Tente novamente.')
            else:
                return (row-1, col-1)
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def check_winner():
    # checar linhas
    for i in range(BOARD_ROWS):
        if board[i][0] == board[i][1] == board[i][2] or board[i][1] == board[i][2] == board[i][3]:
            if board[i][1]:
                return board[i][1]
    # checar colunas
    for j in range(BOARD_COLS):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j]:
                return board[0][j]
    # checar diagonais
    if board[0][0] == board[1][1] == board[2][2] or board[0][3] == board[1][2] == board[2][1]:
        if board[1][1]:
            return board[1][1]
    return None

def switch_player():
    global current_player
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]

def bot_turn():
    print('BOT:')
    while True:
        row = random.randint(0, BOARD_ROWS-1)
        col = random.randint(0, BOARD_COLS-1)
        if not board[row][col]:
            board[row][col] = current_player
            print_board()
            winner = check_winner()
            if winner:
                print('Vencedor: {}'.format(winner))
                global game_over
                game_over = True
            break

# jogo
print('Bem-vindo ao jogo de três em linha!\n')

# menu de opções
while True:
    print('Selecione uma opção:')
    print('A. Jogar uma partida')
    print('B. Sair')
    option = input().upper()

    if option == 'A':
        # definir a ordem dos jogadores
        current_player = random.choice(players)
        print('O primeiro jogador é {}'.format(current_player))
        # limpar o tabuleiro
        board = [[None for j in range(BOARD_COLS)] for i in range(BOARD_ROWS)]
        game_over = False
        # jogo
        while not game_over:
            print_board()
            if current_player == players[0]:
                choice = get_player_choice()
                board[choice[0]][choice[1]] = current_player
            else:
                bot_turn()
            winner = check_winner()
            if winner:
                print('Vencedor: {}'.format(winner))
                game_over = True
            else:
                switch_player()
        print_board()
    elif option == 'B':
        break
    else:
        print('Opção inválida. Tente novamente.')

