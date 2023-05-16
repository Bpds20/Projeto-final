menu = ttk.Button(root, text="MENU")
menu.grid(row=3, column=3, sticky='snew', ipadx=40, ipady=40)
menu.config(command=lambda: opcoesmenu())

def jogar_partida():
    print("Opção A - Jogar partida")
    # Lógica para jogar a partida

def carregar_partida():
    print("Opção B - Carregar partida a partir de um arquivo")
    # Lógica para carregar uma partida a partir de um arquivo

def regras_do_jogo():
    tkinter.messagebox.showinfo("Regras do jogo", "O objetivo deste jogo é ser o primeiro a contruir uma linha de três peças da mesma cor na horizontal, vertical ou diagonal. \n O jogo realiza-se no tabuleiro inicialmente vazio.\n Em cada jogada, cada jogador realiza uma das seguintes opções: \n ->Coloca uma peça verde num quadrado vazio; \n ->Substitui uma peça verde por uma peça amarela; \n ->Substtui uma peça amarela por uma peça vermelha. \n De notar que as peças vermelhas não podem ser substituidas. Insto significa que o jogo tem de terminar sempre. \n À medida que o tabuleiro fica com peças vermelhas, é inevitável que surja uma linha de três peças.")

def sair_do_jogo():
   
    root.quit()

def opcoesmenu():
    root = tkinter.Tk()
    root.title("Menu")

    button_a = Button(root, text="Jogar partida", command=jogar_partida)
    button_a.pack()

    button_b = Button(root, text="Carregar partida", command=carregar_partida)
    button_b.pack()

    button_c = Button(root, text="Regras do jogo", command=regras_do_jogo)
    button_c.pack()

    button_d = Button(root, text="Sair do jogo", command=sair_do_jogo)
    button_d.pack()

    root.mainloop()

