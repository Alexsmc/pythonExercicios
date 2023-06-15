import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json


class LivroJogoAssistente(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Assistente para Livro-Jogo")
        self.geometry("500x400")

        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(pady=20)

        self.mostrar_personagem_frame = tk.Frame(self)

        self.nome_label = tk.Label(self.mostrar_personagem_frame, text="Digite o nome do jogador:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self.mostrar_personagem_frame)
        self.nome_entry.pack()

        self.novo_jogador_button = tk.Button(self.menu_frame, text="Novo Jogador", command=self.exibir_escolha_pocao)
        self.novo_jogador_button.pack(pady=10)

        self.continue_button = tk.Button(self.menu_frame, text="Continue", command=self.continue_jogo)
        self.continue_button.pack(pady=10)

        self.batalha_button = tk.Button(self.menu_frame, text="Batalha")
        self.batalha_button.pack(pady=10)

        self.salvar_sair_button = tk.Button(self.menu_frame, text="Salvar e Sair", command=self.salvar_sair)
        self.salvar_sair_button.pack(pady=10)

        self.nome = ""
        self.habilidade = 0
        self.energia = 0
        self.sorte = 0
        self.provisoes = 0
        self.ouro = 0
        self.pocoes = ["Nenhuma", "Poção da Habilidade", "Poção da Força", "Poção da Fortuna"]
        self.pocao_escolhida = tk.StringVar()
        self.pocao_escolhida.set(self.pocoes[0])
        self.mochila = []
        self.joias = []
        self.posicao = 0

        self.pocoes_combobox = None

    def exibir_escolha_pocao(self):
        self.nome = self.nome_entry.get()
        if self.nome:
            self.menu_frame.pack_forget()
            self.mostrar_personagem_frame.pack(pady=20)

            self.nome_label.destroy()
            self.nome_entry.destroy()

            self.pocoes_combobox = tk.OptionMenu(self.mostrar_personagem_frame, self.pocao_escolhida, *self.pocoes)
            self.pocoes_combobox.pack(pady=10)

            confirmar_button = tk.Button(self.mostrar_personagem_frame, text="Confirmar",
                                         command=self.criar_personagem)
            confirmar_button.pack(pady=10)

    def novo_jogador(self):
        self.menu_frame.pack_forget()
        self.novo_jogador_frame.pack(pady=20)

        self.nome_entry.delete(0, tk.END)
        self.nome_entry.focus_set()

        self.pocao_var.set(None)

        self.construir_novo_jogador()

    def criar_personagem(self):
        pocao_escolhida = self.pocao_escolhida.get()
        if pocao_escolhida != "Nenhuma":
            self.habilidade = random.randint(1, 6) + 6
            self.energia = sum([random.randint(1, 6) for _ in range(2)]) + 12
            self.sorte = random.randint(1, 6) + 6
            self.provisoes = 10
            self.ouro = 10
            self.mochila = []
            self.joias = []
            self.posicao = 1

            self.pocoes.remove(pocao_escolhida)

            self.mostrar_personagem_frame.pack_forget()
            self.menu_frame.pack(pady=20)

            self.atualizar_interface()
            self.salvar_jogador()

    def continue_jogo(self):
        try:
            with open("jogador.json", "r") as arquivo:
                jogador_salvo = json.load(arquivo)

            self.nome = jogador_salvo["nome"]
            self.habilidade = jogador_salvo["habilidade"]
            self.energia = jogador_salvo["energia"]
            self.sorte = jogador_salvo["sorte"]
            self.provisoes = jogador_salvo["provisoes"]
            self.ouro = jogador_salvo["ouro"]
            self.mochila = jogador_salvo["mochila"]
            self.joias = jogador_salvo["joias"]
            self.posicao = jogador_salvo["posicao"]

            self.mostrar_personagem_frame.pack_forget()
            self.menu_frame.pack(pady=20)

            self.atualizar_interface()
        except FileNotFoundError:
            messagebox.showinfo("Erro", "Nenhum jogador salvo encontrado.")

    def salvar_sair(self):
        self.salvar_jogador()
        self.destroy()

    def salvar_jogador(self):
        nova_posicao = simpledialog.askinteger("Salvar e Sair", "Digite a nova posição do jogador:")
        if nova_posicao:
            jogador = {
                "nome": self.nome,
                "habilidade": self.habilidade,
                "energia": self.energia,
                "sorte": self.sorte,
                "provisoes": self.provisoes,
                "ouro": self.ouro,
                "pocoes": self.pocoes,
                "mochila": self.mochila,
                "joias": self.joias,
                "posicao": nova_posicao
            }
            with open("jogador.json", "w") as arquivo:
                json.dump(jogador, arquivo, indent=4)
            messagebox.showinfo("Salvar e Sair", "Jogador salvo com sucesso!")

    def atualizar_interface(self):
        self.menu_frame.pack_forget()
        self.mostrar_personagem_frame.pack(pady=20)

        self.mostrar_personagem()

    def mostrar_personagem(self):
        self.mostrar_personagem_frame.destroy()

        self.mostrar_personagem_frame = tk.Frame(self)
        self.mostrar_personagem_frame.pack(pady=20)

        tk.Label(self.mostrar_personagem_frame, text=f"Nome: {self.nome}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Habilidade: {self.habilidade}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Energia: {self.energia}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Sorte: {self.sorte}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Provisões: {self.provisoes}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Ouro: {self.ouro}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Mochila: {', '.join(self.mochila)}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Joias: {', '.join(self.joias)}").pack()
        tk.Label(self.mostrar_personagem_frame, text=f"Posição: {self.posicao}").pack()

        voltar_button = tk.Button(self.mostrar_personagem_frame, text="Voltar ao Menu Inicial",
                                  command=self.voltar_menu_inicial)
        voltar_button.pack(pady=10)

    def voltar_menu_inicial(self):
        self.mostrar_personagem_frame.pack_forget()
        self.menu_frame.pack(pady=20)


if __name__ == "__main__":
    app = LivroJogoAssistente()
    app.mainloop()
