import tkinter as tk
from tkinter import messagebox

# Fonction pour vérifier s'il y a un gagnant
def check_winner():
    # Listes des combinaisons gagnantes
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6]  # diagonales
    ]

    for combo in win_combinations:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            return True

    return False

# Fonction pour gérer le clic sur un bouton
def button_click(idx):
    global player

    if buttons[idx]['text'] == "":
        buttons[idx]['text'] = player
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Le joueur {player} a gagné !")
            reset_game()
        elif "" not in [button['text'] for button in buttons]:
            messagebox.showinfo("Tic Tac Toe", "Match nul !")
            reset_game()
        else:
            player = "X" if player == "O" else "O"

# Fonction pour réinitialiser le jeu
def reset_game():
    global player
    player = "X"
    for button in buttons:
        button['text'] = ""

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tic Tac Toe")

# Liste de boutons pour les cases du jeu
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 20), width=4, height=2, command=lambda idx=i: button_click(idx))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Variable pour suivre le joueur actuel
player = "X"

# Bouton de réinitialisation
reset_button = tk.Button(root, text="Nouvelle partie", command=reset_game)
reset_button.grid(row=3, columnspan=3)

# Lancement de la boucle principale
root.mainloop()