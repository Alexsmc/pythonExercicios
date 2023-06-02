import tkinter as tk
from tkinter import messagebox
import random
import csv
import PIL

# Função para verificar o resultado do jogo
def check_winner(player_choice):
    choices = ['Pedra', 'Papel', 'Tesoura', 'Spock', 'Lagarto']
    computer_choice = random.choice(choices)

    # Exibir imagens de escolha
    player_img = PIL.Image.open(f"icons/{player_choice.lower()}.png")
    computer_img = PIL.Image.open(f"icons/{computer_choice.lower()}.png")
    player_icon.config(image=PIL.ImageTk.PhotoImage(player_img))
    computer_icon.config(image=PIL.ImageTk.PhotoImage(computer_img))

    # Atraso de 2 segundos antes de exibir o resultado
    window.after(2000, show_result, player_choice, computer_choice)

# Função para exibir o resultado do jogo
def show_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        messagebox.showinfo("Resultado", "Empate!")
    elif (player_choice == 'Pedra' and (computer_choice == 'Tesoura' or computer_choice == 'Lagarto')) or \
            (player_choice == 'Papel' and (computer_choice == 'Pedra' or computer_choice == 'Spock')) or \
            (player_choice == 'Tesoura' and (computer_choice == 'Papel' or computer_choice == 'Lagarto')) or \
            (player_choice == 'Spock' and (computer_choice == 'Pedra' or computer_choice == 'Tesoura')) or \
            (player_choice == 'Lagarto' and (computer_choice == 'Papel' or computer_choice == 'Spock')):
        messagebox.showinfo("Resultado", f"Você ganhou! O computador escolheu {computer_choice}.")
        player_score[0] += 1
    else:
        messagebox.showinfo("Resultado", f"Você perdeu! O computador escolheu {computer_choice}.")

    # Atualizar a pontuação do jogador
    score_label.config(text=f"Pontuação: {player_score[0]}")

    # Encerrar o jogo se o computador vencer
    if player_score[0] == 0:
        end_game()

# Função para encerrar o jogo e exibir o ranking
def end_game():
    messagebox.showinfo("Fim de Jogo", f"Você fez {player_score[0]} pontos.")
    save_score()
    show_ranking()

# Função para salvar a pontuação do jogador
def save_score():
    player_name = player_entry.get()
    score = player_score[0]

    with open('ranking.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player_name, score])

# Função para exibir o ranking dos 10 melhores jogadores
def show_ranking():
    messagebox.showinfo("Ranking", "Top 10 Jogadores:\n\n" + get_ranking())

# Função para obter o ranking dos 10 melhores jogadores
def get_ranking():
    ranking = "Nome do Jogador  |  Pontuação\n"
    ranking += "-" * 30 + "\n"

    with open('ranking.csv', 'r') as file:
        reader = csv.reader(file)
        sorted_scores = sorted(reader, key=lambda row: int(row[1]), reverse=True)
        top_10_scores = sorted_scores[:10]

        for row in top_10_scores:
            player_name, score = row
            ranking += f"{player_name:16}  |  {score}\n"

    return ranking

# Criação da janela
window = tk.Tk()
window.title("Pedra, Papel, Tesoura, Spock, Lagarto")

# Criação do rótulo e campo de entrada para o nome do jogador
player_label = tk.Label(window, text="Nome do Jogador:")
player_label.pack()

player_entry = tk.Entry(window)
player_entry.pack()

# Criação dos ícones para as escolhas
player_icon = tk.Label(window)
player_icon.pack()

computer_icon = tk.Label(window)
computer_icon.pack()

# Carregar as imagens dos ícones
rock_img = PIL.Image.open("icons/rock.png")
paper_img = PIL.Image.open("icons/paper.png")
scissors_img = PIL.Image.open("icons/scissors.png")
spock_img = PIL.Image.open("icons/spock.png")
lizard_img = PIL.Image.open("icons/lizard.png")

# Redimensionar as imagens dos ícones
resized_rock_img = rock_img.resize((100, 100))
resized_paper_img = paper_img.resize((100, 100))
resized_scissors_img = scissors_img.resize((100, 100))
resized_spock_img = spock_img.resize((100, 100))
resized_lizard_img = lizard_img.resize((100, 100))

# Configurar as imagens dos ícones
player_icon.config(image=PIL.ImageTk.PhotoImage(resized_rock_img))
computer_icon.config(image=PIL.ImageTk.PhotoImage(resized_rock_img))

# Criação dos botões
btn_rock = tk.Button(window, image=PIL.ImageTk.PhotoImage(resized_rock_img), command=lambda: check_winner('Pedra'))
btn_rock.pack(side=tk.LEFT)

btn_paper = tk.Button(window, image=PIL.ImageTk.PhotoImage(resized_paper_img), command=lambda: check_winner('Papel'))
btn_paper.pack(side=tk.LEFT)

btn_scissors = tk.Button(window, image=PIL.ImageTk.PhotoImage(resized_scissors_img), command=lambda: check_winner('Tesoura'))
btn_scissors.pack(side=tk.LEFT)

btn_spock = tk.Button(window, image=PIL.ImageTk.PhotoImage(resized_spock_img), command=lambda: check_winner('Spock'))
btn_spock.pack(side=tk.LEFT)

btn_lizard = tk.Button(window, image=PIL.ImageTk.PhotoImage(resized_lizard_img), command=lambda: check_winner('Lagarto'))
btn_lizard.pack(side=tk.LEFT)

# Variável para armazenar a pontuação do jogador
player_score = [0]

# Criação do rótulo para exibir a pontuação do jogador
score_label = tk.Label(window, text="Pontuação: 0")
score_label.pack()

# Executar o loop principal da interface
window.mainloop()
