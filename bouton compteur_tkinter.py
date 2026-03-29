import tkinter as tk

def ajouter ():
    compteur.set(compteur.get() + 1)     #set met la valeur à jour et get récupère la valeur actuelle

fenetre = tk.Tk()
fenetre.title("Bouton compteur")
fenetre.geometry("500x300")

texte_titre = tk.Label(fenetre, text="Bouton Compteur")
texte_titre.pack()

compteur = tk.IntVar()
compteur_label = tk.Label(fenetre, textvariable=compteur)
compteur_label.pack()

bouton_plus = tk.Button(fenetre, text="Ajouter", command=ajouter)
bouton_plus.pack()

fenetre.mainloop()